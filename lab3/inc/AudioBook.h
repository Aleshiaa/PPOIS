#pragma once
#include <./inc/Book.h>
#include <./inc/User.h>
/**
* @brief Class AudioBook
* 
*/
class AudioBook : public Book {
public:
    /**
    * @brief Constructor
    * @param title Title 
    * @param author Author
    * @param publication_date Date of publication
    * @param ISBN International Standard Book Number
    * @param genre Genre
    * @param narrator Narrator of audiobook
    * @param duration Duration of audiobook
    * 
    */
    AudioBook(const std::string& title, const std::string& author, const std::string& publication_date, const std::string& ISBN, const std::string& genre, const std::string& narrator, int duration);
    /**
    * @brief Destructor
    */
    ~AudioBook();
    /**
    * @brief Play audiobook
    * 
    */
    void CheckOut(User* user) override;
    void Return(User* user) override;
    std::string GetItemInfo() const override;
    bool IsAvailable() const override;
    void Play();
private:
    std::string narrator;
    int duration;
};