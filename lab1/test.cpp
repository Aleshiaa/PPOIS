#include "gtest/gtest.h"
#include "matrix.h"


TEST(MatrixTest, ConstructorsAndOperators) {

    Matrix matrix1(3, 3);
    EXPECT_EQ(matrix1.isZero(), true);

 
    Matrix matrix2(matrix1);
    EXPECT_EQ(matrix2, matrix1);


    Matrix matrix3 = matrix2;
    EXPECT_EQ(matrix3, matrix2);


    EXPECT_EQ(matrix1 == matrix2, true);
    EXPECT_EQ(matrix1 != matrix3, false);
}


TEST(MatrixTest, ResizeAndLoadFromFile) {
    Matrix matrix(2, 3);

    matrix.resize(3, 2);
    EXPECT_EQ(matrix.isZero(), true);

    matrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/matrix_test.txt");
    EXPECT_EQ(matrix.isZero(), false);
}

TEST(MatrixTest, SubMatrixAndTranspose) {
    Matrix matrix(3, 3);
    matrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/matrix_test.txt");

    Matrix submatrix = matrix.subMatrix(0, 1, 2, 2);
    EXPECT_EQ(submatrix, Matrix(2, 2));

    Matrix transposedMatrix = matrix.transpose();
    EXPECT_EQ(transposedMatrix.transpose(), matrix);
}

TEST(MatrixTest, MatrixTypeCheck) {

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

    Matrix identityMatrix(3, 3);
    for (size_t i = 0; i < 3; ++i) {
        for (size_t j = 0; j < 3; ++j) {
            identityMatrix[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }
    EXPECT_EQ(identityMatrix.isIdentity(), true);
    EXPECT_EQ(squareMatrix.isIdentity(), false);

    Matrix zeroMatrix(2, 2);
    EXPECT_EQ(zeroMatrix.isZero(), true);
    EXPECT_EQ(squareMatrix.isZero(), true);


    Matrix symmetricMatrix(3, 3);
    symmetricMatrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/symmetric_matrix_test.txt");
    EXPECT_EQ(symmetricMatrix.isSymmetric(), true);
    EXPECT_EQ(squareMatrix.isSymmetric(), true);

    Matrix upperTriangularMatrix(3, 3);
    upperTriangularMatrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/upper_triangular_matrix_test.txt"); 
    EXPECT_EQ(upperTriangularMatrix.isUpperTriangular(), true);
    EXPECT_EQ(squareMatrix.isUpperTriangular(), true);

    Matrix lowerTriangularMatrix(3, 3);
    lowerTriangularMatrix.loadFromFile("D:/BSUIR/3_semester/PPOIS/lab1/lower_triangular_matrix_test.txt");
    EXPECT_EQ(lowerTriangularMatrix.isLowerTriangular(), true);
    EXPECT_EQ(squareMatrix.isLowerTriangular(), true);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}