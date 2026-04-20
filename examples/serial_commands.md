# MicroBot System — Serial Commands

## 1. Overview

This document defines the serial commands currently used by the MicroBot hardware prototype.

The command interface is intentionally minimal. Its purpose is to provide a simple control layer for triggering predefined behavior modes during testing and demonstration.

At the current stage, commands are sent manually through the Serial Monitor.

---

## 2. Interface Parameters

| Parameter          | Value                |
| ------------------ | -------------------- |
| Communication Type | Serial               |
| Baud Rate          | 115200               |
| Input Method       | Manual command input |

---

## 3. Command Set

| Command | Action                 |
| ------- | ---------------------- |
| 0       | Disable all nodes      |
| 1       | Activate Sync mode     |
| 2       | Activate Wave mode     |
| 3       | Activate Chase mode    |
| 4       | Activate Random mode   |
| 5       | Activate Alert mode    |
| s       | Print system status    |
| h       | Print help information |

---

## 4. Command Semantics

### 4.1 `0`

Disables all active outputs and returns the system to an inactive state.

This command is useful for:

* reset
* idle state
* safe stop

### 4.2 `1`

Activates Sync mode.

All nodes share the same state simultaneously.

### 4.3 `2`

Activates Wave mode.

Activation propagates sequentially across the available nodes.

### 4.4 `3`

Activates Chase mode.

A moving pattern travels through the node set, producing a dynamic motion effect.

### 4.5 `4`

Activates Random mode.

Nodes change state independently to simulate low-coherence activity.

### 4.6 `5`

Activates Alert mode.

All nodes flash rapidly to indicate a warning or critical pattern.

### 4.7 `s`

Prints current system status through the serial output.

This may include:

* current mode
* number of nodes
* general runtime information

### 4.8 `h`

Prints the list of supported commands.

This is intended as a built-in operator reference.

---

## 5. Intended Use

The serial command layer is currently used for:

* manual testing
* mode switching
* hardware validation
* demonstration control

It is not yet a full communication protocol.

---

## 6. Future Evolution

In future versions, the command system may be extended to support:

* parameterized commands
* node-specific addressing
* wireless command routing
* simulation-to-hardware synchronization
* structured messaging formats

These additions should remain consistent with the overall modular architecture of the system.

---

## 7. Conclusion

The current serial interface provides a minimal but effective way to control the hardware prototype.

Although simple, it supports reproducible demonstrations and creates a bridge between abstract behavior modes and physical execution.
