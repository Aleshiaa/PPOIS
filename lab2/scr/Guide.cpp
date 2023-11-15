#include <.\inc\Guide.h>

Guide::Guide(const std::string& firstName, const std::string& lastName, int age, char gender, int employeeId, const std::string& position, double salary, const std::string& license)
    : Employee(firstName, lastName, age, gender, employeeId, position, salary), license(license) {
}

void Guide::ConductTour() {
    std::cout << "Проведение экскурсии для " << firstName << " " << lastName << std::endl;
}

void Guide::ProvideInformation() {
    std::cout << "Предоставление информации для " << firstName << " " << lastName << std::endl;
}