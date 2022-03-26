from sorting_strategy import SortingStrategy
from drawable_algorithm import (
    DrawableSortingAlgorithm,
    Iterator,
)


class InsertionSort(DrawableSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy, py_display):
        super().__init__(self.__class__.__name__, "O(n^2)", 0, py_display)
        self.sorting_strategy = sorting_strategy

    def _sort(self, sortable: list[int], **kwargs) -> Iterator:
        for i in range(0, len(sortable)):
            value = sortable[i]
            j = i
            while self._sorting_condition(sortable, j, value):
                yield {"current_value1": i, "compared_value1": j}
                sortable[j] = sortable[j - 1]
                j = j - 1
            sortable[j] = value

    def _sorting_condition(self, sortable: list[int], i: int, value: int) -> bool:
        if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
            return (i > 0) and (sortable[i - 1] > value)
        if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
            return (i > 0) and (sortable[i - 1] < value)
