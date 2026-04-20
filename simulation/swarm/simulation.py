"""
Extended simulation engine with multiple behavior modes.
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
from swarm.rules import (
    get_neighbors,
    apply_alignment,
    apply_cohesion,
    apply_separation,
)


class SwarmSimulation:

    MODE_ALIGNMENT = 0
    MODE_FLOCKING = 1
    MODE_DISORDER = 2

    def __init__(self, width: int, height: int) -> None:
        self.environment = Environment(width, height)
        self.agents: List[Agent] = self._create_agents()
        self.neighbor_map: Dict[int, List[Agent]] = {}

        self.mode = self.MODE_FLOCKING

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

    def set_mode(self, mode: int) -> None:
        self.mode = mode

    def update(self) -> None:
        self.neighbor_map = {}

        for agent in self.agents:
            neighbors = get_neighbors(agent, self.agents, AGENT_DETECTION_RADIUS)
            self.neighbor_map[agent.agent_id] = neighbors

            if self.mode == self.MODE_ALIGNMENT:
                apply_alignment(agent, neighbors)

            elif self.mode == self.MODE_FLOCKING:
                apply_alignment(agent, neighbors)
                apply_cohesion(agent, neighbors)
                apply_separation(agent, neighbors)

            elif self.mode == self.MODE_DISORDER:
                agent.vx += random.uniform(-0.2, 0.2)
                agent.vy += random.uniform(-0.2, 0.2)

            agent.limit_speed()

        for agent in self.agents:
            agent.update_position()
            agent.bounce_on_bounds(
                self.environment.width,
                self.environment.height,
            )
