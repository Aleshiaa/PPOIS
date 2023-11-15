#pragma once
#include <.\inc\Employee.h>
/**
 * @brief Класс Гид
 * 
 */
class Guide : public Employee {
public:
    /**
     * @brief Конструктор гида
     * @param firstName имя
     * @param lastName фамилия
     * @param age возраст
     * @param gender пол
     * @param employeeId личный номер ID
     * @param position должность
     * @param salary заработная плата
     * @param license лицензия
     * 
     */
    Guide(const std::string& firstName, const std::string& lastName, int age, char gender, int employeeId, const std::string& position, double salary, const std::string& license);

    /**
    * @brief проведение экскурсии
    * 
    */
    void ConductTour();
    /**
    * @brief предоставление информации
    * 
    */
    void ProvideInformation();
    std::string license;
};
