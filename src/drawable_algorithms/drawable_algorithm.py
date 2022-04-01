from time import perf_counter
from typing import Iterator
from scene import Scene
from time import sleep


class DrawableSortingAlgorithm:

    def __init__(self, name: str, complexity: str, speed: float, scene: Scene):
        self._name = name
        self._complexity = complexity
        self._speed = speed
        self._scene = scene

    def draw_sorting_algorithm(self, sortable: list[int]):
        start_time = perf_counter()
        alg_it = self._sort(sortable)
        try:
            while True:
                kwargs = next(alg_it)
                self._scene.draw(sortable, **kwargs, speed=self._speed, name=self._name,
                                 complexity=self._complexity, start_time=start_time)
        except StopIteration:
            self._scene.draw(sortable, -1, -1, -1, -1, speed=self._speed, name=self._name,
                             complexity=self._complexity, start_time=start_time, finished=True,
                             animation_delay=0.0001)
            sleep(1)

    def _sort(self, sortable: list[int], **kwargs) -> Iterator:
        raise NotImplemented
