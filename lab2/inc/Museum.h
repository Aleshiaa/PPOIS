#pragma once
#include <string>
#include <vector>
#include <./inc/FinancialDepartment.h>
#include <./inc/MuseumHall.h>
/**
 * @brief Класс Музей
 * 
 */
class Museum {
public:
    /**
     * @brief Конструктор музея
     * @param name название музея
     * @param address адрес музея
     * @param hours время работы
     * 
     */
   Museum::Museum(const std::string& name, const std::string& address, const std::string& hours);
    /**
    * @brief управление информацией о музее
    * 
    */
    void Museum::ManageMuseumInfo();
    /**
    * @brief организация выставки
    * @param выставка
    */
    void Museum::OrganizeExhibition(const Exhibition& exhibition);
    /**
    * @brief управление выставочными залами
    * 
    */
    void Museum::ManageHalls();
    std::string name;
    std::string address;
    std::string hours;
    FinancialDepartment financeDept;
    std::vector<MuseumHall> halls;
    std::vector<Exhibition> exhibitions;
};