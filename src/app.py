from sorting_algorithms import (
    InsertionSort,
    MergeSort,
    SortingStrategy
)
import pygame


import random


def main():
    pygame.init()
    display = pygame.display.set_mode((1024, 512))

    random_list = []
    for i in range(0, 125):
        random_list.append(random.randint(0, 99999))

    # Merge-Sort
    merge_sort = MergeSort(random_list, SortingStrategy.LOW_TO_HIGH, display)
    sorted_list, time = merge_sort.timed_sort()
    print(f"{merge_sort.name}: \nsorted-list: {sorted_list} \ntime: "
          f"{time} \ncomplexity: {merge_sort.complexity}\n")

    # Insertion-Sort
    insertion_sort = InsertionSort(random_list, SortingStrategy.LOW_TO_HIGH, display)
    sorted_list, time = insertion_sort.timed_sort()
    print(f"{insertion_sort.name}: \nsorted-list: {sorted_list} \ntime: "
          f"{time} \ncomplexity: {insertion_sort.complexity}\n")

    random_list = []
    for i in range(0, 125):
        random_list.append(random.randint(0, 9999))

    # Insertion-Sort
    insertion_sort.change_sortable(random_list)
    sorted_list, time = insertion_sort.timed_sort()
    print(f"{insertion_sort.name}: \nsorted-list: {sorted_list} \ntime: "
          f"{time} \ncomplexity: {insertion_sort.complexity}\n")


if __name__ == "__main__":
    main()
