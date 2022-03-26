import drawable_algorithms as da
import pygame
import random


def main():
    pygame.init()
    display = pygame.display.set_mode((1024, 512))

    random_list = []
    for i in range(0, 50):
        random_list.append(random.randint(0, 99999))

    # Quick-Sort
    quick_sort = da.QuickSort(da.SortingStrategy.LOW_TO_HIGH, display)
    print(quick_sort.timed_sort(random_list))

    random_list = []
    for i in range(0, 50):
        random_list.append(random.randint(0, 99999))

    # Bubble-Sort
    bubble_sort = da.BubbleSort(da.SortingStrategy.LOW_TO_HIGH, display)
    print(bubble_sort.timed_sort(random_list))

    random_list = []
    for i in range(0, 50):
        random_list.append(random.randint(0, 99999))

    # Merge-Sort
    merge_sort = da.MergeSort(da.SortingStrategy.LOW_TO_HIGH, display)
    print(merge_sort.timed_sort(random_list))

    random_list = []
    for i in range(0, 50):
        random_list.append(random.randint(0, 99999))

    # Insertion-Sort
    insertion_sort = da.InsertionSort(da.SortingStrategy.LOW_TO_HIGH, display)
    print(insertion_sort.timed_sort(random_list))

if __name__ == "__main__":
    main()
