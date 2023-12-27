#include "matrix.h"
#include <fstream>


Matrix::Matrix(size_t rows, size_t cols) : rows(rows), cols(cols) {
    data.resize(rows, std::vector<double>(cols, 0.0));
}

Matrix::Matrix(const Matrix &other) : rows(other.rows), cols(other.cols), data(other.data) {}

Matrix &Matrix::operator=(const Matrix &other) {
    if (this != &other) {
        rows = other.rows;
        cols = other.cols;
        data = other.data;
    }
    return *this;
}

bool Matrix::operator==(const Matrix &other) const {
    return (rows == other.rows) && (cols == other.cols) && (data == other.data);
}

bool Matrix::operator!=(const Matrix &other) const {
    return !(*this == other);
}

std::ostream &operator<<(std::ostream &out, const Matrix &matrix) {
    for (size_t i = 0; i < matrix.rows; ++i) {
        for (size_t j = 0; j < matrix.cols; ++j) {
            out << matrix.data[i][j] << ' ';
        }
        out << '\n';
    }
    return out;
}

std::istream &operator>>(std::istream &in, Matrix &matrix) {
    for (size_t i = 0; i < matrix.rows; ++i) {
        for (size_t j = 0; j < matrix.cols; ++j) {
            in >> matrix.data[i][j];
        }
    }
    return in;
}

void Matrix::resize(size_t newRows, size_t newCols) {
    data.resize(newRows, std::vector<double>(newCols, 0.0));
    rows = newRows;
    cols = newCols;
}

void Matrix::loadFromFile(const std::string &filename) {
    std::ifstream file(filename);
    if (file.is_open()) {
        file >> *this;
        file.close();
    } else {
        std::cerr << "Error: Unable to open file " << filename << std::endl;
    }
}

Matrix Matrix::subMatrix(size_t startRow, size_t startCol, size_t subRows, size_t subCols) const {
    if (startRow >= rows || startCol >= cols || startRow + subRows > rows || startCol + subCols > cols) {
        std::cerr << "Error: Invalid submatrix dimensions or starting indices." << std::endl;
        return Matrix(0, 0);
    }

    Matrix submatrix(subRows, subCols);
    for (size_t i = 0; i < subRows; ++i) {
        for (size_t j = 0; j < subCols; ++j) {
            submatrix.data[i][j] = data[startRow + i][startCol + j];
        }
    }
    return submatrix;
}


bool Matrix::isSquare() const {
    return rows == cols;
}

bool Matrix::isDiagonal() const {
    if (!isSquare()) {
        return false;
    }

    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            if (i != j && data[i][j] != 0.0) {
                return false;
            }
        }
    }
    return true;
}

bool Matrix::isZero() const {
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            if (data[i][j] != 0.0) {
                return false;
            }
        }
    }
    return true;
}

bool Matrix::isIdentity() const {
    if (!isSquare()) {
        return false;
    }

    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            if ((i == j && data[i][j] != 1.0) || (i != j && data[i][j] != 0.0)) {
                return false;
            }
        }
    }
    return true;
}

bool Matrix::isSymmetric() const {
    if (!isSquare()) {
        return false;
    }

    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            if (data[i][j] != data[j][i]) {
                return false;
            }
        }
    }
    return true;
}

bool Matrix::isUpperTriangular() const {
    for (size_t i = 1; i < rows; ++i) {
        for (size_t j = 0; j < i; ++j) {
            if (data[i][j] != 0.0) {
                return false;
            }
        }
    }
    return true;
}

bool Matrix::isLowerTriangular() const {
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = i + 1; j < cols; ++j) {
            if (data[i][j] != 0.0) {
                return false;
            }
        }
    }
    return true;
}

Matrix Matrix::transpose() const {
    Matrix result(cols, rows);
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            result.data[j][i] = data[i][j];
        }
    }
    return result;
}

std::vector<double>& Matrix::operator[](size_t index) {
    if (index < rows) {
        return data[index];
    } else {
        throw std::out_of_range("Index out of bounds");
    }
}