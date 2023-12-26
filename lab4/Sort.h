#pragma once

#include <vector>

template <typename T>
void introSort(std::vector<T>& array);

template <typename T>
void introSortRecursion(std::vector<T>& array, int begin, int end, int depthLimit);

template <typename T>
void introSortHelper(std::vector<T>& array, int begin, int end);


template <typename T>
void tacoSort(std::vector<T>& array);

template <typename T>
void reverseTaco(std::vector<T>& array, int begin, int end);

template <typename T>
void tacoSortRecursion(std::vector<T>& array, int begin, int end, int depthLimit);