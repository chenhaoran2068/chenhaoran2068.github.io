(() => {
  const root = document.querySelector("[data-system-route-interactive]");
  const dataNode = document.getElementById("system-route-data");
  if (!root || !dataNode) return;

  let content;
  try {
    content = JSON.parse(dataNode.textContent);
  } catch {
    return;
  }

  const stages = content.stages || {};
  const labels = content.labels || {};
  const stageTitle = document.getElementById("stage-inspector-title");
  const stagePrecondition = document.getElementById("stage-inspector-precondition");
  const stageStartLabel = document.getElementById("stage-inspector-start-label");
  const stageStart = document.getElementById("stage-inspector-start");
  const stageWorkLabel = document.getElementById("stage-inspector-work-label");
  const stageWork = document.getElementById("stage-inspector-work");
  const stageNextLabel = document.getElementById("stage-inspector-next-label");
  const stageNext = document.getElementById("stage-inspector-next");
  const stageNextRow = document.getElementById("stage-inspector-next-row");
  const stageInspector = root.querySelector(".system-route-inspector");
  const stageEntries = root.querySelectorAll("[data-stage-key]");
  const systemFlow = root.querySelector("[data-system-flow]");

  const selectStage = (key, revealInspector = false) => {
    const entry = stages[key];
    if (!entry) return;

    stageTitle.textContent = entry.title;
    stagePrecondition.textContent = entry.precondition || "";
    stagePrecondition.hidden = !entry.precondition;
    stageStartLabel.textContent = entry.startLabel || labels.start || "Start";
    stageStart.textContent = entry.start || "";
    stageWorkLabel.textContent = entry.workLabel || labels.work || "At this stage";
    stageWork.textContent = entry.work || "";
    stageNextLabel.textContent = entry.nextLabel || labels.next || "Next";
    stageNext.textContent = entry.next || "";
    stageNextRow.hidden = !entry.next;

    stageEntries.forEach((element) => {
      element.classList.toggle("is-selected", element.dataset.stageKey === key);
    });

    if (!revealInspector) return;
    requestAnimationFrame(() => {
      if (window.matchMedia("(max-width: 760px)").matches) {
        (stageInspector || stageTitle).scrollIntoView({ block: "start", behavior: "auto" });
        return;
      }
      if (!stageInspector) return;
      const stickyTop = Number.parseFloat(getComputedStyle(stageInspector).top) || 0;
      const currentTop = stageInspector.getBoundingClientRect().top;
      if (currentTop < stickyTop) {
        window.scrollBy({ top: currentTop - stickyTop, behavior: "auto" });
      }
    });
  };

  const drawSystemFlow = () => {
    if (!systemFlow) return;
    const canvas = systemFlow.querySelector(".system-flow-connectors");
    const paths = systemFlow.querySelector("[data-system-flow-paths]");
    const labelLayer = systemFlow.querySelector(".system-flow-return-labels");
    const rootBox = systemFlow.getBoundingClientRect();
    if (!canvas || !paths || !labelLayer || rootBox.width === 0 || rootBox.height === 0) return;

    const nodeBox = (key) => {
      const node = systemFlow.querySelector(`[data-flow-node="${key}"]`);
      if (!node) return null;
      const box = node.getBoundingClientRect();
      return {
        left: box.left - rootBox.left,
        right: box.right - rootBox.left,
        top: box.top - rootBox.top,
        bottom: box.bottom - rootBox.top,
        centerX: box.left - rootBox.left + box.width / 2,
        centerY: box.top - rootBox.top + box.height / 2,
      };
    };
    const namespace = "http://www.w3.org/2000/svg";
    const addPath = (className, d) => {
      const path = document.createElementNS(namespace, "path");
      path.setAttribute("class", className);
      path.setAttribute("d", d);
      paths.appendChild(path);
    };
    const addLabel = (label, x, y) => {
      const text = document.createElement("span");
      text.className = "system-flow-return-label";
      text.style.left = `${Math.max(2, x)}px`;
      text.style.top = `${Math.max(2, y)}px`;
      text.textContent = label;
      labelLayer.appendChild(text);
    };
    const forward = (fromKey, toKey) => {
      const from = nodeBox(fromKey);
      const to = nodeBox(toKey);
      if (!from || !to) return;
      const movingDown = to.centerY >= from.centerY;
      const startY = movingDown ? from.bottom : from.top;
      const endY = movingDown ? to.top : to.bottom;
      const gap = Math.max(16, Math.abs(endY - startY) / 2);
      addPath(
        "system-flow-path-forward",
        `M ${from.centerX} ${startY} C ${from.centerX} ${startY + (movingDown ? gap : -gap)} ${to.centerX} ${endY - (movingDown ? gap : -gap)} ${to.centerX} ${endY}`,
      );
    };
    const returnTo = (fromKey, toKey, railIndex, label) => {
      const from = nodeBox(fromKey);
      const to = nodeBox(toKey);
      if (!from || !to) return;
      const rail = 8 + railIndex * 9;
      addPath("system-flow-path-return", `M ${from.left} ${from.centerY} H ${rail} V ${to.centerY} H ${to.left}`);
      addLabel(label, rail + 3, (from.centerY + to.centerY) / 2 - 8);
    };
    const stopAt = (fromKey, toKey) => {
      const from = nodeBox(fromKey);
      const to = nodeBox(toKey);
      if (!from || !to) return;
      addPath("system-flow-path-stop", `M ${from.right} ${from.centerY} H ${to.left}`);
    };

    paths.replaceChildren();
    labelLayer.replaceChildren();
    canvas.setAttribute("viewBox", `0 0 ${rootBox.width} ${rootBox.height}`);
    canvas.setAttribute("width", String(rootBox.width));
    canvas.setAttribute("height", String(rootBox.height));

    [["3", "4"], ["4", "5"], ["5", "key-part"], ["key-part", "feasibility-decision"], ["feasibility-decision", "6"], ["6", "7"], ["7", "8"], ["8", "9"], ["9", "10"], ["10", "11"]].forEach(([from, to]) => forward(from, to));
    const returns = labels.returns || [];
    returnTo("4", "3", 0, returns[0] || "Redesign");
    returnTo("feasibility-decision", "3", 1, returns[1] || "Redesign");
    returnTo("8", "6", 2, returns[2] || "Correct");
    returnTo("10", "4", 3, returns[3] || "Revise design");
    returnTo("10", "6", 4, returns[4] || "Add analysis");
    returnTo("10", "8", 5, returns[5] || "Review again");
    stopAt("feasibility-decision", "stop");
  };

  stageEntries.forEach((element) => {
    element.addEventListener("click", () => selectStage(element.dataset.stageKey, true));
    element.addEventListener("focus", () => selectStage(element.dataset.stageKey));
  });
  window.addEventListener("resize", drawSystemFlow);
  root.querySelector(".system-mode-collaborative")?.addEventListener("toggle", () => requestAnimationFrame(drawSystemFlow));
  selectStage("1");
  requestAnimationFrame(drawSystemFlow);
})();
