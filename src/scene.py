import pygame
from time import sleep, perf_counter


class Scene(object):

    def __init__(self, width: int, height: int):
        pygame.init()
        self._width = width
        self._height = height
        self._height_padding = (self._height / 10)
        self._color_green = (0, 128, 0)
        self._color_red = (255, 0, 0)
        self._color_white = (255, 255, 255)
        self._display_color = (0, 0, 0)
        self._display = pygame.display.set_mode((self._width, self._height))
        self._font = pygame.font.Font('freesansbold.ttf', int(self._height/25))

    def draw(self, sortable: list[int], current_value1: int = -1, current_value2: int = -1,
             compared_value1: int = -1, compared_value2: int = -1, speed: float = 0, name: str = "",
             complexity: str = "", start_time: float = 0, finished: bool = False, animation_delay: float = 0) -> None:
        self._draw_text(f"Name: {name}, Complexity: {complexity} Time: {round((perf_counter() - start_time), 4)}")
        if sortable:
            normalized_sortable = self._normalize(sortable)
            step_size = self._width / len(normalized_sortable)
            line_width = (self._width - (self._width / 5)) / len(normalized_sortable)
            for i, e in enumerate(normalized_sortable):
                if finished:
                    pygame.draw.rect(self._display, self._color_green, (i * step_size, 0, line_width, e))
                    pygame.display.update()
                    sleep(animation_delay)
                    continue
                elif i == current_value1 or i == current_value2:
                    pygame.draw.rect(self._display, self._color_red, (i * step_size, 0, line_width, e))
                elif i == compared_value1 or i == compared_value2:
                    pygame.draw.rect(self._display, self._color_green, (i * step_size, 0, line_width, e))
                else:
                    pygame.draw.rect(self._display, self._color_white, (i * step_size, 0, line_width, e))
            pygame.display.update()
            self._reset_display()
            sleep(speed)

    def _draw_text(self, text: str):
        render_text = self._font.render(text, True, self._color_white)
        self._display.blit(render_text, (0, self._height - (self._height_padding / 2)))

    def _normalize(self, sortable: list[int]) -> list[float]:
        normalized_sortable = []
        for e in sortable:
            normalized_e = (self._height - self._height_padding) * (e / max(sortable))
            normalized_sortable.append(normalized_e)
        return normalized_sortable

    def _reset_display(self) -> None:
        self._display.fill(self._display_color)
