#pragma once
#include <./inc/LibraryItem.h>
#include <./inc/User.h>
/**
* @brief Class book
* 
*/
class Book : public LibraryItem {
public:
    /**
    * @brief Constructor
    * @param title Title 
    * @param author Author
    * @param publication_date Date of publication
    * @param ISBN International Standard Book Number
    * @param genre Genre
    * 
    */
    Book(const std::string& title, const std::string& author, const std::string& publication_date, const std::string& ISBN, const std::string& genre);
    /**
    * @brief Destructor
    * 
    */
    virtual ~Book();
    
    void CheckOut(User* user) override;
    void Return(User* user) override;
    std::string GetItemInfo() const override;
    bool IsAvailable() const override;
    std::string GetAuthors() const;

private:
    std::string ISBN;
    std::string genre;
};