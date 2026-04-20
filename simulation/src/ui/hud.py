"""
MicroBot System - HUD
---------------------
Provides simple on-screen information for the simulation.
"""

from __future__ import annotations

import pygame

from config.settings import TEXT_COLOR


class HUD:
    """
    Simple heads-up display for simulation metadata.
    """

    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial", 18)

    def draw_line(
        self,
        surface: pygame.Surface,
        text: str,
        x: int,
        y: int,
    ) -> None:
        rendered = self.font.render(text, True, TEXT_COLOR)
        surface.blit(rendered, (x, y))

    def draw(
        self,
        surface: pygame.Surface,
        mode_name: str,
        bot_count: int,
        fps_value: float,
    ) -> None:
        self.draw_line(surface, "MicroBot System - Swarm Simulation", 20, 20)
        self.draw_line(surface, f"Mode: {mode_name}", 20, 48)
        self.draw_line(surface, f"Bots: {bot_count}", 20, 76)
        self.draw_line(surface, f"FPS: {int(fps_value)}", 20, 104)

        self.draw_line(surface, "[1] Alignment", 20, 148)
        self.draw_line(surface, "[2] Flocking", 20, 176)
        self.draw_line(surface, "[3] Disorder", 20, 204)
        self.draw_line(surface, "[R] Reset", 20, 232)
