(function () {
  var scriptEl = document.currentScript;
  var FETCH_TIMEOUT_MS = 5000;

  function escapeHtml(value) {
    return value
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function tableHtml(models) {
    console.log(models)
    var rows = models
      .slice()
      .sort(function (left, right) {
        return left.model.id.localeCompare(right.model.id);
      })
      .map(function (model) {
        var modelId = escapeHtml(model.model.id);
        var modelUrl = "https://huggingface.co/" + encodeURI(model.model.id);
        var maxTokens = model.description.toLowerCase().match(/context length (\d+) tokens/) 
        var alwaysOn = model.description.toLowerCase().includes("always on") ? "Yes" : "No";
        return [
          "<tr>",
          "<td><code>" + modelId + "</code></td>",
          '<td><a href="' + modelUrl + '">Model card</a></td>',
          "<td>" + (maxTokens ? maxTokens[1] : "N/A") + "</td>",
          "<td>" + alwaysOn + "</td>",
          "</tr>",
        ].join("");
      })
      .join("");

    return [
      '<div class="wy-table-responsive">',
      '<table class="docutils align-default">',
      "<thead>",
      "<tr><th>Model</th><th>HuggingFace</th><th>Max tokens</th><th>Always on</th></tr>",
      "</thead>",
      "<tbody>",
      rows,
      "</tbody>",
      "</table>",
      "</div>",
    ].join("");
  }

  function renderTable(container, models) {
    container.innerHTML = tableHtml(models);
  }

  function renderFallbackTable(container, models) {
    container.innerHTML = [
      '<p class="llm-models-fallback-note">',
      "Showing a locally cached model list because the live gateway did not respond. ",
      '<a href="https://llm-gateway.k8s.aalto.fi/api/v1/modelinfos">Check the API docs</a> for the current list.',
      "</p>",
      tableHtml(models),
    ].join("");
  }

  function renderError(container) {
    container.innerHTML = [
      '<p class="llm-models-error">',
      'Unable to load the current model list from the gateway. ',
      '<a href="https://llm-gateway.k8s.aalto.fi/api/v1/modelinfos">Check the API docs</a>.',
      "</p>",
    ].join("");
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

  function loadFallback(container) {
    if (!scriptEl) {
      renderError(container);
      return;
    }

    var fallbackUrl = new URL("models.json", scriptEl.src).href;

    fetch(fallbackUrl)
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Unexpected status " + response.status);
        }
        return response.json();
      })
      .then(function (models) {
        if (!Array.isArray(models)) {
          throw new Error("Model response was not an array");
        }
        renderFallbackTable(container, models);
      })
      .catch(function (err) {
        console.error(err)
        renderError(container);
      });
  }

  function loadModels() {
    var container = document.querySelector("[data-llm-model-table]");
    console.log("Loading models into container:", container);
    if (!container) {
      return;
    }
    console.log("Fetching models from URL:", container.getAttribute("data-models-url"));
    var modelsUrl = container.getAttribute("data-models-url");
    container.innerHTML = "<p>Loading current model list...</p>";

    fetchWithTimeout(modelsUrl, FETCH_TIMEOUT_MS)
      .then(function (response) {
        console.log("Fetched models response:", response);
        if (!response.ok) {          
          throw new Error("Unexpected status " + response.status);
        }
        return response.json();
      })
      .then(function (models) {
        console.log("Fetched models:", models);
        if (!Array.isArray(models)) {
          throw new Error("Model response was not an array");
        }
        renderTable(container, models);
      })
      .catch(function () {
        loadFallback(container);
      });
  }

  document.addEventListener("DOMContentLoaded", loadModels);
})();