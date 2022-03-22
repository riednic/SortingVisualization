from sorting_algorithms import (
    InsertionSort,
    MergeSort,
    SortingStrategy
)

import random


def main():
    random_list = []
    for i in range(0, 5000):
        random_list.append(random.randint(0, 99999))

    # Merge-Sort
    merge_sort = MergeSort(SortingStrategy.LOW_TO_HIGH)
    sorted_list = merge_sort.timed_sort(random_list)
    print(f"{merge_sort.name}: \nsorted-list: {sorted_list[0]} \ntime: "
          f"{sorted_list[1]} \ncomplexity: {merge_sort.complexity}\n")

    # Insertion-Sort
    insertion_sort = InsertionSort(SortingStrategy.LOW_TO_HIGH)
    exec_time = insertion_sort.timed_sort(random_list)
    print(f"{insertion_sort.name}: \nsorted-list: {random_list} \ntime: "
          f"{exec_time} \ncomplexity: {insertion_sort.complexity}\n")


if __name__ == "__main__":
    main()
