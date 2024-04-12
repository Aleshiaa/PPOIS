import datetime
from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Patient:
    id: int
    full_name: str
    birth_date: datetime.date
    address: str
    date_of_patients_appointment: datetime.date
    doctor_full_name: str
    report: str
