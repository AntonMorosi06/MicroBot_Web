document.addEventListener("DOMContentLoaded", () => {
  initializeDashboard();
});

function initializeDashboard() {
  const activeNodes = document.getElementById("dashboard-active-nodes");
  const mode = document.getElementById("dashboard-mode");
  const coherence = document.getElementById("dashboard-coherence");
  const networkStatus = document.getElementById("dashboard-network-status");
  const systemNote = document.getElementById("dashboard-system-note");

  if (!activeNodes || !mode || !coherence || !networkStatus || !systemNote) {
    return;
  }

  const dashboardState = {
    activeNodes: 16,
    mode: "Flocking",
    coherence: "82%",
    networkStatus: "Prototype-level connectivity",
    systemNote:
      "The current configuration demonstrates modular architecture and swarm logic, while full integration between simulation, web, and hardware remains a future step.",
  };

  activeNodes.textContent = String(dashboardState.activeNodes);
  mode.textContent = dashboardState.mode;
  coherence.textContent = dashboardState.coherence;
  networkStatus.textContent = dashboardState.networkStatus;
  systemNote.textContent = dashboardState.systemNote;
}
