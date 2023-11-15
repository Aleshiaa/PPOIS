#pragma once
#include <./inc/LibraryItem.h>
/**
* @brief Class Magazine
* 
*/
class Magazine : public LibraryItem {
public:
    /**
    * @brief Constructor
    * @param title Title 
    * @param author Author
    * @param publication_date Date of publication
    * @param issue_number Issue number
    * 
    */
    Magazine(const std::string& title, const std::string& author, const std::string& publication_date, int issue_number);
    /**
    * @brief Destructor
    * 
    */
    virtual ~Magazine();

    int GetIssueNumber() const;

private:
    int issue_number;
};