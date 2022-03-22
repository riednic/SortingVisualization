from enum import IntEnum
from time import perf_counter


class SortingStrategy(IntEnum):
    LOW_TO_HIGH = 0
    HIGH_TO_LOW = 1


class InPlaceSortingAlgorithm:

    def __init__(self, name: str, complexity: str):
        self.name = name
        self.complexity = complexity

    def timed_sort(self, sortable: list[int]) -> float:
        start_time = perf_counter()
        self.sort(sortable)
        end_time = perf_counter()
        return end_time - start_time

    def sort(self, sortable: list[int]):
        raise NotImplemented


class OutOfPlaceSortingAlgorithm:

    def __init__(self, name: str, complexity: str):
        self.name = name
        self.complexity = complexity

    def timed_sort(self, sortable: list[int]) -> (list[int], float):
        start_time = perf_counter()
        solution = self.sort(sortable)
        end_time = perf_counter()
        return solution, end_time - start_time

    def sort(self, sortable: list[int]) -> list[int]:
        raise NotImplemented


class InsertionSort(InPlaceSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy):
        super().__init__(self.__class__.__name__, "O(n^2)")
        self.sorting_strategy = sorting_strategy

    def sort(self, sortable: list[int]):
        for i in range(1, len(sortable)):
            value = sortable[i]
            j = i
            while self._sorting_condition(sortable, j, value):
                sortable[j] = sortable[j - 1]
                j = j - 1
            sortable[j] = value

    def _sorting_condition(self, sortable: list[int], j: int, value: int) -> bool:
        if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
            return (j > 0) and (sortable[j - 1] > value)
        if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
            return (j > 0) and (sortable[j - 1] < value)


class MergeSort(OutOfPlaceSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy):
        super().__init__(self.__class__.__name__, "O(log(n))")
        self.sorting_strategy = sorting_strategy

    def sort(self, sortable: list[int]) -> list[int]:
        if len(sortable) <= 1:
            return sortable
        else:
            split = round(len(sortable) / 2)
            left = self.sort(sortable[0:split])
            right = self.sort(sortable[split:len(sortable)])
            return self._merge(left, right)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        merged = []
        while left and right:
            if self._sorting_condition(left, right):
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        return merged

    def _sorting_condition(self, left: list[int], right: list[int]) -> bool:
        if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
            return left[0] <= right[0]
        if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
            return left[0] >= right[0]