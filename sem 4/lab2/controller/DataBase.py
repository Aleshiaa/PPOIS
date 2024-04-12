import datetime
from typing import List

from controller.PatientDao import PatientDao
from model.PatientDto import PatientDto
from model.Patient import Patient


def to_patient_dto(patient: Patient) -> PatientDto:
    patient_dto: PatientDto = PatientDto(full_name=patient.full_name, address=patient.address,
                                         birth_date=patient.birth_date,
                                         date_of_patients_appointment=patient.date_of_patients_appointment,
                                         doctor_full_name=patient.doctor_full_name, report=patient.report,
                                         id=patient.id)
    return patient_dto


def to_patient_entity(patient_dto: PatientDto) -> Patient:
    patient: Patient = Patient(address=patient_dto.address, birth_date=patient_dto.birth_date,
                               doctor_full_name=patient_dto.doctor_full_name, report=patient_dto.report,
                               date_of_patients_appointment=patient_dto.date_of_patients_appointment,
                               full_name=patient_dto.full_name, id=None)
    return patient


class DBPatientController:
    def __init__(self):
        self.__patient_dao = PatientDao()

    def get_by_id(self, patient_id: int) -> PatientDto:
        patient: Patient = self.__patient_dao.find_by_id(patient_id)
        if patient is None:
            raise RuntimeWarning("No patient with id: " + str(patient_id))
        return to_patient_dto(patient)

    def get_all(self) -> List[PatientDto]:
        patients: List[Patient] = self.__patient_dao.find_all()
        patient_dtos: List[PatientDto] = [to_patient_dto(patient) for patient in patients]
        return patient_dtos

    def get_by_full_name(self, name: str) -> List[PatientDto]:
        patients: List[Patient] = self.__patient_dao.find_by_full_name(name)
        if not patients:
            return []
        return [to_patient_dto(patient) for patient in patients]

    def get_by_birth_date(self, date: datetime.date) -> List[PatientDto]:
        patients: List[Patient] = self.__patient_dao.find_by_birth_date(date)
        if not patients:
            return []
        return [to_patient_dto(patient) for patient in patients]

    def get_by_address(self, address: str) -> List[PatientDto]:
        patients: List[Patient] = self.__patient_dao.find_by_address(address)
        if not patients:
            return []
        return [to_patient_dto(patient) for patient in patients]

    def get_by_date_of_patients_appointment(self, appointment_date: datetime.date) -> List[PatientDto]:
        patients: List[Patient] = self.__patient_dao.find_by_date_of_patients_appointment(appointment_date)
        if not patients:
            return []
        return [to_patient_dto(patient) for patient in patients]

    def get_by_doctor_full_name(self, doctor_name: str) -> List[PatientDto]:
        patients: List[Patient] = self.__patient_dao.find_by_doctor_full_name(doctor_name)
        if not patients:
            return []
        return [to_patient_dto(patient) for patient in patients]

    def get_by_report(self, report_text: str) -> List[PatientDto]:
        patients: List[Patient] = self.__patient_dao.find_by_report(report_text)
        if not patients:
            return []
        return [to_patient_dto(patient) for patient in patients]

    def delete_by_full_name(self, name: str):
        patients: List[Patient] = self.__patient_dao.find_by_full_name(name)
        if patients is None:
            return 0
        return self.__patient_dao.delete_by_full_name(name)

    def delete_by_birth_date(self, date: datetime.date):
        patients: List[Patient] = self.__patient_dao.find_by_birth_date(date)
        if patients is None:
            return 0
        return self.__patient_dao.delete_by_birth_date(date)

    def delete_by_address(self, address: str):
        patients: List[Patient] = self.__patient_dao.find_by_address(address)
        if patients is None:
            return 0
        return self.__patient_dao.delete_by_address(address)

    def delete_by_date_of_patients_appointment(self, appointment_date: datetime.date):
        patients: List[Patient] = self.__patient_dao.find_by_date_of_patients_appointment(appointment_date)
        if patients is None:
            return 0
        return self.__patient_dao.delete_by_date_of_patients_appointment(appointment_date)

    def delete_by_doctor_full_name(self, doctor_name: str):
        patients: List[Patient] = self.__patient_dao.find_by_doctor_full_name(doctor_name)
        if patients is None:
            return 0
        return self.__patient_dao.delete_by_doctor_full_name(doctor_name)

    def delete_by_report(self, report_text: str):
        patients: List[Patient] = self.__patient_dao.find_by_report(report_text)
        if patients is None:
            return 0
        return self.__patient_dao.delete_by_report(report_text)

    def create(self, dto: PatientDto) -> PatientDto:
        patient: Patient = to_patient_entity(dto)
        patient_created: Patient = self.__patient_dao.create(patient)
        return to_patient_dto(patient_created)

    def save_db(self):
        self.__patient_dao.save_db()
