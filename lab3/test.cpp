#include <gtest/gtest.h>
#include "library.h"


TEST(LibraryItemTest, CheckOut) {
    LibraryItem item("Sample Title", "Sample Author", "2023-01-01");
    EXPECT_TRUE(item.IsAvailable());
    User user("User Name", "user@example.com", "password");
    item.CheckOut(&user);
    EXPECT_FALSE(item.IsAvailable());
}

TEST(LibraryItemTest, Return) {
    LibraryItem item("Sample Title", "Sample Author", "2023-01-01");
    User user("User Name", "user@example.com", "password");
    item.CheckOut(&user);
    item.Return(&user);
    EXPECT_TRUE(item.IsAvailable());
}

TEST(UserTest, BorrowItem) {
    LibraryItem item("Sample Title", "Sample Author", "2023-01-01");
    User user("User Name", "user@example.com", "password");
    user.BorrowItem(&item);
    EXPECT_EQ(user.GetBorrowedItems().size(), 1);
}

TEST(UserTest, ReturnItem) {
    LibraryItem item("Sample Title", "Sample Author", "2023-01-01");
    User user("User Name", "user@example.com", "password");
    user.BorrowItem(&item);
    user.ReturnItem(&item);
    EXPECT_EQ(user.GetBorrowedItems().size(), 0);
}

TEST(LibraryTest, RegisterUser) {
    Library library;

    User user("User Name", "user@example.com", "password");
    library.RegisterUser(&user);

    User* authenticatedUser = library.AuthenticateUser("user@example.com", "password");
    EXPECT_EQ(authenticatedUser, &user);
}


TEST(BookTest, GetAuthors) {
    Book book("Sample Book", "Sample Author", "2023-01-01", "1234567890", "Sample Genre");
    EXPECT_EQ(book.GetAuthors(), "Sample Author");
}


TEST(MagazineTest, GetIssueNumber) {
    Magazine magazine("Sample Magazine", "Sample Author", "2023-01-01", 42);
    EXPECT_EQ(magazine.GetIssueNumber(), 42);
}


TEST(TransactionTest, GetTransactionDetails) {
    User user("User Name", "user@example.com", "password");
    LibraryItem item("Sample Item", "Sample Author", "2023-01-01");
    Transaction transaction(&user, &item, "2023-01-15");

    std::string transactionDetails = transaction.GetTransactionDetails();
    EXPECT_EQ(transactionDetails, "Transaction Date: 2023-01-15, User: User Name, Item: Title: Sample Item, Author: Sample Author, Publication Date: 2023-01-01");
}


TEST(OnlineLibraryItemTest, Download) {
    OnlineLibraryItem onlineItem("Sample Online Item", "Sample Author", "2023-01-01", "http://sample.com", "PDF");

    testing::internal::CaptureStdout();
    onlineItem.Download();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Downloading Sample Online Item from http://sample.com in PDF format.\n");
}


TEST(AudioBookTest, Play) {
    AudioBook audioBook("Sample AudioBook", "Sample Author", "2023-01-01", "1234567890", "Sample Genre", "Sample Narrator", 120);

    testing::internal::CaptureStdout();
    audioBook.Play();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Playing Sample AudioBook narrated by Sample Narrator (Duration: 120 minutes).\n");
}


TEST(EBookTest, Open) {
    EBook eBook("Sample EBook", "Sample Author", "2023-01-01", "1234567890", "Sample Genre", 512, "http://ebook.com/sample");

    testing::internal::CaptureStdout();
    eBook.Open();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Opening Sample EBook (File Size: 512KB) from http://ebook.com/sample\n");
}

TEST(BookTest, CheckOut) {
    Book book("The Catcher in the Rye", "J.D. Salinger", "1951", "123456789", "Fiction");
    User user("Alice", "alice@example.com", "password");
    book.CheckOut(&user);
    EXPECT_FALSE(book.IsAvailable());
}

TEST(EBookTest, CheckOut) {
    EBook ebook("The Great Gatsby", "F. Scott Fitzgerald", "1925", "987654321", "Classic", 500, "http://example.com/ebook");
    User user("Bob", "bob@example.com", "password");
    ebook.CheckOut(&user);
    EXPECT_FALSE(ebook.IsAvailable());
}

TEST(AudioBookTest, CheckOut) {
    AudioBook audiobook("To Kill a Mockingbird", "Harper Lee", "1960", "567890123", "Drama", "Narrator Name", 360);
    User user("Charlie", "charlie@example.com", "password");
    audiobook.CheckOut(&user);
    EXPECT_FALSE(audiobook.IsAvailable());
}

TEST(BookTest, Return) {
    Book book("The Catcher in the Rye", "J.D. Salinger", "1951", "123456789", "Fiction");
    User user("Alice", "alice@example.com", "password");
    book.CheckOut(&user);
    book.Return(&user);
    EXPECT_TRUE(book.IsAvailable());
}

TEST(EBookTest, Return) {
    EBook ebook("The Great Gatsby", "F. Scott Fitzgerald", "1925", "987654321", "Classic", 500, "http://example.com/ebook");
    User user("Bob", "bob@example.com", "password");
    ebook.CheckOut(&user);
    ebook.Return(&user);
    EXPECT_TRUE(ebook.IsAvailable());
}

TEST(AudioBookTest, Return) {
    AudioBook audiobook("To Kill a Mockingbird", "Harper Lee", "1960", "567890123", "Drama", "Narrator Name", 360);
    User user("Charlie", "charlie@example.com", "password");
    audiobook.CheckOut(&user);
    audiobook.Return(&user);
    EXPECT_TRUE(audiobook.IsAvailable());
}

int main(int argc, char** argv) {
    std::locale::global(std::locale("en_US.UTF-8"));
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}