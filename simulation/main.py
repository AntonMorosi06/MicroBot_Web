"""
MicroBot System - Swarm Simulation Entry Point
----------------------------------------------
Runs the visual simulation using pygame.
"""

from __future__ import annotations
import sys
import pygame

from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    BACKGROUND_COLOR,
    NODE_COLOR,
    NEIGHBOR_LINE_COLOR,
    TEXT_COLOR,
    FPS,
    SHOW_NEIGHBOR_LINKS,
    SHOW_INFO_TEXT,
)
from swarm.simulation import SwarmSimulation


def draw_text(screen: pygame.Surface, font: pygame.font.Font, text: str, x: int, y: int) -> None:
    rendered = font.render(text, True, TEXT_COLOR)
    screen.blit(rendered, (x, y))


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    simulation = SwarmSimulation(WINDOW_WIDTH, WINDOW_HEIGHT)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulation.update()

        screen.fill(BACKGROUND_COLOR)

        if SHOW_NEIGHBOR_LINKS:
            for agent in simulation.agents:
                neighbors = simulation.neighbor_map.get(agent.agent_id, [])
                for neighbor in neighbors:
                    pygame.draw.line(
                        screen,
                        NEIGHBOR_LINE_COLOR,
                        (int(agent.x), int(agent.y)),
                        (int(neighbor.x), int(neighbor.y)),
                        1,
                    )

        for agent in simulation.agents:
            pygame.draw.circle(
                screen,
                NODE_COLOR,
                (int(agent.x), int(agent.y)),
                agent.radius,
            )

        if SHOW_INFO_TEXT:
            draw_text(screen, font, "MicroBot Swarm Simulation", 20, 20)
            draw_text(screen, font, f"Agents: {len(simulation.agents)}", 20, 45)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
