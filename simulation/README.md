# MicroBot System — Simulation Module

## 1. Overview

The simulation module represents the core logic layer of the MicroBot system.

It implements a multi-agent environment in which individual nodes (agents) interact based on local rules, producing emergent collective behavior.

This module is designed to:

* model swarm dynamics
* validate interaction rules
* provide a controllable and observable environment

The simulation acts as a foundational step before deploying behavior to physical hardware.

---

## 2. Structure

The simulation module is organized as follows:

| File / Module        | Description                            |
| -------------------- | -------------------------------------- |
| main.py              | Entry point for running the simulation |
| config.py            | Global configuration parameters        |
| swarm/agent.py       | Definition of a single node (MicroBot) |
| swarm/environment.py | Simulation space definition            |
| swarm/rules.py       | Local interaction rules                |
| swarm/simulation.py  | Core simulation engine                 |
| utils/               | Helper functions (optional extensions) |

This structure separates responsibilities and supports future extensions.

---

## 3. Concepts

The simulation is based on a multi-agent model.

Each agent:

* has a position and velocity
* interacts only with nearby agents
* updates its state at each time step

Global system behavior is not explicitly defined. It emerges from repeated local interactions.

### Agent Model

| Property          | Description                    |
| ----------------- | ------------------------------ |
| Position (x, y)   | Location in 2D space           |
| Velocity (vx, vy) | Movement direction and speed   |
| Detection Radius  | Range for neighbor interaction |

### Interaction Model

Agents identify nearby neighbors and adjust their behavior accordingly.

The current implementation includes:

| Rule      | Description                             |
| --------- | --------------------------------------- |
| Alignment | Agents adjust velocity toward neighbors |

Additional rules can be added in `rules.py`.

---

## 4. Requirements

The simulation requires Python 3.10 or higher.

Install dependencies using:

```bash
pip install -r requirements.txt
```

The current implementation uses:

* pygame (for visualization)

---

## 5. How to Run

From the `simulation/` directory, run:

```bash
python main.py
```

A window will open displaying the swarm simulation.

---

## 6. Visualization

The simulation provides a real-time visual representation of agents.

| Element      | Description                      |
| ------------ | -------------------------------- |
| Circles      | Represent agents                 |
| Lines        | Represent neighbor relationships |
| Text overlay | Displays system information      |

The visualization is intended for debugging and understanding system behavior.

---

## 7. Execution Model

The simulation follows a discrete update loop:

1. Detect neighbors for each agent
2. Apply local interaction rules
3. Update velocity and limit speed
4. Update positions
5. Render the new state

This loop runs at a fixed frame rate.

---

## 8. Configuration

Simulation parameters are defined in `config.py`.

| Parameter              | Description                   |
| ---------------------- | ----------------------------- |
| NUM_AGENTS             | Number of nodes in the system |
| AGENT_MAX_SPEED        | Maximum velocity              |
| AGENT_DETECTION_RADIUS | Interaction range             |
| WINDOW_WIDTH / HEIGHT  | Simulation space size         |

These parameters can be modified to explore different behaviors.

---

## 9. Extending the Simulation

The system is designed to support additional behaviors and complexity.

Possible extensions include:

| Area          | Extension                                |
| ------------- | ---------------------------------------- |
| Rules         | Cohesion, separation, obstacle avoidance |
| Visualization | Improved rendering and metrics           |
| Interaction   | Keyboard or UI-based controls            |
| Data          | Logging and analysis of system evolution |

All behavioral logic should be added inside `rules.py`.

---

## 10. Limitations

| Area          | Limitation                           |
| ------------- | ------------------------------------ |
| Physics       | Simplified motion model              |
| Communication | No explicit messaging between agents |
| Environment   | No obstacles or dynamic conditions   |
| Scalability   | Limited by rendering performance     |

These limitations are acceptable for a prototype stage.

---

## 11. Role in the System

The simulation module serves as the reference implementation of swarm logic.

| Layer         | Role                         |
| ------------- | ---------------------------- |
| Simulation    | Defines behavior             |
| Web Interface | Visualizes behavior          |
| Hardware      | Executes simplified behavior |

Future versions aim to align these layers more closely.

---

## 12. Conclusion

The simulation module provides a structured and controllable environment for studying distributed behavior.

It demonstrates that even minimal local rules can produce coordinated system-level dynamics.

This module forms the basis for further development toward a fully distributed MicroBot system.
