from typing import List

from model.Patient import Patient


class EmptyListStorage:
    def __init__(self, *args):
        super().__init__()
        self._patients: List[Patient] = []

    def insert(self, patient: Patient):
        self._patients.append(patient)

    def get_all_patients(self) -> List[Patient]:
        return self._patients

    def search_by_name(self, name: str, offset=0, limit=None) -> List[Patient]:
        result = [patient for patient in self._patients if name.lower() in patient.full_name.lower()]
        return result[offset:offset + limit] if limit else result

    def delete_by_name(self, name: str) -> int:
        patients_to_remove = [patient for patient in self._patients if name.lower() in patient.full_name.lower()]
        for patient in patients_to_remove:
            self._patients.remove(patient)
        return len(patients_to_remove)

    def search_by_birth_date(self, birth_date: str, offset=0, limit=None) -> List[Patient]:
        result = [patient for patient in self._patients if birth_date == patient.birth_date]
        return result[offset:offset + limit] if limit else result

    def delete_by_birth_date(self, birth_date: str) -> int:
        patients_to_remove = [patient for patient in self._patients if birth_date == patient.birth_date]
        for patient in patients_to_remove:
            self._patients.remove(patient)
        return len(patients_to_remove)

    def search_by_address(self, address: str, offset=0, limit=None) -> List[Patient]:
        result = [patient for patient in self._patients if address.lower() == patient.address.lower()]
        return result[offset:offset + limit] if limit else result

    def delete_by_address(self, address: str) -> int:
        patients_to_remove = [patient for patient in self._patients if address.lower() == patient.address.lower()]
        for patient in patients_to_remove:
            self._patients.remove(patient)
        return len(patients_to_remove)

    def search_by_date_of_patients_appointment(self, date_of_patients_appointment: str, offset=0, limit=None)\
            -> List[Patient]:
        result = [patient for patient in self._patients if date_of_patients_appointment ==
                  patient.date_of_patients_appointment]
        return result[offset:offset + limit] if limit else result

    def delete_by_date_of_patients_appointment(self, date_of_patients_appointment: str) -> int:
        patients_to_remove = [patient for patient in self._patients if
                              date_of_patients_appointment == patient.date_of_patients_appointment]
        for patient in patients_to_remove:
            self._patients.remove(patient)
        return len(patients_to_remove)

    def search_by_doctor_full_name(self, doctor_full_name: str, offset=0, limit=None) -> List[Patient]:
        result = [patient for patient in self._patients if doctor_full_name.lower() == patient.doctor_full_name.lower()]
        return result[offset:offset + limit] if limit else result

    def delete_by_doctor_full_name(self, doctor_full_name: str) -> int:
        patients_to_remove = [patient for patient in self._patients if
                              doctor_full_name.lower() == patient.doctor_full_name.lower()]
        for patient in patients_to_remove:
            self._patients.remove(patient)
        return len(patients_to_remove)

    def search_by_report(self, report: str, offset=0, limit=None) -> List[Patient]:
        result = [patient for patient in self._patients if report.lower() == patient.report.lower()]
        return result[offset:offset + limit] if limit else result

    def delete_by_report(self, report: str) -> int:
        patients_to_remove = [patient for patient in self._patients if
                              report.lower() == patient.report.lower()]
        for patient in patients_to_remove:
            self._patients.remove(patient)
        return len(patients_to_remove)
