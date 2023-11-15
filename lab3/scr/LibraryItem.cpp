#include <./inc/LibraryItem.h>
#include <./inc/User.h>
// Implement LibraryItem

LibraryItem::LibraryItem(const std::string& title, const std::string& author, const std::string& publication_date)
    : title(title), author(author), publication_date(publication_date), is_available(true) {}

LibraryItem::~LibraryItem() {}

void LibraryItem::CheckOut(User* user) {
    if (is_available) {
        is_available = false;
        user->BorrowItem(this);
    } else {
        std::cout << "This item is not available for checkout." << std::endl;
    }
}

void LibraryItem::Return(User* user) {
    if (!is_available) {
        is_available = true;
        user->ReturnItem(this);
    } else {
        std::cout << "This item is already available." << std::endl;
    }
}
std::string LibraryItem::GetItemInfo() const {
    return "Title: " + title + ", Author: " + author + ", Publication Date: " + publication_date;
}

bool LibraryItem::IsAvailable() const {
    return is_available;
}
