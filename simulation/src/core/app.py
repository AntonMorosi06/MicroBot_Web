"""
MicroBot System - Simulation Application Core
---------------------------------------------
Coordinates world state, bots, interaction rules, metrics, and rendering.
"""

from __future__ import annotations

import random
import pygame

from config.settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    BACKGROUND_COLOR,
    BOT_COLOR,
    LINK_COLOR,
    ACCENT_COLOR,
    SHOW_LINKS,
    SHOW_HUD,
    SHOW_CENTER_OF_MASS,
    WORLD_PADDING,
    NUM_BOTS,
    BOT_RADIUS,
    BOT_MAX_SPEED,
    BOT_DETECTION_RADIUS,
    BOT_SEPARATION_DISTANCE,
    ALIGNMENT_STRENGTH,
    COHESION_STRENGTH,
    SEPARATION_STRENGTH,
)
from src.core.world import World
from src.entities.bot import Bot
from src.entities.controller import SimulationController
from src.systems.formations import (
    get_neighbors,
    apply_alignment,
    apply_cohesion,
    apply_separation,
)
from src.systems.metrics import (
    compute_average_speed,
    compute_average_neighbors,
    compute_center_of_mass,
    compute_coherence,
)
from src.ui.hud import HUD


class SimulationApp:
    """
    Main coordinator of the MicroBot swarm simulation.
    """

    def __init__(self) -> None:
        self.world = World(WINDOW_WIDTH, WINDOW_HEIGHT, WORLD_PADDING)
        self.controller = SimulationController()
        self.hud = HUD()

        self.bots: list[Bot] = []
        self.neighbor_map: dict[int, list[Bot]] = {}

        self.average_speed = 0.0
        self.average_neighbors = 0.0
        self.coherence = 0.0
        self.center_of_mass = (0.0, 0.0)

        self.reset()

    def reset(self) -> None:
        """
        Resets the simulation with a new random bot distribution.
        """
        self.bots = []

        for i in range(NUM_BOTS):
            x = random.uniform(
                self.world.padding,
                self.world.width - self.world.padding,
            )
            y = random.uniform(
                self.world.padding,
                self.world.height - self.world.padding,
            )

            bot = Bot(
                bot_id=i,
                x=x,
                y=y,
                radius=BOT_RADIUS,
                max_speed=BOT_MAX_SPEED,
            )
            self.bots.append(bot)

        self.neighbor_map = {}
        self.average_speed = 0.0
        self.average_neighbors = 0.0
        self.coherence = 0.0
        self.center_of_mass = (0.0, 0.0)

    def update(self) -> None:
        """
        Updates the state of all bots according to the active mode.
        """
        self.neighbor_map = {}

        for bot in self.bots:
            neighbors = get_neighbors(bot, self.bots, BOT_DETECTION_RADIUS)
            self.neighbor_map[bot.bot_id] = neighbors

            mode = self.controller.get_mode()

            if mode == SimulationController.MODE_ALIGNMENT:
                apply_alignment(bot, neighbors, ALIGNMENT_STRENGTH)

            elif mode == SimulationController.MODE_FLOCKING:
                apply_alignment(bot, neighbors, ALIGNMENT_STRENGTH)
                apply_cohesion(bot, neighbors, COHESION_STRENGTH)
                apply_separation(
                    bot,
                    neighbors,
                    BOT_SEPARATION_DISTANCE,
                    SEPARATION_STRENGTH,
                )

            elif mode == SimulationController.MODE_DISORDER:
                bot.apply_force(
                    random.uniform(-0.2, 0.2),
                    random.uniform(-0.2, 0.2),
                )

            bot.limit_speed()

        for bot in self.bots:
            bot.update_position()
            bot.bounce_on_bounds(self.world.width, self.world.height)

        self.average_speed = compute_average_speed(self.bots)
        self.average_neighbors = compute_average_neighbors(self.neighbor_map)
        self.coherence = compute_coherence(self.bots)
        self.center_of_mass = compute_center_of_mass(self.bots)

    def handle_keydown(self, key: int) -> None:
        """
        Handles keyboard input for simulation control.
        """
        if key == pygame.K_1:
            self.controller.set_mode(SimulationController.MODE_ALIGNMENT)

        elif key == pygame.K_2:
            self.controller.set_mode(SimulationController.MODE_FLOCKING)

        elif key == pygame.K_3:
            self.controller.set_mode(SimulationController.MODE_DISORDER)

        elif key == pygame.K_r:
            self.reset()

    def draw_links(self, surface: pygame.Surface) -> None:
        """
        Draws neighbor links between bots.
        """
        if not SHOW_LINKS:
            return

        for bot in self.bots:
            neighbors = self.neighbor_map.get(bot.bot_id, [])
            for neighbor in neighbors:
                pygame.draw.line(
                    surface,
                    LINK_COLOR,
                    bot.position_tuple(),
                    neighbor.position_tuple(),
                    1,
                )

    def draw_bots(self, surface: pygame.Surface) -> None:
        """
        Draws all bots to the screen.
        """
        for bot in self.bots:
            pygame.draw.circle(
                surface,
                BOT_COLOR,
                bot.position_tuple(),
                bot.radius,
            )

    def draw_center_of_mass(self, surface: pygame.Surface) -> None:
        """
        Draws the estimated center of mass of the swarm.
        """
        if not SHOW_CENTER_OF_MASS:
            return

        x, y = self.center_of_mass
        cx, cy = int(x), int(y)

        pygame.draw.circle(surface, ACCENT_COLOR, (cx, cy), 5)
        pygame.draw.line(surface, ACCENT_COLOR, (cx - 10, cy), (cx + 10, cy), 1)
        pygame.draw.line(surface, ACCENT_COLOR, (cx, cy - 10), (cx, cy + 10), 1)

    def draw(self, surface: pygame.Surface, fps_value: float) -> None:
        """
        Renders the current simulation state.
        """
        surface.fill(BACKGROUND_COLOR)

        self.draw_links(surface)
        self.draw_bots(surface)
        self.draw_center_of_mass(surface)

        if SHOW_HUD:
            self.hud.draw(
                surface=surface,
                mode_name=self.controller.get_mode(),
                bot_count=len(self.bots),
                fps_value=fps_value,
                average_speed=self.average_speed,
                average_neighbors=self.average_neighbors,
                coherence=self.coherence,
            )
