from time import perf_counter, sleep
from typing import Iterator
from pygame import draw, display


class DrawableSortingAlgorithm:

    def __init__(self, name: str, complexity: str, py_display: display):
        self.name = name
        self.complexity = complexity
        self.display = py_display
        self.width = py_display.get_size()[0]
        self.height = py_display.get_size()[1]
        self.color_green = (0, 128, 0)
        self.color_red = (255, 0, 0)
        self.color_white = (255, 255, 255)
        self.display_color = (0, 0, 0)

    def draw_sorting_algorithm(self, sortable: list[int]):
        alg_it = self._sort(sortable)
        try:
            while True:
                kwargs = next(alg_it)
                self._draw(sortable, **kwargs)
        except StopIteration:
            pass

    def timed_sort(self, sortable: list[int]) -> float:
        start_time = perf_counter()
        self.draw_sorting_algorithm(sortable)
        end_time = perf_counter()
        return end_time - start_time

    def _reset_display(self) -> None:
        self.display.fill(self.display_color)

    def _normalize(self, sortable: list[int]) -> list[int]:
        normalized_sortable = []
        for e in sortable:
            normalized_e = self.height * (e / max(sortable))
            normalized_sortable.append(normalized_e)
        return normalized_sortable

    def _draw(self, sortable: list[int], **kwargs) -> None:
        raise NotImplemented

    def _sort(self, sortable: list[int], **kwargs) -> Iterator:
        raise NotImplemented
