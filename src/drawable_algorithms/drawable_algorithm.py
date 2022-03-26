from time import perf_counter, sleep
from typing import Iterator
from pygame import draw, display


class DrawableSortingAlgorithm:

    def __init__(self, name: str, complexity: str, speed: float, py_display: display):
        self.name = name
        self.complexity = complexity
        self.speed = speed
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

    def _draw(self, sortable: list[int], current_value1: int = -1, current_value2: int = -1,
              compared_value1: int = -1, compared_value2: int = -1) -> None:
        self._reset_display()
        if sortable:
            normalized_sortable = self._normalize(sortable)
            line_width = self.width / len(normalized_sortable)
            for i, e in enumerate(normalized_sortable):
                if i == current_value1 or i == current_value2:
                    draw.rect(self.display, self.color_red, (i * line_width, 0, line_width, e))
                elif i == compared_value1 or i == compared_value2:
                    draw.rect(self.display, self.color_green, (i * line_width, 0, line_width, e))
                else:
                    draw.rect(self.display, self.color_white, (i * line_width, 0, line_width, e))
            display.update()
            sleep(self.speed)

    def _sort(self, sortable: list[int], **kwargs) -> Iterator:
        raise NotImplemented
