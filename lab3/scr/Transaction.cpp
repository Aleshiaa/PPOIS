#include <./inc/Transaction.h>
// Implement Transaction

Transaction::Transaction(User* user, LibraryItem* item, const std::string& transaction_date)
    : user(user), item(item), transaction_date(transaction_date) {}

Transaction::~Transaction() {}

std::string Transaction::GetTransactionDetails() const {
    return "Transaction Date: " + transaction_date + ", User: " + user->name + ", Item: " + item->GetItemInfo();
}