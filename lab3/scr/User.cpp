#include <./inc/User.h>
#include <./inc/LibraryItem.h>
// Implement User

User::User(const std::string& name, const std::string& email, const std::string& password)
    : name(name), email(email), password(password) {}

User::~User() {}

void User::BorrowItem(LibraryItem* item) {
    borrowed_items.push_back(item);
}

void User::ReturnItem(LibraryItem* item) {
    for (auto it = borrowed_items.begin(); it != borrowed_items.end(); ++it) {
        if (*it == item) {
            borrowed_items.erase(it);
            break;
        }
    }
}