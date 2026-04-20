"""
MicroBot System - Swarm Metrics
-------------------------------
Provides basic system-level metrics for the simulation.
"""

from __future__ import annotations

import math
from typing import List, Dict

from src.entities.bot import Bot


def compute_average_speed(bots: List[Bot]) -> float:
    """
    Returns the average speed magnitude across all bots.
    """
    if not bots:
        return 0.0

    total_speed = sum(bot.speed() for bot in bots)
    return total_speed / len(bots)


def compute_average_neighbors(neighbor_map: Dict[int, List[Bot]]) -> float:
    """
    Returns the average number of neighbors per bot.
    """
    if not neighbor_map:
        return 0.0

    total_neighbors = sum(len(neighbors) for neighbors in neighbor_map.values())
    return total_neighbors / len(neighbor_map)


def compute_center_of_mass(bots: List[Bot]) -> tuple[float, float]:
    """
    Returns the center of mass of the swarm.
    """
    if not bots:
        return 0.0, 0.0

    avg_x = sum(bot.x for bot in bots) / len(bots)
    avg_y = sum(bot.y for bot in bots) / len(bots)
    return avg_x, avg_y


def compute_coherence(bots: List[Bot]) -> float:
    """
    Estimates directional coherence based on bot velocity alignment.

    Returns a normalized value between 0.0 and 1.0.
    """
    if not bots:
        return 0.0

    sum_vx = sum(bot.vx for bot in bots)
    sum_vy = sum(bot.vy for bot in bots)

    resultant_magnitude = math.sqrt(sum_vx * sum_vx + sum_vy * sum_vy)
    total_speed = sum(bot.speed() for bot in bots)

    if total_speed == 0:
        return 0.0

    coherence = resultant_magnitude / total_speed
    return max(0.0, min(1.0, coherence))
