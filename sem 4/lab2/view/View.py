import datetime
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from tkcalendar import DateEntry
from anytree import Node, RenderTree

from Search import SearchResultsWindow
from controller.DataBase import DBPatientController
from model.PatientDto import PatientDto
from controller.XML import XmlPatientController
from model.Patient import Patient

db_patient_controller: DBPatientController = DBPatientController()
try:
    filename = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if filename:
        xml_patient_controller = XmlPatientController(filename)
except FileNotFoundError:
    print("Файл не найден или не выбран.")
except Exception as e:
    print("Произошла ошибка:", e)
is_database = True
data = db_patient_controller.get_all()


class SearchWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Поиск")
        self.window.grab_set()
        self.full_name_label = ttk.Label(self.window, text="Full Name:")
        self.full_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.full_name_entry = ttk.Entry(self.window)
        self.full_name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.birth_date_label = ttk.Label(self.window, text="Birth Date (YYYY-MM-DD):")
        self.birth_date_label.grid(row=1, column=0, padx=5, pady=5)
        self.birth_date_entry = DateEntry(self.window, date_pattern='yyyy-mm-dd', date=None)
        self.birth_date_entry.grid(row=1, column=1, padx=5, pady=5)
        self.birth_date_entry.set_date(datetime.date(1111, 11, 11))

        self.doctor_full_name_label = ttk.Label(self.window, text="Doctor Full Name:")
        self.doctor_full_name_label.grid(row=2, column=0, padx=5, pady=5)
        self.doctor_full_name_entry = ttk.Entry(self.window)
        self.doctor_full_name_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = ttk.Label(self.window, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = ttk.Entry(self.window)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.appointment_date_label = ttk.Label(self.window, text="Appointment Date (YYYY-MM-DD):")
        self.appointment_date_label.grid(row=4, column=0, padx=5, pady=5)
        self.appointment_date_entry = DateEntry(self.window, date_pattern='yyyy-mm-dd')
        self.appointment_date_entry.grid(row=4, column=1, padx=5, pady=5)
        self.appointment_date_entry.set_date(datetime.date(1111, 11, 11))

        self.report_label = ttk.Label(self.window, text="Report:")
        self.report_label.grid(row=5, column=0, padx=5, pady=5)
        self.report_entry = ttk.Entry(self.window)
        self.report_entry.grid(row=5, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(self.window, text="Найти", command=self.search)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

    def search(self):
        full_name: str = self.full_name_entry.get()
        birth_date: str = self.birth_date_entry.get()
        doctor_full_name: str = self.doctor_full_name_entry.get()
        address: str = self.address_entry.get()
        appointment_date: str = self.appointment_date_entry.get()
        report: str = self.report_entry.get()
        if birth_date == "1111-11-11":
            birth_date = ""
        if appointment_date == "1111-11-11":
            appointment_date = ""
        if is_database is True:
            found_patients = db_patient_controller.get_all()
            if full_name:
                found_patients = set(db_patient_controller.get_by_full_name(full_name))
            if birth_date:
                try:
                    found_patients = set(found_patients) & set(
                        db_patient_controller.get_by_birth_date(
                            datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()))
                except ValueError:
                    show_error("Ошибка: Некорректный формат даты. Используйте формат 'YYYY-MM-DD'.")
                    return
            if doctor_full_name:
                found_patients = set(found_patients) & set(db_patient_controller.get_by_doctor_full_name
                                                           (doctor_full_name))
            if address:
                found_patients = set(found_patients) & set(db_patient_controller.get_by_address(address))
            if appointment_date:
                try:
                    found_patients = set(found_patients) & set(db_patient_controller.get_by_date_of_patients_appointment
                                                               (datetime.datetime.strptime(appointment_date,
                                                                                           "%Y-%m-%d").date()))
                except ValueError:
                    show_error("Ошибка: Некорректный формат даты. Используйте формат 'YYYY-MM-DD'.")
                    return
            if report:
                found_patients = set(found_patients) & set(db_patient_controller.get_by_report(report))
        else:
            found_patients = xml_patient_controller.get_all_patients()
            if full_name:
                found_patients = set(xml_patient_controller.search_by_name(full_name))
            if birth_date:
                found_patients = set(found_patients) & set(xml_patient_controller.search_by_birth_date(birth_date))
            if doctor_full_name:
                found_patients = set(found_patients) & set(xml_patient_controller.search_by_doctor_full_name
                                                           (doctor_full_name))
            if address:
                found_patients = set(found_patients) & set(xml_patient_controller.search_by_address(address))
            if appointment_date:
                found_patients = set(found_patients) & set(xml_patient_controller.search_by_date_of_patients_appointment
                                                           (appointment_date))
            if report:
                found_patients = set(found_patients) & set(xml_patient_controller.search_by_report(report))
        found_patients = list(found_patients)
        SearchResultsWindow(self.window, found_patients)


def create_patient_tree(patients):
    new_root = Node("Patients")
    for patient in patients:
        patient_node = Node(str(patient.id), parent=new_root)
        Node(f"id: {patient.id}", parent=patient_node)
        Node(f"full_name: {patient.full_name}", parent=patient_node)
        Node(f"birth_date: {patient.birth_date}", parent=patient_node)
        Node(f"address: {patient.address}", parent=patient_node)
        Node(f"date_of_patients_appointment: {patient.date_of_patients_appointment}", parent=patient_node)
        Node(f"doctor_full_name: {patient.doctor_full_name}", parent=patient_node)
        Node(f"report: {patient.report}", parent=patient_node)
    return new_root


def display_patient_tree(patients):
    patient_tree = create_patient_tree(patients)
    tree_text = ""
    for pre, _, node in RenderTree(patient_tree):
        tree_text += "%s%s\n" % (pre, node.name)
    return tree_text


def show_tree_window():
    global data
    tree_text = display_patient_tree(data)

    tree_window = tk.Toplevel()
    tree_window.title("Patient Tree")

    tree_text_widget = tk.Text(tree_window, wrap="none")
    tree_text_widget.insert(tk.END, tree_text)
    tree_text_widget.pack(fill=tk.BOTH, expand=True)


def show_error(message):
    messagebox.showerror("Ошибка", message)


def save():
    if messagebox.askyesno("Сохранение", "Вы хотите сохранить изменения?"):
        db_patient_controller.save_db()
        xml_patient_controller.save()


def on_exit():
    if messagebox.askyesno("Выход", "Вы хотите выйти из приложения?"):
        root.destroy()


def validate_input(full_name, birth_date_str, doctor_full_name, address, appointment_date_str, report):
    if not full_name.strip():
        show_error("Ошибка: Поле 'full_name' не должно быть пустым.")
        return False

    try:
        datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
    except ValueError:
        show_error("Ошибка: Некорректный формат даты рождения. Используйте формат 'YYYY-MM-DD'.")
        return False

    if not doctor_full_name.strip():
        show_error("Ошибка: Поле 'doctor_full_name' не должно быть пустым.")
        return False
    if not address.strip():
        show_error("Ошибка: Поле 'address' не должно быть пустым.")
        return False
    if not appointment_date_str.strip():
        show_error("Ошибка: Поле 'date_of_patients_appointment' не должно быть пустым.")
        return False
    if not report.strip():
        show_error("Ошибка: Поле 'report' не должно быть пустым.")
        return False

    try:
        datetime.datetime.strptime(appointment_date_str, "%Y-%m-%d")
    except ValueError:
        show_error("Ошибка: Некорректный формат даты приема. Используйте формат 'YYYY-MM-DD'.")
        return False

    return True


def display_patients():
    global current_page, records_per_page, treeview, data

    for row in treeview.get_children():
        treeview.delete(row)

    if is_database:
        data = db_patient_controller.get_all()
    else:
        data = xml_patient_controller.get_all_patients()

    start = (current_page - 1) * records_per_page
    end = start + records_per_page
    for patient in data[start:end]:
        record = (
            patient.id, patient.full_name, patient.birth_date, patient.address, patient.date_of_patients_appointment,
            patient.doctor_full_name, patient.report)
        treeview.insert("", "end", values=record)


def calculate_total_pages():
    global records_per_page, data
    return -(-len(data) // records_per_page)


def prev_page():
    global current_page
    if current_page > 1:
        current_page -= 1
        display_patients()
        update_page_info()


def next_page():
    global current_page
    total_pages = calculate_total_pages()
    if current_page < total_pages:
        current_page += 1
        display_patients()
        update_page_info()


def first_page():
    global current_page
    current_page = 1
    display_patients()
    update_page_info()


def last_page():
    global current_page
    total_pages = calculate_total_pages()
    if current_page != total_pages:
        current_page = total_pages
        display_patients()
        update_page_info()


def change_records_per_page():
    global records_per_page
    try:
        new_records_per_page = int(records_per_page_entry.get())
        if new_records_per_page > 0:
            records_per_page = new_records_per_page
            display_patients()
            update_page_info()
    except ValueError:
        pass


def update_page_info():
    global current_page, records_per_page, treeview
    total_pages_label.config(text="Total Pages: {}".format(calculate_total_pages()))
    current_page_label.config(text="Current Page: {}".format(current_page))
    records_per_page_label.config(text="Records per Page: {}".format(records_per_page))
    total_records_label.config(text="Total Records: {}".format(calculate_total_records()))


def calculate_total_records():
    return len(data)


def set_is_database_true():
    global is_database
    is_database = True
    first_page()


def set_is_database_false():
    global is_database
    is_database = False
    first_page()


def create_patient():
    dialog = tk.Toplevel(root)
    dialog.title("Create Patient")
    dialog.grab_set()

    full_name_label = ttk.Label(dialog, text="Full Name:")
    full_name_label.grid(row=0, column=0, padx=5, pady=5)
    full_name_entry = ttk.Entry(dialog)
    full_name_entry.grid(row=0, column=1, padx=5, pady=5)

    birth_date_label = ttk.Label(dialog, text="Birth Date (YYYY-MM-DD):")
    birth_date_label.grid(row=1, column=0, padx=5, pady=5)
    birth_date_entry = DateEntry(dialog, date_pattern='yyyy-mm-dd')
    birth_date_entry.grid(row=1, column=1, padx=5, pady=5)

    doctor_full_name_label = ttk.Label(dialog, text="Doctor Full Name:")
    doctor_full_name_label.grid(row=2, column=0, padx=5, pady=5)
    doctor_full_name_entry = ttk.Entry(dialog)
    doctor_full_name_entry.grid(row=2, column=1, padx=5, pady=5)

    address_label = ttk.Label(dialog, text="Address:")
    address_label.grid(row=3, column=0, padx=5, pady=5)
    address_entry = ttk.Entry(dialog)
    address_entry.grid(row=3, column=1, padx=5, pady=5)

    appointment_date_label = ttk.Label(dialog, text="Appointment Date (YYYY-MM-DD):")
    appointment_date_label.grid(row=4, column=0, padx=5, pady=5)
    appointment_date_entry = DateEntry(dialog, date_pattern='yyyy-mm-dd')
    appointment_date_entry.grid(row=4, column=1, padx=5, pady=5)

    report_label = ttk.Label(dialog, text="Report:")
    report_label.grid(row=5, column=0, padx=5, pady=5)
    report_entry = ttk.Entry(dialog)
    report_entry.grid(row=5, column=1, padx=5, pady=5)

    def save_patient():
        full_name: str = full_name_entry.get()
        birth_date: str = birth_date_entry.get()
        doctor_full_name: str = doctor_full_name_entry.get()
        address: str = address_entry.get()
        appointment_date: str = appointment_date_entry.get()
        report: str = report_entry.get()

        if validate_input(full_name, birth_date, doctor_full_name, address, appointment_date, report):
            birth_date: datetime.date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
            appointment_date: datetime.date = datetime.datetime.strptime(appointment_date, "%Y-%m-%d").date()
            if is_database is True:
                new_patient = PatientDto(full_name=full_name, birth_date=birth_date, doctor_full_name=doctor_full_name,
                                         address=address, date_of_patients_appointment=appointment_date,
                                         report=report, id=None)
                db_patient_controller.create(new_patient)
            else:
                xml_patient = xml_patient_controller.get_all_patients()[-1]
                new_patient = Patient(full_name=full_name, birth_date=birth_date, doctor_full_name=doctor_full_name,
                                      address=address, date_of_patients_appointment=appointment_date,
                                      report=report, id=int(xml_patient.id) + 1)
                xml_patient_controller.insert(new_patient)
            messagebox.showinfo("Success!", "Patient created successfully.")
            dialog.destroy()
            last_page()

    save_button = ttk.Button(dialog, text="Save Patient", command=save_patient)
    save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


def delete_patients():
    dialog = tk.Toplevel(root)
    dialog.title("Delete Patient")
    dialog.grab_set()

    full_name_label = ttk.Label(dialog, text="Full Name:")
    full_name_label.grid(row=0, column=0, padx=5, pady=5)
    full_name_entry = ttk.Entry(dialog)
    full_name_entry.grid(row=0, column=1, padx=5, pady=5)

    birth_date_label = ttk.Label(dialog, text="Birth Date (YYYY-MM-DD):")
    birth_date_label.grid(row=1, column=0, padx=5, pady=5)
    birth_date_entry = DateEntry(dialog, date_pattern='yyyy-mm-dd')
    birth_date_entry.grid(row=1, column=1, padx=5, pady=5)
    birth_date_entry.set_date(datetime.date(1111, 11, 11))

    doctor_full_name_label = ttk.Label(dialog, text="Doctor Full Name:")
    doctor_full_name_label.grid(row=2, column=0, padx=5, pady=5)
    doctor_full_name_entry = ttk.Entry(dialog)
    doctor_full_name_entry.grid(row=2, column=1, padx=5, pady=5)

    address_label = ttk.Label(dialog, text="Address:")
    address_label.grid(row=3, column=0, padx=5, pady=5)
    address_entry = ttk.Entry(dialog)
    address_entry.grid(row=3, column=1, padx=5, pady=5)

    appointment_date_label = ttk.Label(dialog, text="Appointment Date (YYYY-MM-DD):")
    appointment_date_label.grid(row=4, column=0, padx=5, pady=5)
    appointment_date_entry = DateEntry(dialog, date_pattern='yyyy-mm-dd')
    appointment_date_entry.grid(row=4, column=1, padx=5, pady=5)
    appointment_date_entry.set_date(datetime.date(1111, 11, 11))

    report_label = ttk.Label(dialog, text="Report:")
    report_label.grid(row=5, column=0, padx=5, pady=5)
    report_entry = ttk.Entry(dialog)
    report_entry.grid(row=5, column=1, padx=5, pady=5)

    def delete_patient():
        full_name: str = full_name_entry.get()
        birth_date: str = birth_date_entry.get()
        doctor_full_name: str = doctor_full_name_entry.get()
        address: str = address_entry.get()
        appointment_date: str = appointment_date_entry.get()
        report: str = report_entry.get()
        delete_num: int = 0
        if birth_date == "1111-11-11":
            birth_date = ""
        if appointment_date == "1111-11-11":
            appointment_date = ""
        if is_database is True:
            if full_name:
                delete_num += db_patient_controller.delete_by_full_name(full_name)
            if birth_date:
                delete_num += db_patient_controller.delete_by_birth_date(
                    datetime.datetime.strptime(birth_date, "%Y-%m-%d").date())
            if doctor_full_name:
                delete_num += db_patient_controller.delete_by_doctor_full_name(doctor_full_name)
            if address:
                delete_num += db_patient_controller.delete_by_address(address)
            if appointment_date:
                delete_num += db_patient_controller.delete_by_date_of_patients_appointment(
                    datetime.datetime.strptime(appointment_date, "%Y-%m-%d").date())
            if report:
                delete_num += db_patient_controller.delete_by_report(report)
        else:
            if full_name:
                delete_num += xml_patient_controller.delete_by_name(full_name)
            if birth_date:
                delete_num += xml_patient_controller.delete_by_birth_date(birth_date)
            if doctor_full_name:
                delete_num += xml_patient_controller.delete_by_doctor_full_name(doctor_full_name)
            if address:
                delete_num += xml_patient_controller.delete_by_address(address)
            if appointment_date:
                delete_num += xml_patient_controller.delete_by_date_of_patients_appointment(appointment_date)
            if report:
                delete_num += xml_patient_controller.delete_by_report(report)
        messagebox.showinfo("Success!", "Deleted patients: " + str(delete_num))
        dialog.destroy()
        first_page()

    delete = ttk.Button(dialog, text="Delete Patient", command=delete_patient)
    delete.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


root = tk.Tk()
root.title("Hospital App")
root.geometry('1470x720')
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open a db file", command=set_is_database_true)
file_menu.add_command(label="Open an XML file", command=set_is_database_false)
file_menu.add_command(label="Save file", command=save)
file_menu.add_command(label="Exit", command=on_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Find", command=lambda: SearchWindow(root))
view_menu.add_command(label="Tree", command=lambda: show_tree_window())
menu_bar.add_cascade(label="View", menu=view_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Create", command=create_patient)
edit_menu.add_command(label="Delete", command=delete_patients)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

create_button = ttk.Button(toolbar, text="Create Patient", command=create_patient)
create_button.pack(side=tk.LEFT, padx=2, pady=2)
delete_button = ttk.Button(toolbar, text="Delete Patient", command=delete_patients)
delete_button.pack(side=tk.LEFT)

root.config(menu=menu_bar)

info_frame = tk.Frame(root)
info_frame.pack()

navigation_frame = tk.Frame(root)
navigation_frame.pack()

columns = ("ID", "Full Name", "Birth Date", "Address", "Doctor Full Name", "Appointment Date", "Report")

current_page = 1
records_per_page = 10

prev_button = tk.Button(navigation_frame, text="Previous", command=prev_page)
prev_button.pack(side=tk.LEFT)

next_button = tk.Button(navigation_frame, text="Next", command=next_page)
next_button.pack(side=tk.LEFT)

first_button = tk.Button(navigation_frame, text="First", command=first_page)
first_button.pack(side=tk.LEFT)

last_button = tk.Button(navigation_frame, text="Last", command=last_page)
last_button.pack(side=tk.LEFT)

total_records_label = tk.Label(info_frame, text="Total Records: {}".format(calculate_total_records()))
total_records_label.pack()

total_pages_label = tk.Label(info_frame, text="Total Pages: {}".format(calculate_total_pages()))
total_pages_label.pack()

current_page_label = tk.Label(info_frame, text="Current Page: {}".format(current_page))
current_page_label.pack()

records_per_page_label = tk.Label(info_frame, text="Records per Page: {}".format(records_per_page))
records_per_page_label.pack()

records_per_page_entry = tk.Entry(info_frame)
records_per_page_entry.pack(side=tk.LEFT)
records_per_page_entry.insert(0, "10")

change_records_per_page_button = tk.Button(info_frame, text="Change", command=change_records_per_page)
change_records_per_page_button.pack(side=tk.LEFT)

treeview = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, anchor="center")
treeview.pack()

display_patients()

root.mainloop()
