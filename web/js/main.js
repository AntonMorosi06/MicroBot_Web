document.addEventListener("DOMContentLoaded", () => {
  initializeHeroStats();
  initializeSmoothState();
});

function initializeHeroStats() {
  const nodes = document.getElementById("stat-nodes");
  const mode = document.getElementById("stat-mode");
  const status = document.getElementById("stat-status");

  if (!nodes || !mode || !status) return;

  nodes.textContent = "16";
  mode.textContent = "Flocking";
  status.textContent = "Prototype";
}

function initializeSmoothState() {
  document.body.classList.add("is-ready");
}
