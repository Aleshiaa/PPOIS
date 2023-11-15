#pragma once
#include <.\inc\Person.h>
/**
 * @brief Класс Посетитель
 * 
 */
class Visitor : public Person {
public:
    /**
     * @brief Конструктор посетителя
     * @param firstName имя
     * @param lastName фамилия
     * @param age возраст
     * @param gender пол
     * @param ticketNumber номер входного билета
     * @param visitDate дата визита
     * 
     */
    Visitor::Visitor(const std::string& firstName, const std::string& lastName, int age, char gender, int ticketNumber, const std::string& visitDate);
    /**
    * @brief покупка билета
    * 
    */
    void Visitor::PurchaseTicket();
    /**
    * @brief оценка музея
    * 
    */
    void Visitor::RateMuseum();
    int ticketNumber;
    std::string visitDate;
};
