/*
  ============================================================
  MICROBOT SYSTEM - ESP32 SWARM DEMO
  ------------------------------------------------------------
  Hardware module prototype for the MicroBot System repository.

  This sketch represents a minimal physical implementation of
  simplified swarm behavior using:
  - one ESP32
  - five LED-based nodes
  - serial-triggered behavior modes

  Node mapping:
    Node 0 -> GPIO 23
    Node 1 -> GPIO 22
    Node 2 -> GPIO 21
    Node 3 -> GPIO 19
    Node 4 -> GPIO 18

  Supported serial commands:
    0 -> OFF
    1 -> SYNC
    2 -> WAVE
    3 -> CHASE
    4 -> RANDOM
    5 -> ALERT
    s -> STATUS
    h -> HELP
  ============================================================
*/

const int NUM_NODES = 5;
const int NODE_PINS[NUM_NODES] = {23, 22, 21, 19, 18};

enum SystemMode {
  MODE_OFF = 0,
  MODE_SYNC = 1,
  MODE_WAVE = 2,
  MODE_CHASE = 3,
  MODE_RANDOM = 4,
  MODE_ALERT = 5
};

SystemMode currentMode = MODE_SYNC;

// Global timing
unsigned long nowMs = 0;
unsigned long lastFrameMs = 0;
const unsigned long FRAME_INTERVAL = 20;

// SYNC
bool syncState = false;
unsigned long lastSyncToggleMs = 0;
const unsigned long SYNC_INTERVAL = 500;

// WAVE
int waveIndex = 0;
unsigned long lastWaveStepMs = 0;
const unsigned long WAVE_INTERVAL = 180;

// CHASE
int chaseIndex = 0;
unsigned long lastChaseStepMs = 0;
const unsigned long CHASE_INTERVAL = 120;

// RANDOM
unsigned long lastRandomStepMs = 0;
const unsigned long RANDOM_INTERVAL = 250;

// ALERT
bool alertState = false;
unsigned long lastAlertToggleMs = 0;
const unsigned long ALERT_INTERVAL = 100;

void setAllNodes(bool state) {
  for (int i = 0; i < NUM_NODES; i++) {
    digitalWrite(NODE_PINS[i], state ? HIGH : LOW);
  }
}

void clearAllNodes() {
  setAllNodes(false);
}

const char* modeToString(SystemMode mode) {
  switch (mode) {
    case MODE_OFF: return "OFF";
    case MODE_SYNC: return "SYNC";
    case MODE_WAVE: return "WAVE";
    case MODE_CHASE: return "CHASE";
    case MODE_RANDOM: return "RANDOM";
    case MODE_ALERT: return "ALERT";
    default: return "UNKNOWN";
  }
}

void printHelp() {
  Serial.println();
  Serial.println("=== MICROBOT SYSTEM - SERIAL COMMANDS ===");
  Serial.println("0 -> OFF");
  Serial.println("1 -> SYNC");
  Serial.println("2 -> WAVE");
  Serial.println("3 -> CHASE");
  Serial.println("4 -> RANDOM");
  Serial.println("5 -> ALERT");
  Serial.println("s -> STATUS");
  Serial.println("h -> HELP");
  Serial.println("=========================================");
  Serial.println();
}

void printStatus() {
  Serial.println();
  Serial.println("=== MICROBOT SYSTEM STATUS ===");
  Serial.print("Mode: ");
  Serial.println(modeToString(currentMode));
  Serial.print("Nodes: ");
  Serial.println(NUM_NODES);
  Serial.print("Baud rate: ");
  Serial.println(115200);
  Serial.println("==============================");
  Serial.println();
}

void resetModeState() {
  clearAllNodes();

  syncState = false;
  lastSyncToggleMs = 0;

  waveIndex = 0;
  lastWaveStepMs = 0;

  chaseIndex = 0;
  lastChaseStepMs = 0;

  lastRandomStepMs = 0;

  alertState = false;
  lastAlertToggleMs = 0;
}

void setMode(SystemMode newMode) {
  currentMode = newMode;
  resetModeState();

  Serial.print("Mode changed to: ");
  Serial.println(modeToString(currentMode));
}

void handleSerial() {
  while (Serial.available() > 0) {
    char cmd = Serial.read();

    switch (cmd) {
      case '0':
        setMode(MODE_OFF);
        break;
      case '1':
        setMode(MODE_SYNC);
        break;
      case '2':
        setMode(MODE_WAVE);
        break;
      case '3':
        setMode(MODE_CHASE);
        break;
      case '4':
        setMode(MODE_RANDOM);
        break;
      case '5':
        setMode(MODE_ALERT);
        break;
      case 's':
      case 'S':
        printStatus();
        break;
      case 'h':
      case 'H':
        printHelp();
        break;
      case '\n':
      case '\r':
        break;
      default:
        Serial.print("Unknown command: ");
        Serial.println(cmd);
        Serial.println("Press 'h' for help.");
        break;
    }
  }
}

void runModeOff() {
  clearAllNodes();
}

void runModeSync() {
  if (nowMs - lastSyncToggleMs >= SYNC_INTERVAL) {
    lastSyncToggleMs = nowMs;
    syncState = !syncState;
    setAllNodes(syncState);
  }
}

void runModeWave() {
  if (nowMs - lastWaveStepMs >= WAVE_INTERVAL) {
    lastWaveStepMs = nowMs;

    clearAllNodes();
    digitalWrite(NODE_PINS[waveIndex], HIGH);

    waveIndex++;
    if (waveIndex >= NUM_NODES) {
      waveIndex = 0;
    }
  }
}

void runModeChase() {
  if (nowMs - lastChaseStepMs >= CHASE_INTERVAL) {
    lastChaseStepMs = nowMs;

    clearAllNodes();

    digitalWrite(NODE_PINS[chaseIndex], HIGH);

    int previousIndex = chaseIndex - 1;
    if (previousIndex < 0) {
      previousIndex = NUM_NODES - 1;
    }

    digitalWrite(NODE_PINS[previousIndex], HIGH);

    chaseIndex++;
    if (chaseIndex >= NUM_NODES) {
      chaseIndex = 0;
    }
  }
}

void runModeRandom() {
  if (nowMs - lastRandomStepMs >= RANDOM_INTERVAL) {
    lastRandomStepMs = nowMs;

    for (int i = 0; i < NUM_NODES; i++) {
      digitalWrite(NODE_PINS[i], random(0, 2));
    }
  }
}

void runModeAlert() {
  if (nowMs - lastAlertToggleMs >= ALERT_INTERVAL) {
    lastAlertToggleMs = nowMs;
    alertState = !alertState;
    setAllNodes(alertState);
  }
}

void setup() {
  Serial.begin(115200);
  delay(400);

  for (int i = 0; i < NUM_NODES; i++) {
    pinMode(NODE_PINS[i], OUTPUT);
    digitalWrite(NODE_PINS[i], LOW);
  }

  randomSeed(analogRead(34));

  Serial.println();
  Serial.println("=========================================");
  Serial.println("      MICROBOT SYSTEM - HW PROTOTYPE     ");
  Serial.println("=========================================");
  Serial.println("Boot complete.");
  printHelp();
  printStatus();
}

void loop() {
  nowMs = millis();

  handleSerial();

  if (nowMs - lastFrameMs >= FRAME_INTERVAL) {
    lastFrameMs = nowMs;

    switch (currentMode) {
      case MODE_OFF:
        runModeOff();
        break;
      case MODE_SYNC:
        runModeSync();
        break;
      case MODE_WAVE:
        runModeWave();
        break;
      case MODE_CHASE:
        runModeChase();
        break;
      case MODE_RANDOM:
        runModeRandom();
        break;
      case MODE_ALERT:
        runModeAlert();
        break;
      default:
        runModeOff();
        break;
    }
  }
}
