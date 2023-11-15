#include <./inc/OnlineLibraryItem.h>
// Implement OnlineLibraryItem

OnlineLibraryItem::OnlineLibraryItem(const std::string& title, const std::string& author, const std::string& publication_date, const std::string& url, const std::string& file_format)
    : LibraryItem(title, author, publication_date), url(url), file_format(file_format) {}

OnlineLibraryItem::~OnlineLibraryItem() {}

void OnlineLibraryItem::Download() {
    std::cout << "Downloading " + title + " from " + url + " in " + file_format + " format." << std::endl;
}