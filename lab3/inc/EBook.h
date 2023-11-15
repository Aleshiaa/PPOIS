#pragma once
#include <./inc/Book.h>
#include <./inc/User.h>
/**
* @brief Class EBook
* 
*/
class EBook : public Book {
public:
    /**
    * @brief Constructor
    * @param title Title 
    * @param author Author
    * @param publication_date Date of publication
    * @param ISBN International Standard Book Number
    * @param genre Genre
    * @param file_size Size of ebook file
    * @param download_link Link to download ebook
    * 
    */
    EBook(const std::string& title, const std::string& author, const std::string& publication_date, const std::string& ISBN, const std::string& genre, int file_size, const std::string& download_link);
    /**
    * @brief Destructor
    */
    ~EBook();
    /**
    * @brief Open ebook
    */
    void CheckOut(User* user) override;
    void Return(User* user) override;
    std::string GetItemInfo() const override;
    bool IsAvailable() const override;
    void Open();
private:
    int file_size;
    std::string download_link;
};