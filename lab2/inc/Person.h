#pragma once
#include ".\inc\Museum.h"
#include <iostream>
/**
 * @brief Класс Человек
 * 
 */
class Person {
public:
    /**
     * @brief Конструктор человека
     * @param firstName имя
     * @param lastName фамилия
     * @param age возраст
     * @param gender пол
     */
    Person::Person(const std::string& firstName, const std::string& lastName, int age, char gender);

    /**
    * @brief Аутентификация человека
    * 
    */
    void Person::Authenticate();
    /**
    * @brief Обновление личной информации
    * 
    */
    void Person::UpdatePersonalInfo();
    /**
    * @brief имя человека
    * 
    */
    std::string firstName;
    /**
    * @brief фамилия человека
    * 
    */
    std::string lastName;
    int age;
    char gender;
};
