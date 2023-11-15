#pragma once
#include <string>
/**
 * @brief Класс Билет
 * 
 */
class Ticket {
public:
    /**
     * @brief Конструктор входного билета
     * @param id идентификационный номер билета
     * @param price стоимость входного билета
     * @param type тип билета
     * 
     */
    Ticket(int id, double price, const std::string& type);
    int GetID() const;
    double GetPrice() const;
    std::string GetType() const;
    int id;
    double price;
    std::string type;
};