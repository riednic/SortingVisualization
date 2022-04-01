import drawable_algorithms as da
from random import shuffle
from scene import Scene


def main():
    scene = Scene(1920, 600)

    # Quick-Sort
    random_list = list(range(1, 200))
    shuffle(random_list)
    quick_sort = da.QuickSort(da.SortingStrategy.HIGH_TO_LOW, scene)
    quick_sort.draw_sorting_algorithm(random_list)

    # Merge-Sort
    random_list = list(range(1, 200))
    shuffle(random_list)
    merge_sort = da.MergeSort(da.SortingStrategy.HIGH_TO_LOW, scene)
    merge_sort.draw_sorting_algorithm(random_list)

    # Bubble-Sort
    random_list = list(range(1, 100))
    shuffle(random_list)
    bubble_sort = da.BubbleSort(da.SortingStrategy.HIGH_TO_LOW, scene)
    bubble_sort.draw_sorting_algorithm(random_list)

    # Insertion-Sort
    random_list = list(range(1, 100))
    shuffle(random_list)
    insertion_sort = da.InsertionSort(da.SortingStrategy.HIGH_TO_LOW, scene)
    insertion_sort.draw_sorting_algorithm(random_list)


if __name__ == "__main__":
    main()
