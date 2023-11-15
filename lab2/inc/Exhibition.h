#pragma once
#include <string>
/**
 * @brief Класс Выставка
 * 
 */
class Exhibition {
public:
Exhibition::Exhibition() : name(""), startDate(""), endDate("") {
}
    /**
     * @brief Конструктор выставки
     * @param id название выставки
     * @param startDate дата начала выставки
     * @param endDate дата конца выставки
     * 
     */
    Exhibition(const std::string& name, const std::string& startDate, const std::string& endDate);
    std::string GetName() const;
    std::string GetStartDate() const;
    std::string GetEndDate() const;
    std::string name;
    std::string startDate;
    std::string endDate;
};