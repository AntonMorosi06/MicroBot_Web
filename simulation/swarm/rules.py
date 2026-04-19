"""
Defines local interaction rules for swarm agents.
"""

from __future__ import annotations
from typing import List

from swarm.agent import Agent


def get_neighbors(agent: Agent, agents: List[Agent], detection_radius: float) -> List[Agent]:
    """
    Returns the list of neighbors within detection radius.
    """
    neighbors = []
    for other in agents:
        if other.agent_id == agent.agent_id:
            continue
        if agent.distance_to(other) <= detection_radius:
            neighbors.append(other)
    return neighbors


def apply_alignment(agent: Agent, neighbors: List[Agent], strength: float = 0.02) -> None:
    """
    Applies a simple alignment rule: the agent slightly adjusts
    its velocity toward the average velocity of nearby neighbors.
    """
    if not neighbors:
        return

    avg_vx = sum(n.vx for n in neighbors) / len(neighbors)
    avg_vy = sum(n.vy for n in neighbors) / len(neighbors)

    agent.vx += (avg_vx - agent.vx) * strength
    agent.vy += (avg_vy - agent.vy) * strength
