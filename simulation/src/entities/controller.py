"""
MicroBot System - Simulation Controller
---------------------------------------
Defines a lightweight controller for simulation modes.
"""

from __future__ import annotations


class SimulationController:
    """
    Stores and manages the currently selected simulation mode.
    """

    MODE_ALIGNMENT = "alignment"
    MODE_FLOCKING = "flocking"
    MODE_DISORDER = "disorder"

    def __init__(self) -> None:
        self.current_mode = self.MODE_FLOCKING

    def set_mode(self, mode: str) -> None:
        """
        Sets the active simulation mode.
        """
        self.current_mode = mode

    def get_mode(self) -> str:
        """
        Returns the current simulation mode.
        """
        return self.current_mode
