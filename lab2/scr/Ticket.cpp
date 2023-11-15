#include<.\inc\Ticket.h>

Ticket::Ticket(int id, double price, const std::string& type)
    : id(id), price(price), type(type) {
}

int Ticket::GetID() const {
    return id;
}

double Ticket::GetPrice() const {
    return price;
}

std::string Ticket::GetType() const {
    return type;
}