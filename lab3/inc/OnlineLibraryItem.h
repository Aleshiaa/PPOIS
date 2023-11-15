#pragma once
#include <./inc/LibraryItem.h>
/**
* @brief Class Online item
*/
class OnlineLibraryItem : public LibraryItem {
public:
    /**
    * @brief Constructor
    * @param title Title 
    * @param author Author
    * @param publication_date Date of publication
    * @param url URL
    * @param file_format Format of file
    * 
    */
    OnlineLibraryItem(const std::string& title, const std::string& author, const std::string& publication_date, const std::string& url, const std::string& file_format);
    /**
    * @brief Destructor
    * 
    */
    ~OnlineLibraryItem();
    /**
    * @brief Download online item
    * 
    */
    void Download();
private:
    std::string url;
    std::string file_format;
};