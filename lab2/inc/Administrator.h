#pragma once
#include <.\inc\Employee.h>
/**
 * @brief Класс Администратор
 * 
 */
class Administrator : public Employee {
public:
    /**
     * @brief Конструктор администратора
     * @param firstName имя
     * @param lastName фамилия
     * @param age возраст
     * @param gender пол
     * @param employeeId личный номер ID
     * @param position должность
     * @param salary заработная плата
     * @param accessLevel уровень доступа
     * 
     */
    Administrator::Administrator(const std::string& firstName, const std::string& lastName, int age, char gender, int employeeId, const std::string& position, double salary, int accessLevel);
    /**
    * @brief управление административными функциями
    * 
    */
    void Administrator::ManageAdminFunctions();
    int accessLevel;
};