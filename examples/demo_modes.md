# MicroBot System — Demo Modes

## 1. Purpose

This document describes the main demonstration modes used across the MicroBot system.

These modes are intended to provide simple, readable, and reproducible representations of collective behavior. They are not meant to define the full long-term behavior of the system, but rather to offer a structured set of observable patterns for simulation, visualization, and hardware prototyping.

The same conceptual modes may appear in different modules of the repository:

* simulation
* web visualization
* hardware prototype

This ensures consistency across the system.

---

## 2. General Logic

Each mode corresponds to a distinct coordination pattern.

A mode defines how nodes behave over time, how activation propagates, and how the observer can interpret the state of the system.

The purpose of using modes is twofold. First, they simplify testing. Second, they provide a common vocabulary for comparing behavior across layers.

---

## 3. Defined Modes

| Mode | Name   | Description                                                 |
| ---- | ------ | ----------------------------------------------------------- |
| 0    | Off    | All nodes are inactive                                      |
| 1    | Sync   | All nodes share the same state simultaneously               |
| 2    | Wave   | Activation propagates sequentially across nodes             |
| 3    | Chase  | A moving pattern travels through the system                 |
| 4    | Random | Nodes change independently with stochastic variation        |
| 5    | Alert  | A rapid global signal indicates a warning or critical state |

---

## 4. Mode Descriptions

### 4.1 Off

The Off mode disables all visible activity.

This mode is useful as a baseline condition. It provides a neutral reference state against which all other behaviors can be compared.

Typical use:

* reset state
* idle condition
* initialization phase

---

### 4.2 Sync

In Sync mode, all nodes transition together.

This is the simplest form of global coordination and is useful for validating shared timing and state consistency.

Typical interpretation:

* global synchronization
* broadcast-like behavior
* unified collective state

---

### 4.3 Wave

In Wave mode, activation moves progressively from one node to another.

This mode is useful for representing propagation effects and directional organization.

Typical interpretation:

* sequential coordination
* signal propagation
* ordered activation

---

### 4.4 Chase

In Chase mode, activity moves continuously through the node set, often with one or more trailing active elements.

This behavior is more dynamic than Wave mode and creates a stronger impression of motion.

Typical interpretation:

* directional pursuit
* circulating activity
* moving swarm focus

---

### 4.5 Random

In Random mode, nodes evolve independently with no obvious global order.

This mode is useful both as a contrast case and as a representation of disorder, noise, or exploratory behavior.

Typical interpretation:

* decentralized independent activity
* low-coherence state
* exploratory or unstable condition

---

### 4.6 Alert

In Alert mode, all nodes switch rapidly between active and inactive states.

This creates a high-visibility global signal and is particularly useful in demonstrations where a critical transition must be clearly visible.

Typical interpretation:

* system warning
* critical state
* emergency broadcast

---

## 5. Cross-Module Interpretation

The same mode can have slightly different implementations depending on the layer.

| Layer      | Representation                                |
| ---------- | --------------------------------------------- |
| Simulation | Agent movement or rule-based behavior pattern |
| Web        | Visual animation or dashboard state           |
| Hardware   | LED activation pattern on physical outputs    |

The important point is not identical implementation, but conceptual consistency.

---

## 6. Why These Modes Matter

These modes provide a minimal behavioral vocabulary for the system.

They make the project easier to test, easier to present, and easier to extend. They also establish a bridge between abstract swarm logic and concrete demonstrative outputs.

Without this shared structure, each module risks becoming disconnected from the others.

---

## 7. Future Expansion

Future versions may include more advanced modes such as:

* clustering
* local attraction and repulsion
* adaptive response to sensors
* distributed consensus
* topology-dependent behavior

These should be introduced only when they correspond to real system capabilities.

---

## 8. Conclusion

The demo modes described here provide a practical and coherent way to observe MicroBot behavior across simulation, web visualization, and hardware.

They are intentionally simple, but they form a stable foundation for more advanced distributed logic.
