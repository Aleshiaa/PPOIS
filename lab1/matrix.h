#ifndef MATRIX_H
#define MATRIX_H

#include <iostream>
#include <vector>

class Matrix {
private:
    std::vector<std::vector<double>> data;
    size_t rows;
    size_t cols;

public:
    // Конструкторы
    Matrix(size_t rows, size_t cols);
    Matrix(const Matrix &other);

    // Деструктор
    ~Matrix();

    // Оператор присваивания
    Matrix &operator=(const Matrix &other);

    // Операторы сравнения
    bool operator==(const Matrix &other) const;
    bool operator!=(const Matrix &other) const;

    // Операторы ввода/вывода
    friend std::ostream &operator<<(std::ostream &out, const Matrix &matrix);
    friend std::istream &operator>>(std::istream &in, Matrix &matrix);

    //// Оператор индексации для доступа к элементам матрицы
    std::vector<double>& operator[](size_t row) {
        return data[row];
    }

    const std::vector<double>& operator[](size_t row) const {
        return data[row];
    }

    // Изменение размера матрицы
    void resize(size_t newRows, size_t newCols);

    // Загрузка матрицы из файла
    void loadFromFile(const std::string &filename);

    // Извлечение подматрицы
    Matrix subMatrix(size_t startRow, size_t startCol, size_t subRows, size_t subCols) const;

    // Проверка типа матрицы
    bool isSquare() const;
    bool isDiagonal() const;
    bool isZero() const;
    bool isIdentity() const;
    bool isSymmetric() const;
    bool isUpperTriangular() const;
    bool isLowerTriangular() const;

    // Транспонирование матрицы
    Matrix transpose() const;
};

#endif // MATRIX_H