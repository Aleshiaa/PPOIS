// tests.cpp
#include "gtest/gtest.h"
#include "Sort.cpp"

// Пример собственного класса для тестирования
class CustomClass {
public:
    int value;

    CustomClass(int val) : value(val) {}

    bool operator==(const CustomClass& other) const {
        return value == other.value;
    }

     bool operator<(const CustomClass& other) const {
        return value < other.value;
    }

    bool operator>(const CustomClass& other) const {
        return value > other.value;
    }

     bool operator<=(const CustomClass& other) const {
        return value <= other.value;
    }
};

// Тестирование IntroSort
TEST(SortingAlgorithms, IntroSort) {
    std::vector<int> intArray = {5, 2, 8, 3, 1};
    introSort(intArray);

    std::vector<int> sortedIntArray = {1, 2, 3, 5, 8};
    EXPECT_EQ(intArray, sortedIntArray);

    std::vector<CustomClass> customArray = {CustomClass(5), CustomClass(2), CustomClass(8), CustomClass(3), CustomClass(1)};
    introSort(customArray);

    std::vector<CustomClass> sortedCustomArray = {CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(5), CustomClass(8)};
    EXPECT_EQ(customArray, sortedCustomArray);
}

// Тестирование TacoSort
TEST(SortingAlgorithms, TacoSort) {
    std::vector<int> intArray = {5, 2, 8, 3, 1};
    tacoSort(intArray);

    std::vector<int> sortedIntArray = {1, 2, 3, 5, 8};
    EXPECT_EQ(intArray, sortedIntArray);

    std::vector<CustomClass> customArray = {CustomClass(5), CustomClass(2), CustomClass(8), CustomClass(3), CustomClass(1)};
    tacoSort(customArray);

    std::vector<CustomClass> sortedCustomArray = {CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(5), CustomClass(8)};
    EXPECT_EQ(customArray, sortedCustomArray);
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
