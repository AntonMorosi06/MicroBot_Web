# MicroBot System

## Overview

MicroBot System is a modular prototype framework for exploring swarm-based behavior and programmable matter concepts.

The project models a system composed of multiple simple units (nodes) that interact locally to produce coordinated global behavior. It combines simulation, visualization, documentation, and a minimal hardware prototype into a single structured repository.

The goal is not to build a single autonomous robot, but to study how collective behavior can emerge from distributed units.

---

## System Concept

The MicroBot System is based on a layered architecture:

| Layer      | Description                                           |
| ---------- | ----------------------------------------------------- |
| Input      | External signals, commands, or future interfaces      |
| Vision     | Environmental perception (future component)           |
| Software   | Simulation, logic, control, and visualization         |
| Controller | Embedded systems (e.g. ESP32)                         |
| Field      | Interaction medium (conceptual, e.g. magnetic forces) |
| Nodes      | Individual MicroBot units                             |

Each node operates locally, without global knowledge. System-level behavior emerges from interactions between nodes.

---

## Repository Structure

The repository is organized into independent but connected modules:

```text
MICROBOT_SYSTEM/
├── docs/
├── simulation/
├── web/
├── hardware/
├── examples/
```

| Module     | Purpose                                    |
| ---------- | ------------------------------------------ |
| docs       | System architecture, concepts, and roadmap |
| simulation | Software model of swarm behavior           |
| web        | Visual interface and system presentation   |
| hardware   | Minimal physical prototype (ESP32-based)   |
| examples   | Demonstration modes and command references |

---

## Simulation Module

The simulation implements a swarm of interacting units with:

* local perception
* velocity-based movement
* interaction rules (alignment, cohesion, separation)

### Real-Time Metrics

The system computes global metrics derived from local interactions:

| Metric            | Description                        |
| ----------------- | ---------------------------------- |
| Average Speed     | Mean velocity magnitude            |
| Average Neighbors | Local interaction density          |
| Coherence         | Directional alignment of the swarm |
| Center of Mass    | Global spatial reference           |

These metrics provide a measurable representation of system behavior.

---

## Web Module

The web module provides a structured interface for visualizing the system.

It includes:

* system overview and architecture sections
* simulation canvas (conceptual swarm visualization)
* interactive dashboard with real-time-like metrics

The dashboard reflects the same conceptual metrics used in the simulation:

* coherence
* average neighbors
* speed
* center of mass

Values are dynamically updated to represent a live system state.

---

## Hardware Module

The hardware module contains a minimal physical prototype using:

* ESP32 microcontroller
* LED-based node representation

Each LED acts as a simplified node. Collective behavior is simulated through activation patterns.

### Supported Modes

* Sync
* Wave
* Chase
* Random
* Alert

The hardware is currently centralized but represents the conceptual transition toward distributed systems.

---

## Examples Module

The examples module documents:

* behavior modes
* serial command interface
* system interaction patterns

It acts as a reference layer between documentation and implementation.

---

## Current Scope

The system currently provides:

* a structured simulation environment
* a coherent visualization layer
* a minimal hardware demonstration
* detailed architectural documentation

It does not yet include:

* distributed hardware nodes
* real communication protocols
* physical actuation or sensing

These are planned future steps.

---

## Design Principles

The project is built around the following principles:

* Local rules → global behavior
* Modular system design
* Separation between simulation, visualization, and hardware
* Progressive complexity
* Reproducibility and clarity

---

## Future Direction

Potential future developments include:

* distributed node architecture
* wireless communication between units
* sensor integration
* physical interaction fields (e.g. electromagnetic models)
* real-time synchronization between simulation and hardware

---

## Getting Started

### Simulation

```bash
cd simulation
pip install -r requirements.txt
python main.py
```

### Web

Open:

```bash
web/index.html
```

### Hardware

Upload:

```bash
hardware/esp32_swarm_demo/esp32_swarm_demo.ino
```

to an ESP32 board.

---

## Project Status

This project is an early-stage prototype.

It is intended as a foundation for further exploration rather than a finalized system.

---

## Author

Anton Morosi

---

## License

MIT License
