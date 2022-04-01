from sorting_strategy import SortingStrategy
from drawable_algorithm import (
    DrawableSortingAlgorithm,
    Iterator,
)


class QuickSort(DrawableSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy, py_display):
        super().__init__(self.__class__.__name__, "O(n*log(n))", 0, py_display)
        self.sorting_strategy = sorting_strategy

    def _sort(self, sortable: list[int], left: int = 0, right: int = -1) -> Iterator:
        if right == -1:
            right = len(sortable) - 1
        if left < right:
            split = self._split(sortable, left, right)
            yield {"current_value1": left, "current_value2": right,
                   "compared_value1": split, "compared_value2": -1}
            yield from self._sort(sortable, left, split)
            yield from self._sort(sortable, split + 1, right)

    def _split(self, sortable: list[int], left: int, right: int) -> int:
        i = left
        j = right
        pivot = sortable[i]

        while i < j:
            if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
                if sortable[i] < pivot:
                    i += 1

                if sortable[j] > pivot:
                    j -= 1

            if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
                if sortable[i] > pivot:
                    i += 1

                if sortable[j] < pivot:
                    j -= 1

            if i >= j:
                return i
            else:
                sortable[i], sortable[j] = sortable[j], sortable[i]

