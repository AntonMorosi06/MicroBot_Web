import sys
import pygame

from config import *
from swarm.simulation import SwarmSimulation


def draw_text(screen, font, text, x, y):
    rendered = font.render(text, True, TEXT_COLOR)
    screen.blit(rendered, (x, y))


def main():
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    simulation.set_mode(SwarmSimulation.MODE_ALIGNMENT)

                if event.key == pygame.K_2:
                    simulation.set_mode(SwarmSimulation.MODE_FLOCKING)

                if event.key == pygame.K_3:
                    simulation.set_mode(SwarmSimulation.MODE_DISORDER)

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

        draw_text(screen, font, "Modes:", 20, 20)
        draw_text(screen, font, "[1] Alignment", 20, 45)
        draw_text(screen, font, "[2] Flocking", 20, 70)
        draw_text(screen, font, "[3] Disorder", 20, 95)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
