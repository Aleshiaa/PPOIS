#include <.\inc\FinancialDepartment.h>

FinancialDepartment::FinancialDepartment(double budget)
    : budget(budget) {
}

void FinancialDepartment::RecordFinancialTransaction(double amount, const std::string& description) {
    financialTransactions.push_back(std::make_pair(amount, description));
}

void FinancialDepartment::AnalyzeExpenses() {
    std::cout << "Анализ расходов финансового отдела" << std::endl;
}
