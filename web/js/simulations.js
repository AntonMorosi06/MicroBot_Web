document.addEventListener("DOMContentLoaded", () => {
  initializeSimulationState();
});

function initializeSimulationState() {
  const state = {
    modes: ["Alignment", "Flocking", "Disorder"],
    currentModeIndex: 1,
    nodeCount: 16,
    coherenceValues: {
      Alignment: "74%",
      Flocking: "82%",
      Disorder: "31%",
    },
  };

  applySimulationState(state);

  window.microbotSimulationState = state;
}

function applySimulationState(state) {
  const currentMode = state.modes[state.currentModeIndex];

  const heroMode = document.getElementById("stat-mode");
  const heroNodes = document.getElementById("stat-nodes");

  const dashboardMode = document.getElementById("dashboard-mode");
  const dashboardNodes = document.getElementById("dashboard-active-nodes");
  const dashboardCoherence = document.getElementById("dashboard-coherence");
  const dashboardNote = document.getElementById("dashboard-system-note");

  if (heroMode) heroMode.textContent = currentMode;
  if (heroNodes) heroNodes.textContent = String(state.nodeCount);

  if (dashboardMode) dashboardMode.textContent = currentMode;
  if (dashboardNodes) dashboardNodes.textContent = String(state.nodeCount);

  if (dashboardCoherence) {
    dashboardCoherence.textContent = state.coherenceValues[currentMode] || "N/A";
  }

  if (dashboardNote) {
    dashboardNote.textContent = buildModeNote(currentMode);
  }
}

function buildModeNote(mode) {
  if (mode === "Alignment") {
    return "The current representation emphasizes directional consistency between nodes through local velocity alignment.";
  }

  if (mode === "Flocking") {
    return "The current configuration represents the most balanced collective behavior, combining alignment, cohesion, and separation.";
  }

  if (mode === "Disorder") {
    return "The current state emphasizes low-coherence independent motion, useful as a contrast against coordinated swarm behavior.";
  }

  return "The current configuration demonstrates modular architecture and swarm logic.";
}
