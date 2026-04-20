# MicroBot System — Architecture

## Overview

The MicroBot System is structured as a layered, modular architecture designed to support the study and development of swarm-based systems.

The architecture separates concerns between perception, control, interaction, and physical execution. This enables incremental development while maintaining conceptual consistency across modules.

---

## Architectural Layers

The system is organized into six conceptual layers:

| Layer      | Description                                               |
| ---------- | --------------------------------------------------------- |
| Input      | External commands, user interaction, or future interfaces |
| Vision     | Environmental perception (future component)               |
| Software   | Simulation, control logic, metrics, and visualization     |
| Controller | Embedded execution layer (e.g. ESP32)                     |
| Field      | Interaction medium between nodes (conceptual)             |
| Nodes      | Individual MicroBot units                                 |

---

## Layer Responsibilities

### Input Layer

Handles external control signals such as:

* user commands
* UI interactions
* future API integrations

This layer does not directly control nodes, but feeds the system state.

---

### Vision Layer (Planned)

Intended to provide environmental awareness through:

* computer vision
* tracking systems
* external sensing

Currently not implemented, but structurally defined.

---

### Software Layer

Core of the system.

Responsible for:

* simulation of swarm behavior
* implementation of interaction rules
* computation of system-level metrics
* visualization logic (web and HUD)

This layer defines how local interactions translate into global behavior.

---

### Controller Layer

Represents embedded execution.

In the current prototype:

* implemented via ESP32
* controls multiple nodes centrally

In future versions:

* distributed controllers per node

---

### Field Layer (Conceptual)

Defines how nodes influence each other.

Examples:

* proximity interaction
* force-based models (e.g. magnetic fields)
* communication signals

In the current implementation:

* abstracted through distance-based interaction rules

---

### Node Layer

Represents individual MicroBot units.

Each node is defined by:

* position
* velocity
* local perception radius
* simple behavioral rules

Nodes do not have global knowledge of the system.

---

## Data Flow

The system operates as a continuous loop:

```text id="flow1"
Input → Software → Controller → Nodes → (Field Interaction) → Software
```

Explanation:

1. Input defines system state or mode
2. Software computes behavior and metrics
3. Controller applies commands
4. Nodes update their state
5. Interactions occur through the field (conceptual)
6. Updated state is fed back into the system

This loop enables emergent behavior.

---

## Simulation Architecture

Within the software layer, the simulation is structured as:

```text id="flow2"
World → Bots → Neighbor Detection → Interaction Rules → Metrics → Rendering
```

Where:

* **World** defines boundaries
* **Bots** are agents
* **Neighbor Detection** determines local context
* **Interaction Rules** drive behavior
* **Metrics** describe global state
* **Rendering** visualizes the system

---

## Metric Layer

The system includes a metric computation layer that aggregates local state into global descriptors.

| Metric            | Meaning               |
| ----------------- | --------------------- |
| Average Speed     | System activity level |
| Average Neighbors | Interaction density   |
| Coherence         | Directional alignment |
| Center of Mass    | Spatial reference     |

These metrics are computed in simulation and reflected in the web interface.

---

## Current Implementation Mapping

| Conceptual Layer | Current Implementation            |
| ---------------- | --------------------------------- |
| Input            | Keyboard + Web UI                 |
| Vision           | Not implemented                   |
| Software         | Python simulation + Web interface |
| Controller       | ESP32 prototype                   |
| Field            | Distance-based interaction        |
| Nodes            | Simulated agents + LED nodes      |

---

## Architectural Properties

The system exhibits the following properties:

* **Decentralization (conceptual)**
  Nodes act locally, without global awareness

* **Emergence**
  Global patterns arise from local interactions

* **Modularity**
  Each layer can evolve independently

* **Scalability (planned)**
  Architecture supports expansion to many nodes

---

## Limitations

Current architecture limitations include:

| Area            | Limitation                      |
| --------------- | ------------------------------- |
| Distribution    | Hardware is centralized         |
| Communication   | No real node-to-node messaging  |
| Physics         | Simplified interaction model    |
| Synchronization | No real-time system integration |

---

## Future Evolution

Planned architectural improvements:

* distributed node controllers
* real communication layer
* sensor integration
* field-based physical interaction models
* synchronization between simulation and hardware

---

## Conclusion

The MicroBot System architecture provides a structured foundation for exploring swarm behavior.

It separates conceptual layers while maintaining a consistent data flow, allowing the system to evolve incrementally toward more complex and realistic implementations.
