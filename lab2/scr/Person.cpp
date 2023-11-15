#include<.\inc\Person.h>

Person::Person(const std::string& firstName, const std::string& lastName, int age, char gender)
        : firstName(firstName), lastName(lastName), age(age), gender(gender) {
    }

void Person::Authenticate() {
    std::cout << "Аутентификация пользователя " << firstName << " " << lastName << std::endl;
    }

void Person::UpdatePersonalInfo() {
    std::cout << "Обновление личных данных для " << firstName << " " << lastName << std::endl;
    }