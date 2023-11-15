#pragma once
#include <string>
#include <vector>
#include <iostream>
/**
 * @brief Класс Отдел Финансов
 * 
 */
class FinancialDepartment {
public:
    /**
     * @brief Конструктор финансового отдела
     * @param budget бюджет музея
     * 
     */
    FinancialDepartment(double budget);

    /**
    * @brief записть финансовых операций
    * @param amount количество
    * @param description описание
    */
    void RecordFinancialTransaction(double amount, const std::string& description);
    /**
    * @brief анализ затрат
    * 
    */
    void AnalyzeExpenses();
    double budget;
    std::vector<std::pair<double, std::string>> financialTransactions;
};
