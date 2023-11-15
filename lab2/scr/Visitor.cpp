#include<.\inc\Visitor.h>

Visitor::Visitor(const std::string& firstName, const std::string& lastName, int age, char gender, int ticketNumber, const std::string& visitDate)
    : Person(firstName, lastName, age, gender), ticketNumber(ticketNumber), visitDate(visitDate) {
}
    
void Visitor::PurchaseTicket() {
    std::cout << "Покупка билета для " << firstName << " " << lastName << std::endl;
}

void Visitor::RateMuseum() {
    std::cout << "Оценка музея посетителем " << firstName << " " << lastName << std::endl;
}