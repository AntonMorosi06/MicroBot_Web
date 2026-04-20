"""
MicroBot System - Simulation Entry Point
----------------------------------------
Launches the MicroBot swarm simulation.
"""

from __future__ import annotations

import sys
import pygame

from config.settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    FPS,
)
from src.core.app import SimulationApp


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    app = SimulationApp()

    running = True
    while running:
        fps_value = clock.get_fps()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                app.handle_keydown(event.key)

        app.update()
        app.draw(screen, fps_value)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
