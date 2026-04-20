# MicroBot System — Simulation Module

## Overview

The simulation module provides a software-based representation of the MicroBot system.

It models a simplified swarm of interacting units (bots) moving within a bounded environment. Each bot follows local interaction rules, and global behavior emerges from these interactions.

The purpose of this module is to:

* validate swarm behavior logic
* provide a visual and measurable system state
* act as a bridge between conceptual architecture and physical implementation

The simulation is intentionally minimal, but structured in a way that supports future extensions.

---

## Architecture

The module is organized into distinct layers:

| Layer    | Description                                |
| -------- | ------------------------------------------ |
| core     | Application lifecycle, world management    |
| entities | Bot definition and simulation controller   |
| systems  | Interaction rules and system-level metrics |
| ui       | Rendering and HUD                          |
| config   | Centralized configuration                  |

This separation allows the simulation to remain modular and maintainable.

---

## Simulation Model

The system is composed of multiple bots defined by:

* position `(x, y)`
* velocity `(vx, vy)`
* maximum speed constraint
* local perception radius

Bots do not have global knowledge. Each unit interacts only with nearby neighbors, producing emergent behavior at the system level.

---

## Interaction Rules

The simulation implements three fundamental behaviors:

### Alignment

Bots tend to match the velocity of nearby neighbors.

### Cohesion

Bots move toward the average position of nearby neighbors.

### Separation

Bots avoid getting too close to nearby neighbors.

These rules can be combined to produce different swarm behaviors.

---

## Simulation Modes

The simulation supports multiple modes:

| Mode      | Description                                  |
| --------- | -------------------------------------------- |
| Alignment | Velocity synchronization                     |
| Flocking  | Combined alignment, cohesion, and separation |
| Disorder  | Random motion without coordination           |

Modes can be switched at runtime using keyboard input.

---

## System Metrics

The simulation computes real-time metrics describing the global state of the swarm.

### Average Speed

Represents the mean magnitude of velocity across all bots.

This provides an indication of overall system activity.

---

### Average Neighbors

Represents the average number of nearby bots detected per unit.

This reflects local density and interaction level.

---

### Coherence

Measures how aligned the swarm is in terms of movement direction.

It is defined as the ratio between:

* the magnitude of the sum of all velocity vectors
* the sum of individual speed magnitudes

Values range from:

* `0.0` → completely disordered system
* `1.0` → fully aligned system

---

### Center of Mass

Represents the average position of all bots.

This provides a global spatial reference and helps visualize collective movement.

---

## Rendering

The simulation uses `pygame` for visualization.

The rendering includes:

* bot positions
* optional neighbor links
* center of mass indicator
* HUD with real-time metrics

---

## Controls

| Key | Action           |
| --- | ---------------- |
| 1   | Alignment mode   |
| 2   | Flocking mode    |
| 3   | Disorder mode    |
| R   | Reset simulation |

---

## Execution

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the simulation

```bash
python main.py
```

---

## Current Limitations

| Area          | Limitation                                             |
| ------------- | ------------------------------------------------------ |
| Physics       | Simplified motion model                                |
| Environment   | No obstacles or external fields                        |
| Communication | No explicit messaging between bots                     |
| Scalability   | Designed for visualization, not large-scale simulation |

These constraints are intentional and consistent with the current scope.

---

## Role in the System

The simulation module complements the rest of the repository:

| Module     | Role                              |
| ---------- | --------------------------------- |
| docs       | Defines architecture and concepts |
| simulation | Implements behavior and metrics   |
| web        | Provides presentation layer       |
| hardware   | Provides physical prototype       |

The simulation acts as a central reference for system behavior before hardware scaling.

---

## Future Extensions

Possible future improvements include:

* obstacle interaction
* force-based fields (e.g. magnetic models)
* advanced clustering analysis
* real-time parameter tuning
* integration with external control systems

---

## Conclusion

The simulation module provides a structured and observable environment for studying swarm behavior within the MicroBot system.

It is not a complete model, but a foundational layer that supports both experimentation and system-level reasoning.
