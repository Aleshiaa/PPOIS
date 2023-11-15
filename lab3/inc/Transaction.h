#pragma once
#include <./inc/LibraryItem.h>
#include <./inc/User.h>
/**
* @brief Class Transaction
* 
*/
class Transaction {
public:
    /**
    * @brief Constructor
    * @param user User
    * @param item Item
    * @param transaction_date date of transaction
    * 
    */
    Transaction(User* user, LibraryItem* item, const std::string& transaction_date);
    /**
    * @brief Destructor
    * 
    */
    ~Transaction();

    std::string GetTransactionDetails() const;
private:
    User* user;
    LibraryItem* item;
    std::string transaction_date;
};
