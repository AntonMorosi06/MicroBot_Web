document.addEventListener("DOMContentLoaded", () => {
  initializeSimulationState();
});

function initializeSimulationState() {
  const state = {
    modes: {
      Alignment: {
        activeNodes: 16,
        coherenceBase: 0.74,
        neighborsBase: 4.4,
        speedBase: 1.62,
        note: "The current representation emphasizes directional consistency through local velocity alignment.",
      },
      Flocking: {
        activeNodes: 16,
        coherenceBase: 0.82,
        neighborsBase: 5.2,
        speedBase: 1.84,
        note: "The current configuration represents a balanced swarm behavior model based on alignment, cohesion, and separation.",
      },
      Disorder: {
        activeNodes: 16,
        coherenceBase: 0.31,
        neighborsBase: 2.6,
        speedBase: 1.95,
        note: "The current state emphasizes low-coherence independent motion, useful as a contrast against coordinated swarm behavior.",
      },
    },
    currentMode: "Flocking",
    centerOfMass: {
      x: 640,
      y: 360,
    },
  };

  const modeSelector = document.getElementById("modeSelector");
  if (modeSelector) {
    modeSelector.addEventListener("change", (event) => {
      state.currentMode = event.target.value;
      applySimulationState(state);
    });
  }

  applySimulationState(state);
  startMetricDrift(state);

  window.microbotSimulationState = state;
}

function applySimulationState(state) {
  const modeData = state.modes[state.currentMode];

  setText("stat-nodes", modeData.activeNodes);
  setText("stat-mode", state.currentMode);

  setText("dashboard-active-nodes", modeData.activeNodes);
  setText("dashboard-mode", state.currentMode);
  setText("dashboard-coherence", `${(modeData.coherenceBase * 100).toFixed(1)}%`);
  setText("dashboard-neighbors", modeData.neighborsBase.toFixed(1));
  setText("dashboard-speed", modeData.speedBase.toFixed(2));
  setText("dashboard-com-x", Math.round(state.centerOfMass.x));
  setText("dashboard-com-y", Math.round(state.centerOfMass.y));
  setText("dashboard-network-status", "Prototype-level connectivity");
  setText("dashboard-system-note", modeData.note);
}

function startMetricDrift(state) {
  setInterval(() => {
    const modeData = state.modes[state.currentMode];

    const coherence = vary(modeData.coherenceBase, 0.02, 0, 1);
    const neighbors = vary(modeData.neighborsBase, 0.3, 0, 20);
    const speed = vary(modeData.speedBase, 0.08, 0, 10);

    state.centerOfMass.x = vary(state.centerOfMass.x, 8, 80, 1200);
    state.centerOfMass.y = vary(state.centerOfMass.y, 6, 80, 680);

    setText("dashboard-coherence", `${(coherence * 100).toFixed(1)}%`);
    setText("dashboard-neighbors", neighbors.toFixed(1));
    setText("dashboard-speed", speed.toFixed(2));
    setText("dashboard-com-x", Math.round(state.centerOfMass.x));
    setText("dashboard-com-y", Math.round(state.centerOfMass.y));
  }, 900);
}

function vary(base, range, min, max) {
  const value = base + (Math.random() * 2 - 1) * range;
  return Math.max(min, Math.min(max, value));
}

function setText(id, value) {
  const element = document.getElementById(id);
  if (element) {
    element.textContent = String(value);
  }
}
