from enum import IntEnum
from time import perf_counter, sleep
import pygame.draw


class SortingStrategy(IntEnum):
    LOW_TO_HIGH = 0
    HIGH_TO_LOW = 1


class DrawableSortingAlgorithm:

    def __init__(self, sortable: list[int], name: str, complexity: str, display):
        self.sortable = sortable
        self.name = name
        self.complexity = complexity
        self.display = display
        self.width = display.get_size()[0]
        self.height = display.get_size()[1]
        self.color_green = (0, 128, 0)
        self.color_orange = (240, 134, 48)
        self.color_white = (255, 255, 255)
        self.display_color = (0, 0, 0)

    def draw(self, **kwargs) -> None:
        raise NotImplemented

    def sort(self, **kwargs) -> list[int]:
        raise NotImplemented

    def change_sortable(self, sortable: list[int]):
        self.sortable = sortable

    def timed_sort(self) -> tuple[list[int], float]:
        start_time = perf_counter()
        solution = self.sort(sortable=self.sortable)
        end_time = perf_counter()
        return solution, end_time - start_time

    def _reset_display(self):
        self.display.fill(self.display_color)


class InsertionSort(DrawableSortingAlgorithm):

    def __init__(self, sortable: list[int], sorting_strategy: SortingStrategy, display):
        super().__init__(sortable, self.__class__.__name__, "O(n^2)", display)
        self.sorting_strategy = sorting_strategy

    def draw(self, current_index: int = -1, changed_position: int = -1) -> None:
        if self.sortable:
            self._reset_display()
            normalized_sortable = self._normalize()
            line_width = round(self.width / len(self.sortable))
            for i, e in enumerate(normalized_sortable):
                if i == current_index:
                    pygame.draw.rect(self.display, self.color_green, (i * line_width, 0, line_width, e))
                elif i == changed_position:
                    pygame.draw.rect(self.display, self.color_orange, (i * line_width, 0, line_width, e))
                else:
                    pygame.draw.rect(self.display, self.color_white, (i * line_width, 0, line_width, e))
            pygame.display.update()

    def sort(self, **kwargs) -> list[int]:
        for i in range(1, len(self.sortable)):
            value = self.sortable[i]
            j = i
            while self._sorting_condition(j, value):
                self.sortable[j] = self.sortable[j - 1]
                j = j - 1
                self.draw(i, j)
            self.sortable[j] = value
        return self.sortable

    def _normalize(self) -> list[int]:
        normalized_sortable = []
        for e in self.sortable:
            normalized_e = self.height * (e / max(self.sortable))
            normalized_sortable.append(normalized_e)
        return normalized_sortable

    def _sorting_condition(self, i: int, value: int) -> bool:
        if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
            return (i > 0) and (self.sortable[i - 1] > value)
        if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
            return (i > 0) and (self.sortable[i - 1] < value)


class MergeSort(DrawableSortingAlgorithm):

    def __init__(self, sortable: list[int], sorting_strategy: SortingStrategy, display):
        super().__init__(sortable, self.__class__.__name__, "O(log(n))", display)
        self.sorting_strategy = sorting_strategy

    def draw(self, **kwargs) -> None:
        pass

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
