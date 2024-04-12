from typing import List

import psycopg2
import datetime

from model.Patient import Patient


class PatientDao:
    def __init__(self):
        try:
            self.__connection = psycopg2.connect(
                dbname='postgres',
                user='postgres',
                password='postgres',
                host='localhost',
                port='5432'
            )
        except UnicodeDecodeError:
            print('Can`t establish connection to database')

        self.__find_by_id_query = ('SELECT p.id, p.full_name, p.birth_date, p.address, p.date_of_patients_appointment,'
                                   ' p.doctor_full_name, p.report FROM patients p WHERE p.id = %s')
        self.__find_all_query = ('SELECT p.id, p.full_name, p.birth_date, p.address, p.date_of_patients_appointment, '
                                 'p.doctor_full_name, p.report FROM patients p')
        self.__find_by_full_name_query = ('SELECT p.id, p.full_name, p.birth_date, p.address,'
                                          ' p.date_of_patients_appointment, p.doctor_full_name, p.report'
                                          ' FROM patients p WHERE full_name LIKE %s')
        self.__find_by_birth_date_query = ('SELECT p.id, p.full_name, p.birth_date, p.address, '
                                           'p.date_of_patients_appointment, p.doctor_full_name,p.report '
                                           'FROM patients p WHERE birth_date = %s')
        self.__find_by_address_query = ('SELECT p.id, p.full_name, p.birth_date, p.address,'
                                        ' p.date_of_patients_appointment, p.doctor_full_name, p.report'
                                        ' FROM patients p WHERE address = %s')
        self.__find_by_date_of_patients_appointment_query = ('SELECT p.id, p.full_name, p.birth_date, p.address,'
                                                             ' p.date_of_patients_appointment, p.doctor_full_name, '
                                                             'p.report FROM patients p WHERE '
                                                             'date_of_patients_appointment = %s')
        self.__find_by_doctor_full_name_query = ('SELECT p.id, p.full_name, p.birth_date, p.address,'
                                                 ' p.date_of_patients_appointment, p.doctor_full_name, p.report '
                                                 'FROM patients p WHERE doctor_full_name = %s')
        self.__find_by_report_query = ('SELECT p.id, p.full_name, p.birth_date, p.address,'
                                       ' p.date_of_patients_appointment, p.doctor_full_name, p.report '
                                       'FROM patients p WHERE report = %s')
        self.__delete_by_full_name_query = 'DELETE FROM patients WHERE full_name LIKE %s'
        self.__delete_by_birth_date_query = 'DELETE FROM patients WHERE birth_date = %s'
        self.__delete_by_address_query = 'DELETE FROM patients WHERE address = %s'
        self.__delete_by_date_of_patients_appointment_query = ('DELETE FROM patients WHERE '
                                                               'date_of_patients_appointment = %s')
        self.__delete_by_doctor_full_name_query = 'DELETE FROM patients WHERE doctor_full_name = %s'
        self.__delete_by_report_query = 'DELETE FROM patients WHERE report = %s'
        self.__update_by_id_query = ('UPDATE patients SET full_name = %s, birth_date = %s, address = %s, '
                                     'date_of_patients_appointment = %s, doctor_full_name = %s, report = %s '
                                     'WHERE id = %s')
        self.__create_query = ('INSERT INTO patients (full_name, birth_date, address, date_of_patients_appointment,'
                               ' doctor_full_name, report) VALUES (%s, %s, %s, %s, %s, %s)')

    def find_by_id(self, patient_id) -> Patient | None:
        with self.__connection.cursor() as curs:
            curs.execute(self.__find_by_id_query, (patient_id,))
            query = curs.fetchall()
        if query:
            return Patient(*query[0])
        else:
            return None

    def find_all(self) -> List[Patient] | None:
        with self.__connection.cursor() as curs:
            curs.execute(self.__find_all_query)
            query = curs.fetchall()
        if not query:
            return None
        return [Patient(*element) for element in query]

    def find_by_full_name(self, name: str) -> List[Patient] | None:
        with self.__connection.cursor() as curs:
            curs.execute(self.__find_by_full_name_query, (f'%{name}%',))
            query = curs.fetchall()
        if not query:
            return None
        return [Patient(*element) for element in query]

    def find_by_birth_date(self, date: datetime.date) -> List[Patient] | None:
        with self.__connection.cursor() as curs:
            curs.execute(self.__find_by_birth_date_query, (date,))
            query = curs.fetchall()
        if not query:
            return None
        return [Patient(*element) for element in query]

    def find_by_address(self, address: str) -> List[Patient] | None:
        with self.__connection.cursor() as curs:
            curs.execute(self.__find_by_address_query, (address,))
            query = curs.fetchall()
        if not query:
            return None
        return [Patient(*element) for element in query]

    def find_by_doctor_full_name(self, doctor_full_name: str) -> List[Patient] | None:
        with self.__connection.cursor() as curs:
            curs.execute(self.__find_by_doctor_full_name_query, (doctor_full_name,))
            query = curs.fetchall()
        if not query:
            return None
        return [Patient(*element) for element in query]

    def find_by_date_of_patients_appointment(self, date_of_patients_appointment: datetime.date) -> List[Patient] | None:
        with self.__connection.cursor() as curs:
            curs.execute(self.__find_by_date_of_patients_appointment_query, (date_of_patients_appointment,))
            query = curs.fetchall()
        if not query:
            return None
        return [Patient(*element) for element in query]

    def find_by_report(self, report: str) -> List[Patient] | None:
        with self.__connection.cursor() as curs:
            curs.execute(self.__find_by_report_query, (report,))
            query = curs.fetchall()
        if not query:
            return None
        return [Patient(*element) for element in query]

    def delete_by_full_name(self, name: str):
        with self.__connection.cursor() as curs:
            curs.execute(self.__delete_by_full_name_query, (f'%{name}%',))
            # self.__connection.commit()
            return curs.rowcount

    def delete_by_birth_date(self, date: datetime.date):
        with self.__connection.cursor() as curs:
            curs.execute(self.__delete_by_birth_date_query, (date,))
            # self.__connection.commit()
            return curs.rowcount

    def delete_by_address(self, address: str):
        with self.__connection.cursor() as curs:
            curs.execute(self.__delete_by_address_query, (address,))
            # self.__connection.commit()
            return curs.rowcount

    def delete_by_doctor_full_name(self, doctor_full_name: str):
        with self.__connection.cursor() as curs:
            curs.execute(self.__delete_by_doctor_full_name_query, (doctor_full_name,))
            # self.__connection.commit()
            return curs.rowcount

    def delete_by_date_of_patients_appointment(self, date_of_patients_appointment: datetime.date):
        with self.__connection.cursor() as curs:
            curs.execute(self.__delete_by_date_of_patients_appointment_query, (date_of_patients_appointment,))
            # self.__connection.commit()
            return curs.rowcount

    def delete_by_report(self, report: str):
        with self.__connection.cursor() as curs:
            curs.execute(self.__delete_by_report_query, (report,))
            # self.__connection.commit()
            return curs.rowcount

    def create(self, patient: Patient) -> Patient:
        with self.__connection.cursor() as curs:
            curs.execute(self.__create_query + ' RETURNING id',
                         (patient.full_name, patient.birth_date, patient.address,
                          patient.date_of_patients_appointment, patient.doctor_full_name, patient.report))
            last_row_id = curs.fetchone()[0]
            # self.__connection.commit()
            curs.execute(self.__find_by_id_query, (last_row_id,))
            created_patient = curs.fetchone()
            return Patient(*created_patient)

    def save_db(self):
        self.__connection.commit()

    def __del__(self):
        self.__connection.close()
