#include "gtest/gtest.h"
#include "Sort.cpp"

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

TEST(SortingAlgorithms, IntroSort) {


    std::vector<int> intVector = {5, 2, 8, 3, 1};
    introSort(intVector);
    std::vector<int> sortedIntVector = {1, 2, 3, 5, 8};
    EXPECT_EQ(intVector, sortedIntVector);


    int intArray[] = {5, 2, 8, 3, 1};
    introSort(intArray, sizeof(intArray) / sizeof(int));
    int sortedIntArray[] = {1, 2, 3, 5, 8};
    EXPECT_TRUE(std::equal(std::begin(intArray), std::end(intArray), std::begin(sortedIntArray)));


    std::vector<CustomClass> customVector = {CustomClass(5), CustomClass(2), CustomClass(8), CustomClass(3), CustomClass(1)};
    introSort(customVector);
    std::vector<CustomClass> sortedCustomVector = {CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(5), CustomClass(8)};
    EXPECT_EQ(customVector, sortedCustomVector);


    CustomClass customArray[] = {CustomClass(5), CustomClass(2), CustomClass(8), CustomClass(3), CustomClass(1)};
    introSort(customArray, sizeof(customArray) / sizeof(CustomClass));
    CustomClass sortedCustomArray[] = {CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(5), CustomClass(8)};
    EXPECT_TRUE(std::equal(std::begin(customArray), std::end(customArray), std::begin(sortedCustomArray)));
}

TEST(SortingAlgorithms, TacoSort) {


    std::vector<int> intVector = {5, 2, 8, 3, 1};
    tacoSort(intVector);
    std::vector<int> sortedIntVector = {1, 2, 3, 5, 8};
    EXPECT_EQ(intVector, sortedIntVector);


    int intArray[] = {5, 2, 8, 3, 1};
    tacoSort(intArray, sizeof(intArray) / sizeof(int));
    int sortedIntArray[] = {1, 2, 3, 5, 8};
    EXPECT_TRUE(std::equal(std::begin(intArray), std::end(intArray), std::begin(sortedIntArray)));


    std::vector<CustomClass> customVector = {CustomClass(5), CustomClass(2), CustomClass(8), CustomClass(3), CustomClass(1)};
    tacoSort(customVector);
    std::vector<CustomClass> sortedCustomVector = {CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(5), CustomClass(8)};
    EXPECT_EQ(customVector, sortedCustomVector);


    CustomClass customArray[] = {CustomClass(5), CustomClass(2), CustomClass(8), CustomClass(3), CustomClass(1)};
    tacoSort(customArray, sizeof(customArray) / sizeof(CustomClass));
    CustomClass sortedCustomArray[] = {CustomClass(1), CustomClass(2), CustomClass(3), CustomClass(5), CustomClass(8)};
    EXPECT_TRUE(std::equal(std::begin(customArray), std::end(customArray), std::begin(sortedCustomArray)));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
