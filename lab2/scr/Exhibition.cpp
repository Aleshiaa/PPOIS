#include <.\inc\Exhibition.h>
Exhibition::Exhibition(const std::string& name, const std::string& startDate, const std::string& endDate)
    : name(name), startDate(startDate), endDate(endDate) {
}

std::string Exhibition::GetName() const {
    return name;
}

std::string Exhibition::GetStartDate() const {
    return startDate;
}

std::string Exhibition::GetEndDate() const {
    return endDate;
}