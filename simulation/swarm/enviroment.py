"""
Defines the simulation environment.
"""


class Environment:
    """
    Represents the 2D environment where swarm agents move.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
