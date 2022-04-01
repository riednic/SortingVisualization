from sorting_strategy import SortingStrategy
from drawable_algorithm import (
    DrawableSortingAlgorithm,
    Iterator,
)


class MergeSort(DrawableSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy, py_display):
        super().__init__(self.__class__.__name__, "O(n*log(n))", 0, py_display)
        self.sorting_strategy = sorting_strategy
        self.speed = 0

    def _sort(self, sortable: list[int], left: int = 0, right: int = -1) -> Iterator:
        if right == -1:
            right = len(sortable)
        if left < right:
            split = int((left + right) / 2)
            yield from self._sort(sortable, left, split)
            yield from self._sort(sortable, split + 1, right)
            yield from self._merge(sortable, left, split, right)

    def _merge(self, sortable: list[int], left: int, split: int, right: int) -> Iterator:
        left_sortable = sortable[left:split + 1]
        right_sortable = sortable[split + 1:right + 1]
        left_index = 0
        right_index = 0
        k = left
        while left_index < len(left_sortable) and right_index < len(right_sortable):
            yield {"current_value1": left, "current_value2": right,
                   "compared_value1": left + left_index, "compared_value2": split + right_index}
            if self._sorting_condition(left_sortable, left_index, right_sortable, right_index):
                sortable[k] = left_sortable[left_index]
                left_index += 1
            else:
                sortable[k] = right_sortable[right_index]
                right_index += 1
            k += 1
        while left_index < len(left_sortable):
            sortable[k] = left_sortable[left_index]
            left_index += 1
            k += 1
        while right_index < len(right_sortable):
            sortable[k] = right_sortable[right_index]
            right_index += 1
            k += 1

    def _sorting_condition(self, left_sortable: list[int], left_index: int,
                           right_sortable: list[int], right_index: int) -> bool:
        if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
            return left_sortable[left_index] < right_sortable[right_index]
        if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
            return left_sortable[left_index] > right_sortable[right_index]
