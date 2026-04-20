# MicroBot System — Hardware Module

## Overview

The hardware module contains the first physical prototype of the MicroBot system.

Its purpose is to provide a minimal and reproducible hardware representation of swarm behavior using an ESP32 microcontroller and LED-based nodes. This implementation does not yet correspond to a fully distributed hardware architecture, but it establishes a physical reference for behavior modes, timing logic, and external control through serial commands.

The current hardware module should therefore be understood as an early demonstrative prototype rather than a final system implementation.

---

## Current Structure

| Path                                  | Description                                     |
| ------------------------------------- | ----------------------------------------------- |
| esp32_swarm_demo/esp32_swarm_demo.ino | Main ESP32 firmware for the LED-based prototype |
| schematics/wiring_notes.md            | Wiring description and assembly notes           |

---

## Prototype Model

The present prototype uses one ESP32 board and five LEDs.

Each LED corresponds to a simplified MicroBot node. Node states are represented through digital ON/OFF outputs, and collective behavior is simulated through predefined activation patterns.

This means that the prototype is centralized in hardware execution, even if it conceptually represents a multi-node system.

---

## Supported Behavior Modes

The firmware currently supports the following modes:

| Command | Mode   | Description                          |
| ------- | ------ | ------------------------------------ |
| 0       | Off    | Disables all nodes                   |
| 1       | Sync   | All nodes share the same state       |
| 2       | Wave   | Activation propagates sequentially   |
| 3       | Chase  | Moving pattern across nodes          |
| 4       | Random | Independent stochastic node activity |
| 5       | Alert  | Rapid global flashing pattern        |

These modes correspond to the demonstration logic described in the repository examples.

---

## Control Interface

The prototype is controlled through the Serial Monitor.

| Parameter | Value  |
| --------- | ------ |
| Interface | Serial |
| Baud Rate | 115200 |

Additional commands include:

| Command | Function     |
| ------- | ------------ |
| s       | Print status |
| h       | Print help   |

This command interface is intentionally minimal and suitable for testing and demonstrations.

---

## Required Components

The current prototype requires:

* 1 ESP32 development board
* 5 LEDs
* 5 resistors (220Ω–330Ω recommended)
* 1 breadboard
* jumper wires
* USB cable for power and upload

This keeps the module simple and easy to reproduce.

---

## Purpose Within the Repository

The hardware module complements the other main repository components:

| Module     | Role                                                 |
| ---------- | ---------------------------------------------------- |
| docs       | Describes the architecture and development direction |
| simulation | Implements the behavioral logic in software          |
| web        | Provides visual presentation and interface structure |
| hardware   | Provides a minimal physical implementation           |

The hardware layer is therefore not isolated. It exists as part of a broader system-oriented prototype.

---

## Current Limitations

At the current stage, the hardware module has several clear limitations:

| Area          | Limitation                             |
| ------------- | -------------------------------------- |
| Distribution  | One microcontroller controls all nodes |
| Communication | No node-to-node communication          |
| Sensing       | No environmental sensors connected     |
| Actuation     | No movement or magnetic interaction    |

These limitations are expected and consistent with the current scope of the project.

---

## Future Direction

Future versions of the hardware module may evolve toward:

* one controller per node
* wireless communication
* local sensing
* physically independent units
* more advanced actuation systems

The present prototype should be considered the initial hardware layer of that longer development path.

---

## Conclusion

The hardware module provides a simple but meaningful physical implementation of the MicroBot system.

It translates abstract node-based behavior into visible and testable output patterns, making it a useful bridge between documentation, simulation, and future distributed hardware development.
