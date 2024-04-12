import tkinter as tk
from tkinter import ttk


class SearchResultsWindow:
    def __init__(self, parent, results):
        self.parent = parent
        self.results = results

        self.window = tk.Toplevel(parent)
        self.window.title("Результаты поиска")

        columns = ("ID", "Full Name", "Birth Date", "Address", "Date of patients appointment",
                   "Doctor full name", "Report")
        self.treeview = ttk.Treeview(self.window, columns=columns, show="headings")

        for col in columns:
            self.treeview.heading(col, text=col)

        for col in columns:
            self.treeview.column(col, anchor="center")

        for patient in results:
            self.treeview.insert("", "end", values=(
                patient.id, patient.full_name, patient.birth_date, patient.address, patient.date_of_patients_appointment,
                patient.doctor_full_name, patient.report))

        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar.set)

        self.treeview.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")