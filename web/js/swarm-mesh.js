document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("swarmCanvas");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  const width = canvas.width;
  const height = canvas.height;

  const nodeCount = 16;
  const linkDistance = 110;
  const maxSpeed = 1.1;

  const nodes = Array.from({ length: nodeCount }, (_, index) => ({
    id: index,
    x: Math.random() * width,
    y: Math.random() * height,
    vx: (Math.random() - 0.5) * maxSpeed * 2,
    vy: (Math.random() - 0.5) * maxSpeed * 2,
  }));

  function distance(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  function update() {
    for (const node of nodes) {
      node.x += node.vx;
      node.y += node.vy;

      if (node.x < 0 || node.x > width) node.vx *= -1;
      if (node.y < 0 || node.y > height) node.vy *= -1;

      node.x = Math.max(0, Math.min(width, node.x));
      node.y = Math.max(0, Math.min(height, node.y));
    }
  }

  function drawBackground() {
    const gradient = ctx.createLinearGradient(0, 0, 0, height);
    gradient.addColorStop(0, "rgba(12, 18, 32, 1)");
    gradient.addColorStop(1, "rgba(7, 11, 20, 1)");
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, width, height);
  }

  function drawLinks() {
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i];
        const b = nodes[j];
        const d = distance(a, b);

        if (d < linkDistance) {
          const alpha = 1 - d / linkDistance;
          ctx.strokeStyle = `rgba(80, 160, 255, ${alpha * 0.35})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }
  }

  function drawNodes() {
    for (const node of nodes) {
      ctx.beginPath();
      ctx.fillStyle = "rgba(53, 214, 255, 0.95)";
      ctx.arc(node.x, node.y, 4, 0, Math.PI * 2);
      ctx.fill();

      ctx.beginPath();
      ctx.fillStyle = "rgba(53, 214, 255, 0.12)";
      ctx.arc(node.x, node.y, 10, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function animate() {
    update();
    drawBackground();
    drawLinks();
    drawNodes();
    requestAnimationFrame(animate);
  }

  animate();
});
