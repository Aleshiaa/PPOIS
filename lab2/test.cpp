#include <gtest/gtest.h>
#include <.\inc\Administrator.h>
#include <.\inc\Employee.h>
#include <.\inc\Exhibition.h>
#include <.\inc\Exponat.h>
#include <.\inc\FinancialDepartment.h>
#include <.\inc\Guide.h>
#include<.\inc\Museum.h>
#include<.\inc\MuseumHall.h>
#include<.\inc\Person.h>
#include<.\inc\Ticket.h>
#include<.\inc\Visitor.h>

TEST(PersonTest, AuthenticateTest) {
    Person person("John", "Doe", 30, 'M');
    testing::internal::CaptureStdout();
    person.Authenticate();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Аутентификация пользователя John Doe\n");
}

TEST(PersonTest, UpdatePersonalInfoTest) {
    Person person("Alice", "Smith", 25, 'F');
    testing::internal::CaptureStdout();
    person.UpdatePersonalInfo();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Обновление личных данных для Alice Smith\n");
}

// Тесты для класса Employee
TEST(EmployeeTest, ManagePersonalInfoTest) {
    Employee employee("John", "Doe", 30, 'M', 12345, "Manager", 50000.0);
    testing::internal::CaptureStdout();
    employee.ManagePersonalInfo();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Управление личными данными сотрудника John Doe\n");
}

TEST(EmployeeTest, WorkReportTest) {
    Employee employee("Alice", "Smith", 25, 'F', 54321, "Developer", 60000.0);
    testing::internal::CaptureStdout();
    employee.WorkReport();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Создание отчета о работе для сотрудника Alice Smith\n");
}

// Тесты для класса Administrator
TEST(AdministratorTest, ManageAdminFunctionsTest) {
    Administrator admin("Admin", "Adminson", 40, 'M', 99999, "Administrator", 70000.0, 3);
    testing::internal::CaptureStdout();
    admin.ManageAdminFunctions();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Управление административными функциями музея для Admin Adminson\n");
}

// Тесты для класса Guide
TEST(GuideTest, ConductTourTest) {
    Guide guide("Tour", "Guide", 35, 'M', 77777, "Tour Guide", 45000.0, "Tour License");
    testing::internal::CaptureStdout();
    guide.ConductTour();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Проведение экскурсии для Tour Guide\n");
}

TEST(GuideTest, ProvideInformationTest) {
    Guide guide("Info", "Provider", 28, 'F', 88888, "Information Provider", 40000.0, "Info License");
    testing::internal::CaptureStdout();
    guide.ProvideInformation();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Предоставление информации для Info Provider\n");
}

// Тесты для класса Visitor
TEST(VisitorTest, PurchaseTicketTest) {
    Visitor visitor("Visitor", "One", 22, 'M', 123, "2023-09-25");
    testing::internal::CaptureStdout();
    visitor.PurchaseTicket();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Покупка билета для Visitor One\n");
}

TEST(VisitorTest, RateMuseumTest) {
    Visitor visitor("Museum", "Visitor", 30, 'F', 456, "2023-09-25");
    testing::internal::CaptureStdout();
    visitor.RateMuseum();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Оценка музея посетителем Museum Visitor\n");
}

// Тесты для класса Ticket
TEST(TicketTest, GetIDTest) {
    Ticket ticket(123, 25.0, "Adult");
    EXPECT_EQ(ticket.GetID(), 123);
}

TEST(TicketTest, GetPriceTest) {
    Ticket ticket(456, 15.5, "Child");
    EXPECT_DOUBLE_EQ(ticket.GetPrice(), 15.5);
}

TEST(TicketTest, GetTypeTest) {
    Ticket ticket(789, 30.0, "Senior");
    EXPECT_EQ(ticket.GetType(), "Senior");
}

// Тесты для класса Exponat
TEST(ExponatTest, GetIDTest) {
    Exponat exponat(123, "Painting", "Famous painting description", "Artist Name");
    EXPECT_EQ(exponat.GetID(), 123);
}

TEST(ExponatTest, GetNameTest) {
    Exponat exponat(456, "Sculpture", "Ancient sculpture description", "Ancient Sculptor");
    EXPECT_EQ(exponat.GetName(), "Sculpture");
}

// Тесты для класса Exhibition
TEST(ExhibitionTest, GetStartDateTest) {
    Exhibition exhibition("Ancient Art", "2023-10-01", "2023-12-31");
    EXPECT_EQ(exhibition.GetStartDate(), "2023-10-01");
}

TEST(ExhibitionTest, GetEndDateTest) {
    Exhibition exhibition("Modern Art", "2024-04-15", "2024-06-15");
    EXPECT_EQ(exhibition.GetEndDate(), "2024-06-15");
}

// Тесты для класса MuseumHall
TEST(MuseumHallTest, GetNameTest) {
    MuseumHall hall("Hall 1", "Artifacts and history");
    EXPECT_EQ(hall.GetName(), "Hall 1");
}

TEST(MuseumHallTest, GetDescriptionTest) {
    MuseumHall hall("Hall 2", "Modern Art Gallery");
    EXPECT_EQ(hall.GetDescription(), "Modern Art Gallery");
}

TEST(FinancialDepartmentTest, AnalyzeExpensesTest) {
    FinancialDepartment financeDept(1000000.0);
    testing::internal::CaptureStdout();
    financeDept.AnalyzeExpenses();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Анализ расходов финансового отдела\n");
}

// Тесты для класса Museum
TEST(MuseumTest, ManageMuseumInfoTest) {
    Museum museum("Art Museum", "123 Main St", "Mon-Fri: 9 AM - 5 PM");
    testing::internal::CaptureStdout();
    museum.ManageMuseumInfo();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Управление информацией о музее Art Museum\n");
}

TEST(MuseumTest, ManageHallsTest) {
    Museum museum("Science Museum", "789 Oak St", "Wed-Sun: 11 AM - 7 PM");
    testing::internal::CaptureStdout();
    museum.ManageHalls();
    std::string output = testing::internal::GetCapturedStdout();
    EXPECT_EQ(output, "Управление залами музея Science Museum\n");
}

int main(int argc, char** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}