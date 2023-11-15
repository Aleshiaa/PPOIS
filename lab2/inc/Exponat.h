#pragma once
#include <string>
/**
 * @brief Класс Экспонат
 * 
 */
class Exponat {
public:
    /**
     * @brief Конструктор экспоната
     * @param id идентификационный номер билета
     * @param price стоимость входного билета
     * @param type тип билета
     * 
     */
    Exponat(int id, const std::string& name, const std::string& description, const std::string& author);

    // Геттеры
    int GetID() const;
    std::string GetName() const;
    std::string GetDescription() const;
    std::string GetAuthor() const;
    int id;
    std::string name;
    std::string description;
    std::string author;
};