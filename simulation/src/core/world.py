"""
MicroBot System - Simulation World
----------------------------------
Defines the 2D environment in which bots move.
"""

from __future__ import annotations


class World:
    """
    Represents the simulation environment.

    The world currently provides:
    - width
    - height
    - padding
    """

    def __init__(self, width: int, height: int, padding: int = 0) -> None:
        self.width = width
        self.height = height
        self.padding = padding

    def usable_width(self) -> int:
        return self.width - 2 * self.padding

    def usable_height(self) -> int:
        return self.height - 2 * self.padding
