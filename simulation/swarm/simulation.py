"""
Main simulation engine for the MicroBot swarm system.
"""

from __future__ import annotations
import random
from typing import List, Dict

from config import (
    NUM_AGENTS,
    AGENT_RADIUS,
    AGENT_MAX_SPEED,
    AGENT_DETECTION_RADIUS,
    SPAWN_MARGIN,
)
from swarm.agent import Agent
from swarm.environment import Environment
from swarm.rules import get_neighbors, apply_alignment


class SwarmSimulation:
    """
    Coordinates environment state, agents, and update logic.
    """

    def __init__(self, width: int, height: int) -> None:
        self.environment = Environment(width, height)
        self.agents: List[Agent] = self._create_agents()
        self.neighbor_map: Dict[int, List[Agent]] = {}

    def _create_agents(self) -> List[Agent]:
        agents: List[Agent] = []

        for i in range(NUM_AGENTS):
            x = random.uniform(SPAWN_MARGIN, self.environment.width - SPAWN_MARGIN)
            y = random.uniform(SPAWN_MARGIN, self.environment.height - SPAWN_MARGIN)

            agent = Agent(
                agent_id=i,
                x=x,
                y=y,
                radius=AGENT_RADIUS,
                max_speed=AGENT_MAX_SPEED,
            )
            agents.append(agent)

        return agents

    def update(self) -> None:
        self.neighbor_map = {}

        for agent in self.agents:
            neighbors = get_neighbors(agent, self.agents, AGENT_DETECTION_RADIUS)
            self.neighbor_map[agent.agent_id] = neighbors

            apply_alignment(agent, neighbors)
            agent.limit_speed()

        for agent in self.agents:
            agent.update_position()
            agent.bounce_on_bounds(
                self.environment.width,
                self.environment.height,
            )

    def get_neighbor_count(self, agent_id: int) -> int:
        return len(self.neighbor_map.get(agent_id, []))
