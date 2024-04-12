import xml.dom.minidom
from typing import List
from xml.sax import ContentHandler

from model.Patient import Patient
from controller.EmptyListStorage import EmptyListStorage


class PatientHandler(ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.current_patient = None
        self.patients = []

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "patient":
            self.current_patient = {'id': attributes['id']}

    def endElement(self, tag):
        if tag == "patient":
            self.patients.append(self.current_patient)
            self.current_patient = None
        self.current_tag = ""

    def characters(self, content):
        if self.current_patient is not None:
            self.current_patient[self.current_tag] = content


class XmlPatientController(EmptyListStorage):
    def __init__(self, file):
        super().__init__()
        self.file: str = file
        self._patients: List[Patient] = self.__load_patient_from_xml()

    def __load_patient_from_xml(self):
        handler = PatientHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(self.file)

        patient_list = []
        for patient_data in handler.patients:
            patient = Patient(patient_data['id'], patient_data['full_name'], patient_data['birth_date'],
                              patient_data['address'], patient_data['date_of_patients_appointment'],
                              patient_data['doctor_full_name'], patient_data['report'])
            patient_list.append(patient)

        return patient_list

    def __save_patients_to_xml(self):
        doc = xml.dom.minidom.Document()
        root = doc.createElement("patients")
        doc.appendChild(root)
        for patient in self._patients:
            patient_element = doc.createElement("patient")
            for key, value in patient.__dict__.items():
                if key != 'id':
                    element = doc.createElement(key)
                    element.appendChild(doc.createTextNode(str(value)))
                    patient_element.appendChild(element)
            patient_element.setAttribute("id", str(patient.__dict__['id']))
            root.appendChild(patient_element)
        with open(self.file, "w") as f:
            f.write(doc.toprettyxml(indent="  "))

    def save(self):
        self.__save_patients_to_xml()
