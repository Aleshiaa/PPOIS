#include <./inc/Library.h>

// Implement Library

Library::Library() {}

Library::~Library() {}

void Library::RegisterUser(User* user) {
    users.push_back(user);
}

User* Library::AuthenticateUser(const std::string& email, const std::string& password) {
    for (User* user : users) {
        if (user->email == email && user->password == password) {
            return user;
        }
    }
    return nullptr;
}

LibraryItem* Library::FindItem(const std::string& title) {
    for (LibraryItem* item : items) {
        if (item->title == title) {
            return item;
        }
    }
    return nullptr;
}