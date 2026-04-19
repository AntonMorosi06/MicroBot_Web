"""
Defines the MicroBot agent model used in the simulation.
"""

from __future__ import annotations
import math
import random


class Agent:
    """
    Represents a single swarm node (MicroBot) in the simulation.
    """

    def __init__(
        self,
        agent_id: int,
        x: float,
        y: float,
        radius: int,
        max_speed: float,
    ) -> None:
        self.agent_id = agent_id
        self.x = x
        self.y = y
        self.radius = radius
        self.max_speed = max_speed

        self.vx = random.uniform(-1.0, 1.0)
        self.vy = random.uniform(-1.0, 1.0)

    def distance_to(self, other: "Agent") -> float:
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx * dx + dy * dy)

    def limit_speed(self) -> None:
        speed = math.sqrt(self.vx * self.vx + self.vy * self.vy)
        if speed > self.max_speed and speed > 0:
            scale = self.max_speed / speed
            self.vx *= scale
            self.vy *= scale

    def update_position(self) -> None:
        self.x += self.vx
        self.y += self.vy

    def bounce_on_bounds(self, width: int, height: int) -> None:
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
