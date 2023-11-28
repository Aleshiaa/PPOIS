#include "gtest/gtest.h"
#include "matrix.h"

// Тесты конструкторов и операторов
TEST(MatrixTest, ConstructorsAndOperators) {
    // Тест конструктора по умолчанию
    Matrix matrix1(3, 3);
    EXPECT_EQ(matrix1.isZero(), true);

    // Тест конструктора копирования
    Matrix matrix2(matrix1);
    EXPECT_EQ(matrix2, matrix1);

    // Тест оператора присваивания
    Matrix matrix3 = matrix2;
    EXPECT_EQ(matrix3, matrix2);

    // Тест операторов сравнения
    EXPECT_EQ(matrix1 == matrix2, true);
    EXPECT_EQ(matrix1 != matrix3, false);
}

// Тесты методов изменения размера и загрузки из файла
TEST(MatrixTest, ResizeAndLoadFromFile) {
    Matrix matrix(2, 3);

    // Тест изменения размера
    matrix.resize(3, 2);
    EXPECT_EQ(matrix.isZero(), true);

    // Тест загрузки из файла (предполагается, что файл matrix_test.txt существует)
    matrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/matrix_test.txt");
    EXPECT_EQ(matrix.isZero(), false);
}

// Тесты методов извлечения подматрицы и транспонирования
TEST(MatrixTest, SubMatrixAndTranspose) {
    Matrix matrix(3, 3);
    matrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/matrix_test.txt");

    // Тест извлечения подматрицы
    Matrix submatrix = matrix.subMatrix(0, 1, 2, 2);
    EXPECT_EQ(submatrix, Matrix(2, 2));

    // Тест транспонирования
    Matrix transposedMatrix = matrix.transpose();
    EXPECT_EQ(transposedMatrix.transpose(), matrix); // Проверка, что транспонирование дважды вернет исходную матрицу
}

// Тесты проверки типа матрицы
TEST(MatrixTest, MatrixTypeCheck) {

    // Тесты на квадратность
    Matrix squareMatrix(3, 3);
    Matrix nonSquareMatrix(2, 3);
    EXPECT_EQ(squareMatrix.isSquare(), true);
    EXPECT_EQ(nonSquareMatrix.isSquare(), false);

    Matrix diagonalMatrix(3, 3);
    for (size_t i = 0; i < 3; ++i) {
        for (size_t j = 0; j < 3; ++j) {
            diagonalMatrix[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }
    EXPECT_EQ(diagonalMatrix.isDiagonal(), true);
    EXPECT_EQ(squareMatrix.isDiagonal(), true);

    // Тест на единичную матрицу
    Matrix identityMatrix(3, 3);
    for (size_t i = 0; i < 3; ++i) {
        for (size_t j = 0; j < 3; ++j) {
            identityMatrix[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }
    EXPECT_EQ(identityMatrix.isIdentity(), true);
    EXPECT_EQ(squareMatrix.isIdentity(), false);


    // Тест на нулевую матрицу
    Matrix zeroMatrix(2, 2);
    EXPECT_EQ(zeroMatrix.isZero(), true);
    EXPECT_EQ(squareMatrix.isZero(), true);


    // Тест на симметричность
    Matrix symmetricMatrix(3, 3);
    symmetricMatrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/symmetric_matrix_test.txt"); // Файл содержит симметричную матрицу
    EXPECT_EQ(symmetricMatrix.isSymmetric(), true);
    EXPECT_EQ(squareMatrix.isSymmetric(), true);

    // Тест на верхнюю треугольность
    Matrix upperTriangularMatrix(3, 3);
    upperTriangularMatrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/upper_triangular_matrix_test.txt"); // Файл содержит верхнюю треугольную матрицу
    EXPECT_EQ(upperTriangularMatrix.isUpperTriangular(), true);
    EXPECT_EQ(squareMatrix.isUpperTriangular(), true);

    // Тест на нижнюю треугольность
    Matrix lowerTriangularMatrix(3, 3);
    lowerTriangularMatrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/lower_triangular_matrix_test.txt"); // Файл содержит нижнюю треугольную матрицу
    EXPECT_EQ(lowerTriangularMatrix.isLowerTriangular(), true);
    EXPECT_EQ(squareMatrix.isLowerTriangular(), true);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}