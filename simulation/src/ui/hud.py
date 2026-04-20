"""
MicroBot System - HUD
---------------------
Provides on-screen system information for the simulation.
"""

from __future__ import annotations

import pygame

from config.settings import TEXT_COLOR, ACCENT_COLOR


class HUD:
    """
    Heads-up display for simulation metadata and swarm metrics.
    """

    def __init__(self) -> None:
        self.title_font = pygame.font.SysFont("Arial", 20, bold=True)
        self.body_font = pygame.font.SysFont("Arial", 17)

    def draw_line(
        self,
        surface: pygame.Surface,
        text: str,
        x: int,
        y: int,
        color: tuple[int, int, int] = TEXT_COLOR,
        title: bool = False,
    ) -> None:
        font = self.title_font if title else self.body_font
        rendered = font.render(text, True, color)
        surface.blit(rendered, (x, y))

    def draw(
        self,
        surface: pygame.Surface,
        mode_name: str,
        bot_count: int,
        fps_value: float,
        average_speed: float,
        average_neighbors: float,
        coherence: float,
    ) -> None:
        self.draw_line(
            surface,
            "MicroBot System - Swarm Simulation",
            20,
            20,
            color=ACCENT_COLOR,
            title=True,
        )

        self.draw_line(surface, f"Mode: {mode_name}", 20, 56)
        self.draw_line(surface, f"Bots: {bot_count}", 20, 82)
        self.draw_line(surface, f"FPS: {int(fps_value)}", 20, 108)

        self.draw_line(surface, f"Avg speed: {average_speed:.2f}", 20, 148)
        self.draw_line(surface, f"Avg neighbors: {average_neighbors:.2f}", 20, 174)
        self.draw_line(surface, f"Coherence: {coherence * 100:.1f}%", 20, 200)

        self.draw_line(surface, "[1] Alignment", 20, 246)
        self.draw_line(surface, "[2] Flocking", 20, 272)
        self.draw_line(surface, "[3] Disorder", 20, 298)
        self.draw_line(surface, "[R] Reset", 20, 324)
