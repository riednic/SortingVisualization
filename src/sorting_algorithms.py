from enum import IntEnum
from time import perf_counter, sleep
import pygame.draw


class SortingStrategy(IntEnum):
    LOW_TO_HIGH = 0
    HIGH_TO_LOW = 1


class InPlaceSortingAlgorithm:

    def __init__(self, name: str, complexity: str, display):
        self.display = display
        self.width = display.get_size()[0]
        self.height = display.get_size()[1]
        self.color_green = (0, 128, 0)
        self.color_orange = (240, 134, 48)
        self.color_white = (255, 255, 255)
        self.display_color = (0, 0, 0)
        self.name = name
        self.complexity = complexity

    def draw(self, sortable: list[int], current_index: int, changed_position: int = -1):
        if sortable:
            self._reset_display()
            line_width = round(self.width / len(sortable))
            for i, e in enumerate(sortable):
                line_height = (e / self.height)*2.5
                if i == current_index:
                    pygame.draw.rect(self.display, self.color_green, (i * line_width, 0, line_width, line_height))
                elif i == changed_position:
                    pygame.draw.rect(self.display, self.color_orange, (i * line_width, 0, line_width, line_height))
                else:
                    pygame.draw.rect(self.display, self.color_white, (i * line_width, 0, line_width, line_height))
            pygame.display.update()

    def sort(self, sortable: list[int]):
        raise NotImplemented

    def timed_sort(self, sortable: list[int]) -> float:
        start_time = perf_counter()
        self.sort(sortable)
        end_time = perf_counter()
        return end_time - start_time

    def _reset_display(self):
        self.display.fill(self.display_color)


class OutOfPlaceSortingAlgorithm:

    def __init__(self, name: str, complexity: str, display):
        self.display = display
        self.width = display.get_size()[0]
        self.height = display.get_size()[1]
        self.color_green = (0, 128, 0)
        self.color_orange = (240, 134, 48)
        self.color_white = (255, 255, 255)
        self.display_color = (0, 0, 0)
        self.name = name
        self.complexity = complexity

    def sort(self, sortable: list[int]) -> list[int]:
        raise NotImplemented

    def timed_sort(self, sortable: list[int]) -> (list[int], float):
        start_time = perf_counter()
        solution = self.sort(sortable)
        end_time = perf_counter()
        return solution, end_time - start_time

    def _reset_display(self):
        self.display.fill(self.display_color)


class InsertionSort(InPlaceSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy, display):
        super().__init__(self.__class__.__name__, "O(n^2)", display)
        self.sorting_strategy = sorting_strategy

    def sort(self, sortable: list[int]):
        for i in range(1, len(sortable)):
            value = sortable[i]
            j = i
            while self._sorting_condition(sortable, j, value):
                sortable[j] = sortable[j - 1]
                j = j - 1
                self.draw(sortable, i, j)
            sortable[j] = value

    def _sorting_condition(self, sortable: list[int], j: int, value: int) -> bool:
        if self.sorting_strategy == SortingStrategy.LOW_TO_HIGH:
            return (j > 0) and (sortable[j - 1] > value)
        if self.sorting_strategy == SortingStrategy.HIGH_TO_LOW:
            return (j > 0) and (sortable[j - 1] < value)


class MergeSort(OutOfPlaceSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy, display):
        super().__init__(self.__class__.__name__, "O(log(n))", display)
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