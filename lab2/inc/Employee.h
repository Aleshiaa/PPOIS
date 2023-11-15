#pragma once
#include <.\inc\Person.h>
/**
 * @brief Класс Работник
 * 
 */
class Employee : public Person {
public:
    /**
     * @brief Конструктор работника
     * @param firstName имя
     * @param lastName фамилия
     * @param age возраст
     * @param gender пол
     * @param employeeId личный номер ID
     * @param position должность
     * @param salary заработная плата
     * 
     */
    Employee(const std::string& firstName, const std::string& lastName, int age, char gender, int employeeId, const std::string& position, double salary);

    /**
    * @brief управление личными данными
    * 
    */
    void ManagePersonalInfo();
    /**
    * @brief создание отчета сотрудником
    * 
    */
    void WorkReport();
    int employeeId;
    std::string position;
    double salary;
};