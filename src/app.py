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
    for i in range(0, 500):
        random_list.append(random.randint(0, 99999))

    # Merge-Sort
    merge_sort = MergeSort(SortingStrategy.LOW_TO_HIGH, display)
    sorted_list = merge_sort.timed_sort(random_list)
    print(f"{merge_sort.name}: \nsorted-list: {sorted_list[0]} \ntime: "
          f"{sorted_list[1]} \ncomplexity: {merge_sort.complexity}\n")

    # Insertion-Sort
    insertion_sort = InsertionSort(SortingStrategy.LOW_TO_HIGH, display)
    exec_time = insertion_sort.timed_sort(random_list)
    print(f"{insertion_sort.name}: \nsorted-list: {random_list} \ntime: "
          f"{exec_time} \ncomplexity: {insertion_sort.complexity}\n")


if __name__ == "__main__":
    main()
