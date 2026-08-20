(function () {
  function escapeHtml(value) {
    return value
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function renderTable(container, models) {
    var rows = models
      .slice()
      .sort(function (left, right) {
        return left.id.localeCompare(right.id);
      })
      .map(function (model) {
        var modelId = escapeHtml(model.id);
        var modelUrl = "https://huggingface.co/" + encodeURI(model.id);

        return [
          "<tr>",
          "<td><code>" + modelId + "</code></td>",
          '<td><a href="' + modelUrl + '">Model card</a></td>',
          "</tr>",
        ].join("");
      })
      .join("");

    container.innerHTML = [
      '<div class="wy-table-responsive">',
      '<table class="docutils align-default">',
      "<thead>",
      "<tr><th>Model</th><th>HuggingFace</th></tr>",
      "</thead>",
      "<tbody>",
      rows,
      "</tbody>",
      "</table>",
      "</div>",
    ].join("");
  }

  function renderError(container) {
    container.innerHTML = [
      '<p class="llm-models-error">',
      'Unable to load the current model list from the gateway. ',
      '<a href="https://llm-gateway.k8s.aalto.fi/docs">Check the API docs</a>.',
      "</p>",
    ].join("");
  }

  function loadModels() {
    var container = document.querySelector("[data-llm-model-table]");
    if (!container) {
      return;
    }

    var modelsUrl = container.getAttribute("data-models-url");
    container.innerHTML = "<p>Loading current model list...</p>";

    fetch(modelsUrl)
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
        renderTable(container, models);
      })
      .catch(function () {
        renderError(container);
      });
  }

  document.addEventListener("DOMContentLoaded", loadModels);
})();