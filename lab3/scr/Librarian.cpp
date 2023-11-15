#include <./inc/Librarian.h>
// Implement Librarian

Librarian::Librarian(const std::string& name, const std::string& email, const std::string& password, int employee_id)
    : User(name, email, password), employee_id(employee_id) {}

Librarian::~Librarian() {}

void Librarian::AddItemToLibrary(LibraryItem* item) {
    // Логика добавления элемента в базу данных библиотеки
    // Например, добавление элемента в вектор items, представляющий базу данных библиотеки
    items.push_back(item);
}

void Librarian::RemoveItemFromLibrary(LibraryItem* item) {
    // Логика удаления элемента из базы данных библиотеки
    // Например, поиск элемента в векторе items и его удаление
    auto it = std::find(items.begin(), items.end(), item);
    if (it != items.end()) {
        items.erase(it);
    }
}