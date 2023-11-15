#include <./inc/EBook.h>
// Implement EBook

EBook::EBook(const std::string& title, const std::string& author, const std::string& publication_date, const std::string& ISBN, const std::string& genre, int file_size, const std::string& download_link)
    : Book(title, author, publication_date, ISBN, genre), file_size(file_size), download_link(download_link) {}

EBook::~EBook() {}

void EBook::Open() {
    std::cout << "Opening " + title + " (File Size: " << file_size << "KB) from " + download_link << std::endl;
}

// Реализации для EBook

void EBook::CheckOut(User* user) {
    Book::CheckOut(user);
    std::cout << "Электронная книга " << title << " взята в аренду пользователем " << user->name << std::endl;
}

void EBook::Return(User* user) {
    Book::Return(user);
    std::cout << "Электронная книга " << title << " возвращена пользователем " << user->name << std::endl;
}

std::string EBook::GetItemInfo() const {
    return "Информация об электронной книге: " + title + ", Автор: " + author + ", Дата публикации: " + publication_date;
}

bool EBook::IsAvailable() const {
    return LibraryItem::IsAvailable();
}
