(function () {
  var FETCH_TIMEOUT_MS = 8000;
  var DEFAULT_URL =
    "https://raw.githubusercontent.com/AaltoSciComp/triton-skills/main/triton-rules.md";
  var FALLBACK_URL =
    "https://cdn.jsdelivr.net/gh/AaltoSciComp/triton-skills@main/triton-rules.md";
  var SOURCE_PAGE =
    "https://github.com/AaltoSciComp/triton-skills/blob/main/triton-rules.md";

  function escapeHtml(value) {
    return value
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function fetchWithTimeout(url, timeoutMs) {
    var controller = new AbortController();
    var timer = setTimeout(function () {
      controller.abort();
    }, timeoutMs);

    return fetch(url, { signal: controller.signal }).finally(function () {
      clearTimeout(timer);
    });
  }

  function renderRules(container, text) {
    container.innerHTML = [
      '<p class="triton-rules-source">',
      'Live copy of <a href="' + SOURCE_PAGE + '">triton-rules.md</a> :',
      "</p>",
      '<div class="highlight-text notranslate">',
      '<div class="highlight">',
      "<pre>" + escapeHtml(text.replace(/\r\n/g, "\n").replace(/\s+$/, "") + "\n") + "</pre>",
      "</div>",
      "</div>",
    ].join("");
  }

  function renderError(container) {
    container.innerHTML = [
      '<p class="triton-rules-error">',
      "Unable to load the current Triton agent rules. ",
      'See <a href="' + SOURCE_PAGE + '">triton-rules.md on GitHub</a> ',
      "or <code>/scratch/shareddata/triton-skills/triton-rules.md</code> on Triton.",
      "</p>",
    ].join("");
  }

  function loadFrom(url) {
    return fetchWithTimeout(url, FETCH_TIMEOUT_MS).then(function (response) {
      if (!response.ok) {
        throw new Error("Unexpected status " + response.status);
      }
      return response.text();
    });
  }

  function loadRules() {
    var containers = document.querySelectorAll("[data-triton-rules]");
    if (!containers.length) {
      return;
    }

    containers.forEach(function (container) {
      var rulesUrl = container.getAttribute("data-rules-url") || DEFAULT_URL;
      container.innerHTML = "<p>Loading current Triton agent rules...</p>";

      loadFrom(rulesUrl)
        .catch(function () {
          if (rulesUrl === FALLBACK_URL) {
            throw new Error("fallback already tried");
          }
          return loadFrom(FALLBACK_URL);
        })
        .then(function (text) {
          if (!text || !String(text).trim()) {
            throw new Error("empty rules file");
          }
          renderRules(container, String(text));
        })
        .catch(function () {
          renderError(container);
        });
    });
  }

  document.addEventListener("DOMContentLoaded", loadRules);
})();
