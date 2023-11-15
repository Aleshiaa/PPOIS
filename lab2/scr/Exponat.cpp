#include <.\inc\Exponat.h>

Exponat::Exponat(int id, const std::string& name, const std::string& description, const std::string& author)
    : id(id), name(name), description(description), author(author) {
}

int Exponat::GetID() const {
    return id;
}

std::string Exponat::GetName() const {
    return name;
}

std::string Exponat::GetDescription() const {
    return description;
}

std::string Exponat::GetAuthor() const {
    return author;
}