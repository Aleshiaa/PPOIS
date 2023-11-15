#pragma once
#include <./inc/User.h>
/**
* @brief Class Librarian
* 
*/
class Librarian : public User {
public:
    /**
    * @brief Constructor
    * @param name Name
    * @param email Email
    * @param password Password
    * @param employee_id Employee ID
    */
    Librarian(const std::string& name, const std::string& email, const std::string& password, int employee_id);
    /**
    * @brief Destructor
    */
    virtual ~Librarian();

    /**
    * @brief Add itemm to library
    * @param item Item
    * 
    */
    void AddItemToLibrary(LibraryItem* item);
    /**
    * @brief Remove item from  library
    * @param item Item
    * 
    */
    void RemoveItemFromLibrary(LibraryItem* item);

private:
    int employee_id;
    std::vector<LibraryItem*> items; // Вектор для хранения элементов библиотеки
};
