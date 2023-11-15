#include<.\inc\Museum.h>

Museum::Museum(const std::string& name, const std::string& address, const std::string& hours)
    : name(name), address(address), hours(hours), financeDept(1000000.0) {
    }

void Museum::ManageMuseumInfo() {
    std::cout << "Управление информацией о музее " << name << std::endl;
    }

void Museum::OrganizeExhibition(const Exhibition& exhibition) {
    exhibitions.push_back(exhibition);
    }

void Museum::ManageHalls() {
    std::cout << "Управление залами музея " << name << std::endl;
    }