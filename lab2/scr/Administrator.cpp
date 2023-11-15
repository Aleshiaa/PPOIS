#include <.\inc\Administrator.h>
Administrator::Administrator(const std::string& firstName, const std::string& lastName, int age, char gender, int employeeId, const std::string& position, double salary, int accessLevel)
    : Employee(firstName, lastName, age, gender, employeeId, position, salary), accessLevel(accessLevel) {
}

void Administrator::ManageAdminFunctions() {
    std::cout << "Управление административными функциями музея для " << firstName << " " << lastName << std::endl;
}