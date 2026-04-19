# MicroBot System — Hardware Notes

## 1. Introduction

This document describes the current hardware implementation of the MicroBot system.

The hardware layer represents a simplified physical prototype designed to validate core swarm concepts using minimal components. It does not yet implement true distributed nodes, but simulates multiple agents through a single microcontroller.

The purpose of this prototype is to:

* demonstrate coordinated behavior
* validate timing and control logic
* provide a physical reference for the system

---

## 2. Hardware Overview

The current implementation is based on an ESP32 microcontroller controlling multiple LED units.

Each LED represents a single MicroBot node.

| Component             | Description                |
| --------------------- | -------------------------- |
| ESP32                 | Main microcontroller       |
| LEDs                  | Represent individual nodes |
| Resistors (220Ω–330Ω) | Current limiting for LEDs  |
| Breadboard            | Prototyping surface        |
| Jumper wires          | Electrical connections     |

This configuration allows rapid testing without complex hardware design.

---

## 3. Node Representation

In this prototype, nodes are abstracted as digital outputs.

| Element       | Representation |
| ------------- | -------------- |
| MicroBot      | LED unit       |
| Node state    | LED ON/OFF     |
| Node identity | GPIO pin index |

Although simplified, this mapping preserves the conceptual structure of the system.

---

## 4. Pin Configuration

The system uses five GPIO pins on the ESP32.

| Node ID | GPIO Pin |
| ------- | -------- |
| Node 0  | 23       |
| Node 1  | 22       |
| Node 2  | 21       |
| Node 3  | 19       |
| Node 4  | 18       |

Each pin is configured as a digital output.

---

## 5. Wiring Scheme

Each LED is connected in series with a resistor to prevent overcurrent.

The standard connection is:

GPIO → resistor → LED → GND

More precisely:

* the GPIO pin is connected to one side of the resistor
* the resistor is connected to the LED anode (long leg)
* the LED cathode (short leg) is connected to ground

This configuration ensures safe operation of both the LED and the microcontroller.

---

## 6. Power Considerations

The ESP32 can be powered via USB.

Key considerations:

| Aspect           | Notes                           |
| ---------------- | ------------------------------- |
| Voltage          | ESP32 operates at 3.3V logic    |
| Current per GPIO | Limited, use resistors          |
| Total load       | Must remain within board limits |

The current setup with LEDs is well within safe operating conditions.

---

## 7. Behavior Implementation

Behavior is implemented through software patterns controlling the LEDs.

Each pattern represents a different type of swarm behavior.

| Mode   | Description                           |
| ------ | ------------------------------------- |
| Sync   | All nodes share the same state        |
| Wave   | Activation propagates sequentially    |
| Chase  | Moving pattern with short persistence |
| Random | Independent stochastic activation     |
| Alert  | Rapid global flashing                 |

These modes simulate different coordination strategies.

---

## 8. Control Interface

The system is controlled via serial communication.

| Parameter | Value          |
| --------- | -------------- |
| Baud rate | 115200         |
| Interface | Serial Monitor |

Commands are sent manually and interpreted by the microcontroller.

| Command | Action               |
| ------- | -------------------- |
| 0       | Turn off all nodes   |
| 1       | Activate sync mode   |
| 2       | Activate wave mode   |
| 3       | Activate chase mode  |
| 4       | Activate random mode |
| 5       | Activate alert mode  |

This provides a simple external control mechanism.

---

## 9. Limitations

The current hardware prototype has several limitations:

| Area          | Limitation                                 |
| ------------- | ------------------------------------------ |
| Distribution  | All nodes are controlled by a single ESP32 |
| Communication | No inter-node communication                |
| Autonomy      | Behavior is externally triggered           |
| Sensing       | No environmental input                     |

These limitations are expected and define the next development steps.

---

## 10. Future Hardware Evolution

Future iterations of the hardware system will focus on increasing realism and autonomy.

Planned developments include:

| Area              | Direction                                  |
| ----------------- | ------------------------------------------ |
| Node Architecture | One microcontroller per node               |
| Communication     | Wireless protocols (e.g. ESP-NOW, BLE)     |
| Sensors           | Proximity, light, or environmental sensors |
| Actuation         | Moving components or magnetic interaction  |
| Power             | Independent power sources per node         |

The goal is to transition from a simulated swarm to a physically distributed system.

---

## 11. Integration with System Architecture

The hardware layer is designed to align with the overall system architecture.

| Layer      | Role                         |
| ---------- | ---------------------------- |
| Simulation | Defines behavior logic       |
| Hardware   | Executes behavior physically |
| Interface  | Observes and controls system |

In future versions, these layers will be more tightly integrated.

---

## 12. Conclusion

The current hardware implementation provides a minimal but functional representation of the MicroBot system.

Despite its simplicity, it successfully demonstrates:

* coordinated behavior
* state-based logic
* system-level patterns

It serves as a foundation for more advanced and distributed hardware designs.
