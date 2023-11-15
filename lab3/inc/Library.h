#pragma once
#include <./inc/LibraryItem.h>
#include <./inc/User.h>
/**
* @brief Class Library
* 
*/
class Library {
public:
    /**
    * @brief Constructor
    * 
    */
    Library();
    /**
    * @brief Destructor
    * 
    */
    ~Library();
    /**
    * @brief Register user
    * @param user User
    */
    void RegisterUser(User* user);
    /**
    * @brief User autentification
    * @param email Email
    * @param password Password
    */
    User* AuthenticateUser(const std::string& email, const std::string& password);
    /**
    * @brief Item search
    * @param title Title
    */
    LibraryItem* FindItem(const std::string& title);
    std::vector<User*> users;
    std::vector<LibraryItem*> items;
};

