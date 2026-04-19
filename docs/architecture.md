# MicroBot System — Architecture

## 1. Architectural Overview

The MicroBot system is designed as a layered and modular architecture that separates concerns between simulation, visualization, and physical execution.

The system is not monolithic. Instead, it is composed of independent but interoperable components that can evolve separately while maintaining a coherent structure.

At a high level, the architecture can be described as a three-layer system:

| Layer            | Description                       | Role                                       |
| ---------------- | --------------------------------- | ------------------------------------------ |
| Simulation Layer | Software-based multi-agent system | Defines and tests swarm logic              |
| Interface Layer  | Web-based visualization system    | Provides observation and interaction       |
| Hardware Layer   | Physical node implementation      | Executes behavior in real-world conditions |

These layers are connected conceptually rather than tightly coupled, allowing progressive development.

---

## 2. Design Principles

The architecture is based on a set of guiding principles that influence all components of the system.

| Principle        | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| Modularity       | Each component can be developed and modified independently |
| Scalability      | The system should support increasing numbers of nodes      |
| Decentralization | No central controller is required for core behavior        |
| Abstraction      | Simulation precedes hardware implementation                |
| Observability    | System state must be visible and interpretable             |

These principles ensure that the system remains flexible and extensible.

---

## 3. Simulation Layer

The simulation layer represents the core logic of the system.

It models a swarm as a set of agents interacting within an environment according to predefined local rules.

### Internal Structure

| Module         | Responsibility                              |
| -------------- | ------------------------------------------- |
| agent.py       | Defines individual node behavior and state  |
| environment.py | Represents the space and constraints        |
| rules.py       | Implements interaction logic between agents |
| simulation.py  | Manages update cycles and system evolution  |

### Execution Model

The simulation operates through discrete time steps. At each step:

* each agent evaluates its local state
* interaction rules are applied
* the global system state is updated

No global controller enforces behavior. The system evolves through repeated local interactions.

---

## 4. Interface Layer (Web)

The interface layer provides a visual and interactive representation of the system.

It is not responsible for generating behavior, but for exposing system dynamics in a human-readable form.

### Structure

| Component  | Role                            |
| ---------- | ------------------------------- |
| index.html | Structural layout               |
| style.css  | Visual design                   |
| script.js  | Interaction and dynamic updates |

### Responsibilities

* display node states
* visualize patterns and transitions
* provide user interaction (controls, modes)
* support debugging and interpretation

This layer acts as a bridge between system logic and human understanding.

---

## 5. Hardware Layer

The hardware layer is a simplified physical implementation of the system.

In the current version, nodes are represented by LEDs controlled via an ESP32 microcontroller.

### Structure

| Element   | Description                           |
| --------- | ------------------------------------- |
| ESP32     | Central execution unit                |
| LED units | Represent individual nodes            |
| GPIO pins | Map logical nodes to physical outputs |

### Behavior Model

Each LED corresponds to a node state. Behavior is implemented through predefined modes:

| Mode   | Description                     |
| ------ | ------------------------------- |
| Sync   | All nodes share the same state  |
| Wave   | State propagates sequentially   |
| Chase  | Moving pattern across nodes     |
| Random | Independent stochastic behavior |
| Alert  | High-frequency global signal    |

Although centralized in implementation, this layer is designed to emulate distributed logic.

---

## 6. Data Flow

The system does not yet implement full bidirectional communication between layers. However, a conceptual data flow can be defined.

| Source     | Target     | Type of Data                      |
| ---------- | ---------- | --------------------------------- |
| Simulation | Interface  | State updates, positions, metrics |
| Interface  | Simulation | Control commands (future)         |
| Interface  | Hardware   | Mode selection (manual input)     |
| Hardware   | Interface  | Not implemented (future)          |

Currently, interaction is primarily manual (e.g., serial commands for hardware).

---

## 7. State Management

Each node in the system maintains an internal state that evolves over time.

A minimal node state can be represented as:

| Field     | Description                          |
| --------- | ------------------------------------ |
| id        | Unique identifier                    |
| state     | Current activation or behavior state |
| position  | Spatial location (simulation only)   |
| neighbors | Nearby nodes (logical or spatial)    |

State updates occur at each simulation step or hardware cycle.

---

## 8. Synchronization Model

The system uses a time-based update mechanism rather than event-driven synchronization.

| Aspect      | Description                                                                      |
| ----------- | -------------------------------------------------------------------------------- |
| Timing      | Based on discrete time steps (`millis()` in hardware, loop cycles in simulation) |
| Consistency | No strict global synchronization required                                        |
| Latency     | Not yet modeled explicitly                                                       |

This approach simplifies implementation while remaining compatible with distributed systems.

---

## 9. Extensibility

The architecture is designed to support future extensions without structural redesign.

Possible extensions include:

* wireless communication between nodes
* distributed execution (multiple microcontrollers)
* sensor integration
* adaptive rule systems
* real-time feedback loops

Each extension can be integrated at the appropriate layer without affecting unrelated components.

---

## 10. Limitations of Current Architecture

| Area            | Limitation                                    |
| --------------- | --------------------------------------------- |
| Distribution    | Hardware is still centralized                 |
| Communication   | No real inter-node messaging                  |
| Synchronization | Simplified timing model                       |
| Abstraction gap | Simulation and hardware not yet fully aligned |

These limitations are consistent with the early-stage nature of the system.

---

## 11. Architectural Direction

The long-term goal is to transition toward a fully distributed architecture in which:

* each node operates independently
* communication is local and peer-to-peer
* global behavior emerges without centralized control

This will require:

* embedded communication protocols
* decentralized state management
* robust synchronization strategies

The current architecture serves as a foundation for this transition.
