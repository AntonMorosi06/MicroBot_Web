"""
MicroBot System - Formation Rules
---------------------------------
Implements local interaction rules for swarm behavior.
"""

from __future__ import annotations

import math
from typing import List

from src.entities.bot import Bot


def get_neighbors(bot: Bot, bots: List[Bot], detection_radius: float) -> List[Bot]:
    """
    Returns the list of nearby bots inside the detection radius.
    """
    neighbors: List[Bot] = []

    for other in bots:
        if other.bot_id == bot.bot_id:
            continue
        if bot.distance_to(other) <= detection_radius:
            neighbors.append(other)

    return neighbors


def apply_alignment(bot: Bot, neighbors: List[Bot], strength: float) -> None:
    """
    Adjusts velocity toward the average velocity of nearby bots.
    """
    if not neighbors:
        return

    avg_vx = sum(n.vx for n in neighbors) / len(neighbors)
    avg_vy = sum(n.vy for n in neighbors) / len(neighbors)

    fx = (avg_vx - bot.vx) * strength
    fy = (avg_vy - bot.vy) * strength

    bot.apply_force(fx, fy)


def apply_cohesion(bot: Bot, neighbors: List[Bot], strength: float) -> None:
    """
    Adjusts velocity toward the local center of mass.
    """
    if not neighbors:
        return

    center_x = sum(n.x for n in neighbors) / len(neighbors)
    center_y = sum(n.y for n in neighbors) / len(neighbors)

    fx = (center_x - bot.x) * strength
    fy = (center_y - bot.y) * strength

    bot.apply_force(fx, fy)


def apply_separation(
    bot: Bot,
    neighbors: List[Bot],
    desired_distance: float,
    strength: float,
) -> None:
    """
    Pushes the bot away from neighbors that are too close.
    """
    move_x = 0.0
    move_y = 0.0

    for neighbor in neighbors:
        dx = bot.x - neighbor.x
        dy = bot.y - neighbor.y
        dist = math.sqrt(dx * dx + dy * dy)

        if 0 < dist < desired_distance:
            move_x += dx / dist
            move_y += dy / dist

    bot.apply_force(move_x * strength, move_y * strength)
