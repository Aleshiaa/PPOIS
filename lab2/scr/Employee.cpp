#include <.\inc\Employee.h>
Employee::Employee(const std::string& firstName, const std::string& lastName, int age, char gender, int employeeId, const std::string& position, double salary)
    : Person(firstName, lastName, age, gender), employeeId(employeeId), position(position), salary(salary) {
}

void Employee::ManagePersonalInfo() {
    std::cout << "Управление личными данными сотрудника " << firstName << " " << lastName << std::endl;
}

void Employee::WorkReport() {
    std::cout << "Создание отчета о работе для сотрудника " << firstName << " " << lastName << std::endl;
}