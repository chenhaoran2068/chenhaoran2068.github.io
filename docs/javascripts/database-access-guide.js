(function () {
  "use strict";

  function initializeTabs(root) {
    var tabs = Array.prototype.slice.call(
      root.querySelectorAll('[role="tab"][data-tab-target]')
    );
    var panels = Array.prototype.slice.call(
      root.querySelectorAll("[data-tab-panel]")
    );

    function activate(tab) {
      var targetId = tab.getAttribute("data-tab-target");
      tabs.forEach(function (item) {
        var selected = item === tab;
        item.setAttribute("aria-selected", selected ? "true" : "false");
        item.tabIndex = selected ? 0 : -1;
      });
      panels.forEach(function (panel) {
        panel.hidden = panel.id !== targetId;
      });
    }

    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () {
        activate(tab);
      });
      tab.addEventListener("keydown", function (event) {
        var previous = event.key === "ArrowLeft" || event.key === "ArrowUp";
        var nextKey = event.key === "ArrowRight" || event.key === "ArrowDown";
        if (!previous && !nextKey) {
          return;
        }
        event.preventDefault();
        var offset = nextKey ? 1 : -1;
        var next = tabs[(index + offset + tabs.length) % tabs.length];
        activate(next);
        next.focus();
      });
    });

    var selected = tabs.find(function (tab) {
      return tab.getAttribute("aria-selected") === "true";
    });
    if (selected) {
      activate(selected);
    }
  }

  function initializeCopyButtons(page) {
    var copyLabel = page.getAttribute("data-copy-label") || "Copy";
    var copiedLabel = page.getAttribute("data-copied-label") || "Copied";

    page.querySelectorAll("pre[data-copy]").forEach(function (pre) {
      var blockCopyLabel = pre.getAttribute("data-copy-label") || copyLabel;
      var blockCopiedLabel = pre.getAttribute("data-copied-label") || copiedLabel;
      var shell = document.createElement("div");
      shell.className = "code-block-shell";
      pre.parentNode.insertBefore(shell, pre);
      shell.appendChild(pre);

      var button = document.createElement("button");
      button.type = "button";
      button.className = "code-copy-button";
      button.textContent = blockCopyLabel;
      button.setAttribute("aria-label", blockCopyLabel);
      button.addEventListener("click", function () {
        var code = pre.querySelector("code");
        if (!code || !navigator.clipboard) {
          return;
        }
        navigator.clipboard.writeText(code.textContent).then(function () {
          button.textContent = blockCopiedLabel;
          window.setTimeout(function () {
            button.textContent = blockCopyLabel;
          }, 1600);
        });
      });
      shell.appendChild(button);
    });
  }

  document.querySelectorAll(".database-access-guide").forEach(function (page) {
    page.querySelectorAll("[data-os-tabs], [data-db-tabs]").forEach(initializeTabs);
    initializeCopyButtons(page);
  });
})();
