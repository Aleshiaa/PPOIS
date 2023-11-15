#pragma once
#include <string>
#include <vector>
#include <iostream>

class LibraryItem;
/**
* @brief Class User
* 
*/
class User {
public:
    /**
    * @brief Constructor
    * @param name Name
    * @param email Email
    * @param password Password
    * 
    */
    User(const std::string& name, const std::string& email, const std::string& password);
    /**
    * @brief Destructor
    */
    virtual ~User();

    /**
    * @brief Borrow item
    * @param item Item
    * 
    */
    virtual void BorrowItem(LibraryItem* item);
    /**
    * @brief Return item
    * @param item Item
    * 
    */
    virtual void ReturnItem(LibraryItem* item);

    /**
    * @brief Get borrowed items
    * 
    */
    const std::vector<LibraryItem*>& GetBorrowedItems() const {
        return borrowed_items;
    }
    std::string name;
    std::string email;
    std::string password;
    std::vector<LibraryItem*> borrowed_items;
};