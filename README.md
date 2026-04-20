# MicroBot_Web
# MicroBot System — Distributed Swarm Prototype

# MicroBot System

MicroBot System is a modular prototype framework for exploring swarm-based systems and emergent behavior.

It combines simulation, visualization, and a minimal hardware implementation to study how simple units can coordinate and produce complex global dynamics without centralized control.

---

## What This Project Shows

This repository demonstrates:

* how local interaction rules generate global behavior
* how a swarm system can be modeled, measured, and visualized
* how software, web interfaces, and hardware prototypes can be aligned within a single architecture

---

## System at a Glance

* Simulation of interacting agents with real-time metrics
* Web-based dashboard reflecting system state
* ESP32 prototype representing physical nodes
* Structured architecture and documentation

---


## Overview

MicroBot is a modular swarm system concept based on distributed units (nodes) that coordinate to produce emergent collective behavior.

The project explores a shift from traditional single-robot architectures to a **distributed intelligence model**, where simple agents interact locally to generate complex global patterns.

This repository contains a unified prototype composed of three main layers:

* Simulation (behavior and swarm logic)
* Web interface (visualization and interaction)
* Hardware prototype (ESP32-based physical nodes)

---

## System Architecture

The system is structured into three interconnected components:

### 1. Simulation Engine

A Python-based environment that models swarm behavior using simple local rules.

Key features:

* Multi-agent system simulation
* Emergent behavior patterns
* Modular and extensible logic
* Real-time state evolution

Purpose:
To validate swarm logic before applying it to physical hardware.

---

### 2. Web Interface

A browser-based visualization layer designed to represent system behavior and structure.

Key features:

* Interactive UI
* Real-time visual feedback
* System metrics and overlays
* Conceptual representation of swarm dynamics

Purpose:
To provide a human-readable interface for understanding and presenting the system.

---

### 3. Hardware Prototype (ESP32)

A physical implementation of basic swarm principles using microcontrollers and LEDs.

Key features:

* Multiple nodes simulated via LED units
* State-based behavior system
* Serial-controlled interaction
* Pattern-based coordination (sync, wave, chase, random, alert)

Purpose:
To demonstrate how abstract swarm logic can be translated into real-world behavior.

---

## Conceptual Foundation

MicroBot is based on the principle that:

> Complex systems can emerge from simple rules applied across distributed agents.

Instead of central control, each unit follows local logic, and the global behavior emerges from interaction.

This aligns with:

* Swarm robotics
* Distributed systems
* Emergent computation
* Programmable matter (long-term vision)

---

## How to Run

### Simulation

1. Navigate to the simulation folder
2. Run the main Python file:

```bash
python main.py
```

---

### Web Interface

1. Open the web folder
2. Launch the interface:

```bash
open index.html
```

or serve it locally with a simple server

---

### Hardware (ESP32)

1. Upload the provided `.ino` file to ESP32
2. Connect LEDs to defined GPIO pins
3. Open Serial Monitor (115200 baud)
4. Send commands:

```
0 -> OFF
1 -> SYNC PULSE
2 -> WAVE
3 -> CHASE
4 -> RANDOM
5 -> ALERT
```

---

## Current State

This project represents an **early-stage prototype**, focused on:

* Demonstrating feasibility
* Building system architecture
* Exploring interaction models

The system is functional but still evolving.

---

## Future Directions

Planned developments include:

* Real multi-node communication (wireless)
* Sensor integration
* Magnetic interaction systems
* Scalable swarm coordination
* AI-assisted behavior control

---

## Author

Anton Morosi

Independent developer focused on distributed systems, simulation, and modular robotics.

---

## Notes

This project is part of a broader research and development path aimed at building a scalable swarm system.

It is intended both as a technical exploration and as a foundation for future applications.
