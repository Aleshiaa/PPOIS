#pragma once
#include <string>
#include <vector>
#include <iostream>

class User;
/**
* @brief Class Item
* 
*/
class LibraryItem {
public:
    /**
    * @brief Constuctor
    * @param title Title 
    * @param author Author
    * @param publication_date Date of publication
    */
    LibraryItem(const std::string& title, const std::string& author, const std::string& publication_date);
    /**
    * @brief Destructor
    * 
    */
    virtual ~LibraryItem();

    /**
    * @brief Check out
    * @param user User
    * 
    */
    virtual void CheckOut(User* user);
    /**
    * @brief Return
    * @param user User
    * 
    */
    virtual void Return(User* user);
    /**
    * @brief Get item info
    * 
    */
    virtual std::string GetItemInfo() const;
    /**
    * @brief Check if its available
    * 
    */
    virtual bool IsAvailable() const;
    std::string title;
    std::string author;
    std::string publication_date;
    bool is_available;
};
