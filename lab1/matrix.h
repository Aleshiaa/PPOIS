#ifndef MATRIX_H
#define MATRIX_H

#include <iostream>
#include <vector>

/**
 * @brief Represents a mathematical matrix.
 */
class Matrix {
private:
    std::vector<std::vector<double>> data; ///< 2D vector to store matrix elements.
    size_t rows; ///< Number of rows in the matrix.
    size_t cols; ///< Number of columns in the matrix.

public:
    /**
     * @brief Constructor to create a matrix with specified dimensions.
     * @param rows Number of rows in the matrix.
     * @param cols Number of columns in the matrix.
     */
    Matrix(size_t rows, size_t cols);

    /**
     * @brief Copy constructor to create a matrix as a copy of another matrix.
     * @param other The matrix to be copied.
     */
    Matrix(const Matrix &other);

    /**
     * @brief Assignment operator to assign the contents of another matrix to this matrix.
     * @param other The matrix to be assigned.
     * @return Reference to the modified matrix.
     */
    Matrix &operator=(const Matrix &other);

    /**
     * @brief Equality comparison operator to check if two matrices are equal.
     * @param other The matrix to be compared.
     * @return True if matrices are equal, false otherwise.
     */
    bool operator==(const Matrix &other) const;

    /**
     * @brief Inequality comparison operator to check if two matrices are not equal.
     * @param other The matrix to be compared.
     * @return True if matrices are not equal, false otherwise.
     */
    bool operator!=(const Matrix &other) const;

    /**
     * @brief Overloaded stream insertion operator to print the matrix to an output stream.
     * @param out The output stream.
     * @param matrix The matrix to be printed.
     * @return Reference to the output stream.
     */
    friend std::ostream &operator<<(std::ostream &out, const Matrix &matrix);

    /**
     * @brief Overloaded stream extraction operator to read a matrix from an input stream.
     * @param in The input stream.
     * @param matrix The matrix to be read into.
     * @return Reference to the input stream.
     */
    friend std::istream &operator>>(std::istream &in, Matrix &matrix);

    /**
     * @brief Accessor to get a reference to a row of the matrix.
     * @param row The index of the row.
     * @return Reference to the specified row.
     */
    std::vector<double>& operator[](size_t row);

    /**
     * @brief Const accessor to get a reference to a row of the matrix (for const matrices).
     * @param row The index of the row.
     * @return Reference to the specified row.
     */
    const std::vector<double>& operator[](size_t row) const;

    /**
     * @brief Resize the matrix to the specified dimensions.
     * @param newRows The new number of rows.
     * @param newCols The new number of columns.
     */
    void resize(size_t newRows, size_t newCols);

    /**
     * @brief Load matrix data from a file with the specified filename.
     * @param filename The name of the file to load data from.
     */
    void loadFromFile(const std::string &filename);

    /**
     * @brief Create and return a submatrix of the current matrix.
     * @param startRow The starting row index of the submatrix.
     * @param startCol The starting column index of the submatrix.
     * @param subRows The number of rows in the submatrix.
     * @param subCols The number of columns in the submatrix.
     * @return The submatrix.
     */
    Matrix subMatrix(size_t startRow, size_t startCol, size_t subRows, size_t subCols) const;

    /**
     * @brief Check if the matrix is square (equal number of rows and columns).
     * @return True if the matrix is square, false otherwise.
     */
    bool isSquare() const;

    /**
     * @brief Check if the matrix is diagonal (non-diagonal elements are zero).
     * @return True if the matrix is diagonal, false otherwise.
     */
    bool isDiagonal() const;

    /**
     * @brief Check if all elements in the matrix are zero.
     * @return True if all elements are zero, false otherwise.
     */
    bool isZero() const;

    /**
     * @brief Check if the matrix is an identity matrix.
     * @return True if the matrix is an identity matrix, false otherwise.
     */
    bool isIdentity() const;

    /**
     * @brief Check if the matrix is symmetric.
     * @return True if the matrix is symmetric, false otherwise.
     */
    bool isSymmetric() const;

    /**
     * @brief Check if the matrix is upper triangular.
     * @return True if the matrix is upper triangular, false otherwise.
     */
    bool isUpperTriangular() const;

    /**
     * @brief Check if the matrix is lower triangular.
     * @return True if the matrix is lower triangular, false otherwise.
     */
    bool isLowerTriangular() const;

    /**
     * @brief Compute and return the transpose of the matrix.
     * @return The transposed matrix.
     */
    Matrix transpose() const;
};

#endif