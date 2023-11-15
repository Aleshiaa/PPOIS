#include<.\inc\MuseumHall.h>

MuseumHall::MuseumHall(const std::string& name, const std::string& description)
    : name(name), description(description) {
}

std::string MuseumHall::GetName() const {
    return name;
}

std::string MuseumHall::GetDescription() const {
    return description;
}