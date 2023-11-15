#include <./inc/AudioBook.h>
// Implement AudioBook

AudioBook::AudioBook(const std::string& title, const std::string& author, const std::string& publication_date, const std::string& ISBN, const std::string& genre, const std::string& narrator, int duration)
    : Book(title, author, publication_date, ISBN, genre), narrator(narrator), duration(duration) {}

AudioBook::~AudioBook() {}

void AudioBook::Play() {
    std::cout << "Playing " + title + " narrated by " + narrator + " (Duration: " << duration << " minutes)." << std::endl;
}

// Реализации для AudioBook

void AudioBook::CheckOut(User* user) {
    Book::CheckOut(user);
    std::cout << "Аудиокнига " << title << " взята в аренду пользователем " << user->name << std::endl;
}

void AudioBook::Return(User* user) {
    Book::Return(user);
    std::cout << "Аудиокнига " << title << " возвращена пользователем " << user->name << std::endl;
}

std::string AudioBook::GetItemInfo() const {
    return "Информация об аудиокниге: " + title + ", Автор: " + author + ", Дата публикации: " + publication_date;
}

bool AudioBook::IsAvailable() const {
    return LibraryItem::IsAvailable();
}