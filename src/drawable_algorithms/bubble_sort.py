from sorting_strategy import SortingStrategy
from drawable_algorithm import (
    DrawableSortingAlgorithm,
    Iterator,
    draw,
    display,
    sleep,
)


class BubbleSort(DrawableSortingAlgorithm):

    def __init__(self, sorting_strategy: SortingStrategy, py_display):
        super().__init__(self.__class__.__name__, "O(n^2)", py_display)
        self.sorting_strategy = sorting_strategy
        self.speed = 0

    def _sort(self, sortable: list[int], **kwargs) -> Iterator:
        for i in range(len(sortable), 2, -1):
            for j in range(0, i - 1):
                if sortable[j] > sortable[j + 1]:
                    yield {"current_value": i, "compared_value": j}
                    value = sortable[j]
                    sortable[j] = sortable[j + 1]
                    sortable[j + 1] = value

    def _draw(self, sortable: list[int], current_value: int = -1, compared_value: int = -1) -> None:
        self._reset_display()
        if sortable:
            normalized_sortable = self._normalize(sortable)
            line_width = self.width / len(normalized_sortable)
            for i, e in enumerate(normalized_sortable):
                if i == current_value:
                    draw.rect(self.display, self.color_red, (i * line_width, 0, line_width, e))
                elif i == compared_value:
                    draw.rect(self.display, self.color_green, (i * line_width, 0, line_width, e))
                else:
                    draw.rect(self.display, self.color_white, (i * line_width, 0, line_width, e))
            display.update()
            sleep(self.speed)
