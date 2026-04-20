"""
MicroBot System - Bot Entity
----------------------------
Defines the basic simulated node used in the swarm system.
"""

from __future__ import annotations

import math
import random


class Bot:
    """
    Represents a single MicroBot node inside the 2D simulation space.

    Each bot has:
    - an identifier
    - a position
    - a velocity
    - a visible radius
    - a maximum allowed speed
    """

    def __init__(
        self,
        bot_id: int,
        x: float,
        y: float,
        radius: int,
        max_speed: float,
    ) -> None:
        self.bot_id = bot_id
        self.x = x
        self.y = y
        self.radius = radius
        self.max_speed = max_speed

        self.vx = random.uniform(-1.0, 1.0)
        self.vy = random.uniform(-1.0, 1.0)

        self.state = "active"

    def distance_to(self, other: "Bot") -> float:
        """
        Returns the Euclidean distance to another bot.
        """
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx * dx + dy * dy)

    def speed(self) -> float:
        """
        Returns the current speed magnitude.
        """
        return math.sqrt(self.vx * self.vx + self.vy * self.vy)

    def limit_speed(self) -> None:
        """
        Ensures that the bot velocity does not exceed max_speed.
        """
        current_speed = self.speed()

        if current_speed > self.max_speed and current_speed > 0:
            scale = self.max_speed / current_speed
            self.vx *= scale
            self.vy *= scale

    def update_position(self) -> None:
        """
        Updates the position using the current velocity.
        """
        self.x += self.vx
        self.y += self.vy

    def bounce_on_bounds(self, width: int, height: int) -> None:
        """
        Reflects the bot on simulation boundaries.
        """
        if self.x <= self.radius:
            self.x = self.radius
            self.vx *= -1

        if self.x >= width - self.radius:
            self.x = width - self.radius
            self.vx *= -1

        if self.y <= self.radius:
            self.y = self.radius
            self.vy *= -1

        if self.y >= height - self.radius:
            self.y = height - self.radius
            self.vy *= -1

    def apply_force(self, fx: float, fy: float) -> None:
        """
        Applies a velocity adjustment to the bot.
        """
        self.vx += fx
        self.vy += fy

    def position_tuple(self) -> tuple[int, int]:
        """
        Returns the integer position tuple for rendering.
        """
        return int(self.x), int(self.y)
