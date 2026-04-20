# MicroBot System — Wiring Notes

## 1. Purpose

This document describes the basic wiring model of the current MicroBot hardware prototype.

The present hardware implementation is intentionally minimal. Its purpose is not to represent the final hardware architecture of the system, but to provide a simple physical setup for validating timing, control patterns, and state transitions.

The current prototype uses one ESP32 board and multiple LEDs to represent simplified MicroBot nodes.

---

## 2. Prototype Logic

In the current configuration, each LED corresponds to a single node.

This means that the hardware prototype does not yet implement independent physical units. Instead, it provides an abstract and low-cost representation of a distributed node system through digital outputs.

The mapping is the following:

| System Concept  | Physical Element |
| --------------- | ---------------- |
| MicroBot node   | LED              |
| Node state      | LED ON/OFF       |
| Node identifier | GPIO pin         |

This abstraction is sufficient for demonstrating coordination patterns and serial-controlled state changes.

---

## 3. Required Components

The current prototype requires only a small set of basic components.

| Component               | Quantity  | Notes                          |
| ----------------------- | --------- | ------------------------------ |
| ESP32 development board | 1         | Main control unit              |
| LEDs                    | 5         | One per node                   |
| Resistors               | 5         | 220Ω to 330Ω recommended       |
| Breadboard              | 1         | Standard prototyping board     |
| Jumper wires            | As needed | Male-to-male wires recommended |
| USB cable               | 1         | For power and programming      |

This configuration is intentionally simple and reproducible.

---

## 4. Pin Mapping

The current suggested pin mapping is the following:

| Node ID | GPIO Pin |
| ------- | -------- |
| Node 0  | 23       |
| Node 1  | 22       |
| Node 2  | 21       |
| Node 3  | 19       |
| Node 4  | 18       |

These pins are used as digital outputs.

If a different wiring layout is required, the software mapping must be updated accordingly in the ESP32 code.

---

## 5. Electrical Connection Model

Each node is wired as a standard LED output line.

The electrical path is:

GPIO → resistor → LED anode → LED cathode → GND

This means:

* the GPIO pin provides the output signal
* the resistor limits current
* the LED indicates node state
* ground closes the circuit

This is the simplest safe configuration for a visible digital state output.

---

## 6. Polarity Notes

Correct LED polarity is necessary for proper operation.

| LED Part | Description                          |
| -------- | ------------------------------------ |
| Anode    | Long leg, connected to resistor side |
| Cathode  | Short leg, connected to GND          |

If the LED does not turn on, polarity should be checked first.

---

## 7. Wiring Procedure

A basic assembly procedure is the following:

1. Place the ESP32 on the breadboard or connect it externally
2. Insert the LEDs into the breadboard
3. Connect one resistor in series with each LED anode
4. Connect each resistor to its assigned GPIO pin
5. Connect each LED cathode to GND
6. Connect the ESP32 to the computer through USB
7. Upload the firmware and test the output patterns

This procedure is sufficient for the current prototype stage.

---

## 8. Safety and Practical Notes

The prototype is electrically simple, but a few precautions remain important.

| Topic            | Note                                           |
| ---------------- | ---------------------------------------------- |
| Current limiting | Always use resistors with LEDs                 |
| Short circuits   | Check breadboard connections before powering   |
| GPIO load        | Keep output load minimal                       |
| USB power        | Sufficient for the current LED-based prototype |

The present setup is well within the normal operating limits of the ESP32 when correctly wired.

---

## 9. Operational Interpretation

The wiring setup is not only an electrical layout but also a physical representation of the system model.

Each LED output corresponds to the visible state of a logical node. When the software changes a node state, the change becomes physically observable through the LED pattern.

This creates a direct mapping between abstract control logic and real-world output.

---

## 10. Current Limitations

The current wiring model has clear limitations.

| Area              | Limitation                                   |
| ----------------- | -------------------------------------------- |
| Node independence | Nodes are not physically autonomous          |
| Communication     | No node-to-node communication                |
| Sensors           | No environmental inputs connected            |
| Actuation         | No physical movement or magnetic interaction |

These limitations are expected in an early prototype and do not reduce the usefulness of the setup for demonstration purposes.

---

## 11. Future Hardware Evolution

This wiring model is a first-stage prototype and should be seen as a starting point.

Future versions may include:

* one microcontroller per node
* wireless communication modules
* local sensors
* battery-based node power
* magnetic or mechanical actuation systems

When that happens, the wiring model will evolve from a centralized breadboard layout to a genuinely distributed hardware network.

---

## 12. Conclusion

The current wiring configuration provides a simple and effective way to represent node-based swarm behavior in hardware form.

Although minimal, it establishes a consistent bridge between:

* node abstraction
* control logic
* physical observation

This makes it suitable as a first demonstrative implementation of the MicroBot hardware layer.
