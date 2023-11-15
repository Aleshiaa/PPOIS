#include <./inc/Magazine.h>
// Implement Magazine

Magazine::Magazine(const std::string& title, const std::string& author, const std::string& publication_date, int issue_number)
    : LibraryItem(title, author, publication_date), issue_number(issue_number) {}

Magazine::~Magazine() {}

int Magazine::GetIssueNumber() const {
    return issue_number;
}