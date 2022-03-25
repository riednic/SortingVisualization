from sorting_strategy import SortingStrategy
from drawable_algorithm import (
    DrawableSortingAlgorithm,
    Iterator,
    draw,
    display,
    sleep,
)


class MergeSort(DrawableSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy, py_display):
        super().__init__(self.__class__.__name__, "O(log(n))", py_display)
        self.sorting_strategy = sorting_strategy
        self.speed = 0

    def _draw(self, sortable: list[int], left_i: int = -1, split_j: int = -1, left: int = -1, right: int = -1) -> None:
        self._reset_display()
        if sortable:
            normalized_sortable = self._normalize(sortable)
            line_width = self.width / len(normalized_sortable)
            for i, e in enumerate(normalized_sortable):
                if i == left or i == right:
                    draw.rect(self.display, self.color_red, (i * line_width, 0, line_width, e))
                elif i == left_i or i == split_j:
                    draw.rect(self.display, self.color_green, (i * line_width, 0, line_width, e))
                else:
                    draw.rect(self.display, self.color_white, (i * line_width, 0, line_width, e))
            display.update()
            sleep(self.speed)

    def _sort(self, sortable: list[int], left: int = -1, right: int = -1) -> Iterator:
        if left == -1:
            left = 0
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
        i = 0
        j = 0
        k = left
        while i < len(left_sortable) and j < len(right_sortable):
            yield {"left_i": left + i, "split_j": split + j, "left": left, "right": right}
            if left_sortable[i] < right_sortable[j]:
                sortable[k] = left_sortable[i]
                i += 1
            else:
                sortable[k] = right_sortable[j]
                j += 1
            k += 1
        while i < len(left_sortable):
            sortable[k] = left_sortable[i]
            i += 1
            k += 1
        while j < len(right_sortable):
            sortable[k] = right_sortable[j]
            j += 1
            k += 1

    def _sorting_condition(self, left: list[int], right: list[int]) -> bool:
        if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
            return left[0] <= right[0]
        if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
            return left[0] >= right[0]
