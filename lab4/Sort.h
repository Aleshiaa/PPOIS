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


template <typename T>
void introSort(T* array, int size);

template <typename T>
void introSortRecursion(T* array, int begin, int end, int depthLimit);

template <typename T>
void introSortHelper(T* array, int begin, int end);


template <typename T>
void tacoSort(T* array, int size);

template <typename T>
void reverseTaco(T* array, int begin, int end);

template <typename T>
void tacoSortRecursion(T* array, int begin, int end, int depthLimit);
