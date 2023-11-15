#pragma once
#include <string>
#include <vector>
#include <.\inc\Exponat.h>
#include <.\inc\Exhibition.h>
/**
 * @brief Класс Зал
 * 
 */
class MuseumHall {
public:
    /**
     * @brief Конструктор зала
     * @param name название зала
     * @param description описание зала
     * 
     */
    MuseumHall(const std::string& name, const std::string& description);
    std::string GetName() const;
    std::string GetDescription() const;
    std::string name;
    std::string description;
    std::vector<Exponat> exponats;
    Exhibition currentExhibition;
};