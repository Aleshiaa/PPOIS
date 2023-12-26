
#include "Sort.h"
#include <algorithm>
#include <functional>
#include <cmath>

template <typename T>
void introSort(std::vector<T>& array) {
    int depthLimit = 2 * log(array.size());
    introSortHelper(array, 0, array.size() - 1);
}

template <typename T>
void introSortRecursion(std::vector<T>& array, int begin, int end, int depthLimit) {
    if (end - begin > 16) {
        if (depthLimit == 0) {
            std::make_heap(array.begin() + begin, array.begin() + end + 1, std::greater<T>());
            std::sort_heap(array.begin() + begin, array.begin() + end + 1, std::greater<T>());
            return;
        }

        int pivot = partition(array, begin, end);
        introSortRecursion(array, begin, pivot, depthLimit - 1);
        introSortRecursion(array, pivot + 1, end, depthLimit - 1);
    } else {
        insertionSort(array, begin, end);
    }
}

template <typename T>
void introSortHelper(std::vector<T>& array, int begin, int end) {
    int depthLimit = 2 * log(array.size());
    introSortRecursion(array, begin, end, depthLimit);
}

template <typename T>
int partition(std::vector<T>& array, int begin, int end) {
    int pivot = choosePivot(array, begin, end);
    std::swap(array[pivot], array[end]);
    
    int i = begin - 1;
    for (int j = begin; j < end; ++j) {
        if (array[j] <= array[end]) {
            ++i;
            std::swap(array[i], array[j]);
        }
    }
    
    std::swap(array[i + 1], array[end]);
    return i + 1;
}

template <typename T>
int choosePivot(const std::vector<T>& array, int begin, int end) {
    return (begin + end) / 2;
}

template <typename T>
void insertionSort(std::vector<T>& array, int begin, int end) {
    for (int i = begin + 1; i <= end; ++i) {
        T key = array[i];
        int j = i - 1;

        while (j >= begin && array[j] > key) {
            array[j + 1] = array[j];
            --j;
        }

        array[j + 1] = key;
    }
}

template <typename T>
void tacoSort(std::vector<T>& array) {
    int depthLimit = 2 * log(array.size());
    tacoSortRecursion(array, 0, array.size() - 1, depthLimit);
}

template <typename T>
void reverseTaco(std::vector<T>& array, int begin, int end) {
    for (int i = 0; i < (end - begin + 1) / 2; ++i) {
        std::swap(array[begin + i], array[end - i]);
    }
}

template <typename T>
void tacoSortRecursion(std::vector<T>& array, int begin, int end, int depthLimit) {
    if (end - begin > 16) {
        if (depthLimit == 0) {
            reverseTaco(array, begin, end);
            return;
        }

        int pivot = partition(array, begin, end);
        tacoSortRecursion(array, begin, pivot, depthLimit - 1);
        tacoSortRecursion(array, pivot + 1, end, depthLimit - 1);
    } else {
        insertionSort(array, begin, end);
    }
}


template <typename T>
void introSort(T* array, int size) {
    int depthLimit = 2 * log(size);
    introSortHelper(array, 0, size - 1);
}

template <typename T>
void introSortRecursion(T* array, int begin, int end, int depthLimit) {
    if (end - begin > 16) {
        if (depthLimit == 0) {
            std::make_heap(array + begin, array + end + 1, std::greater<T>());
            std::sort_heap(array + begin, array + end + 1, std::greater<T>());
            return;
        }

        int pivot = partition(array, begin, end);
        introSortRecursion(array, begin, pivot, depthLimit - 1);
        introSortRecursion(array, pivot + 1, end, depthLimit - 1);
    } else {
        insertionSort(array, begin, end);
    }
}

template <typename T>
void introSortHelper(T* array, int begin, int end) {
    int depthLimit = 2 * log(end - begin + 1);
    introSortRecursion(array, begin, end, depthLimit);
}

template <typename T>
int partition(T* array, int begin, int end) {
    int pivot = choosePivot(array, begin, end);
    std::swap(array[pivot], array[end]);

    int i = begin - 1;
    for (int j = begin; j < end; ++j) {
        if (array[j] <= array[end]) {
            ++i;
            std::swap(array[i], array[j]);
        }
    }

    std::swap(array[i + 1], array[end]);
    return i + 1;
}

template <typename T>
int choosePivot(T* array, int begin, int end) {
    return (begin + end) / 2;
}

template <typename T>
void insertionSort(T* array, int begin, int end) {
    for (int i = begin + 1; i <= end; ++i) {
        T key = array[i];
        int j = i - 1;

        while (j >= begin && array[j] > key) {
            array[j + 1] = array[j];
            --j;
        }

        array[j + 1] = key;
    }
}

template <typename T>
void tacoSort(T* array, int size) {
    int depthLimit = 2 * log(size);
    tacoSortRecursion(array, 0, size - 1, depthLimit);
}

template <typename T>
void reverseTaco(T* array, int begin, int end) {
    for (int i = 0; i < (end - begin + 1) / 2; ++i) {
        std::swap(array[begin + i], array[end - i]);
    }
}

template <typename T>
void tacoSortRecursion(T* array, int begin, int end, int depthLimit) {
    if (end - begin > 16) {
        if (depthLimit == 0) {
            reverseTaco(array, begin, end);
            return;
        }

        int pivot = partition(array, begin, end);
        tacoSortRecursion(array, begin, pivot, depthLimit - 1);
        tacoSortRecursion(array, pivot + 1, end, depthLimit - 1);
    } else {
        insertionSort(array, begin, end);
    }
}
