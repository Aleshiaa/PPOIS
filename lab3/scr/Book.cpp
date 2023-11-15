#include <./inc/Book.h>
// Implement Book

Book::Book(const std::string& title, const std::string& author, const std::string& publication_date, const std::string& ISBN, const std::string& genre)
    : LibraryItem(title, author, publication_date), ISBN(ISBN), genre(genre) {}

Book::~Book() {}

std::string Book::GetAuthors() const {
    return author;
}

void Book::CheckOut(User* user) {
    LibraryItem::CheckOut(user);
    std::cout << "Книга " << title << " взята в аренду пользователем " << user->name << std::endl;
}

void Book::Return(User* user) {
    LibraryItem::Return(user);
    std::cout << "Книга " << title << " возвращена пользователем " << user->name << std::endl;
}

std::string Book::GetItemInfo() const {
    return "Информация о книге: " + title + ", Автор: " + author + ", Дата публикации: " + publication_date;
}

bool Book::IsAvailable() const {
    return LibraryItem::IsAvailable();
}