from sorting_strategy import SortingStrategy
from drawable_algorithm import (
    DrawableSortingAlgorithm,
    Iterator,
)


class BubbleSort(DrawableSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy, py_display):
        super().__init__(self.__class__.__name__, "O(n^2)", 0, py_display)
        self.sorting_strategy = sorting_strategy

    def _sort(self, sortable: list[int], **kwargs) -> Iterator:
        for i in range(len(sortable), 2, -1):
            for j in range(0, i - 1):
                if self._sorting_condition(sortable, j):
                    yield {"current_value1": i, "compared_value1": j}
                    sortable[j], sortable[j + 1] = sortable[j + 1], sortable[j]

    def _sorting_condition(self, sortable: list[int], j: int) -> bool:
        if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
            return sortable[j] > sortable[j + 1]
        if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
            return sortable[j] < sortable[j + 1]
