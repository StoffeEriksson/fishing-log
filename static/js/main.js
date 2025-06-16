// Automatically fade out alert messages after 3 seconds
setTimeout(() => {
  document.querySelectorAll(".custom-alert").forEach((alert) => {
    alert.style.opacity = "0";
    setTimeout(() => alert.remove(), 500); // Remove element after fade-out
  });
}, 3000);

// When the page has loaded
document.addEventListener("DOMContentLoaded", function () {
  // If global variables for species chart exist, draw it
  if (window.speciesLabels && window.speciesCounts) {
    drawCatchChart(window.speciesLabels, window.speciesCounts);
  }

  // If global variables for monthly chart exist, draw it
  if (window.monthLabels && window.monthCounts) {
    drawMonthChart(window.monthLabels, window.monthCounts);
  }

  // Initialize the dynamic catch input logic
  setupDynamicCatchForm();
});

/**
 * Render a bar chart of total catches per species
 */
function drawCatchChart(labels, data) {
  const ctx = document.getElementById("catchChart").getContext("2d");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Total Catches",
          data: data.map((v) => Math.round(v)), // Round values for cleaner bars
          backgroundColor: "orange",
          borderColor: "darkorange",
          borderWidth: 2,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            color: "#fff",
            precision: 0,
          },
          grid: {
            color: "rgba(255, 255, 255, 0.2)",
          },
        },
        x: {
          ticks: { color: "#fff" },
          grid: { color: "rgba(255, 255, 255, 0.2)" },
        },
      },
      plugins: {
        legend: {
          labels: { color: "white" },
        },
      },
    },
  });
}

/**
 * Render a line chart of total catches per month
 */
function drawMonthChart(labels, data) {
  const ctx = document.getElementById("monthChart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Catches per Month",
          data: data,
          fill: true,
          backgroundColor: "rgba(255,165,0,0.2)", // Light orange fill
          borderColor: "orange",
          tension: 0.3, // Smooth curve
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          ticks: { stepSize: 1, precision: 0, color: "#fff" },
          grid: { color: "rgba(255,255,255,0.2)" },
        },
        x: {
          ticks: { color: "#fff" },
          grid: { color: "rgba(255,255,255,0.2)" },
        },
      },
      plugins: {
        legend: {
          labels: { color: "#fff" },
        },
      },
    },
  });
}

/**
 * Setup dynamic form for adding multiple catches in one session
 */
function setupDynamicCatchForm() {
  const addBtn = document.getElementById("add-catch");
  const speciesInput = document.getElementById("species-input");
  const countInput = document.getElementById("count-input");
  const listContainer = document.getElementById("catch-preview"); // For visual preview
  const formContainer = document.getElementById("catch-formset"); // For hidden inputs
  const totalForms = document.getElementById("id_form-TOTAL_FORMS"); // Tracks how many forms exist

  // Abort if any required element is missing
  if (
    !addBtn ||
    !speciesInput ||
    !countInput ||
    !listContainer ||
    !formContainer ||
    !totalForms
  ) {
    return;
  }

  // When user clicks "Add" catch
  addBtn.addEventListener("click", () => {
    const species = speciesInput.value;
    const count = parseInt(countInput.value, 10);
    if (!species || isNaN(count) || count <= 0) return;

    const index = parseInt(totalForms.value, 10);
    totalForms.value = index + 1;

    // Create visual preview of added catch
    const displayName = speciesInput.options[speciesInput.selectedIndex].text;
    const wrapper = document.createElement("div");
    wrapper.className = "faded-catch mb-2";
    wrapper.innerHTML = `
      <span>${displayName} – ${count} pcs</span>
      <button type="button" class="remove-catch btn btn-sm btn-danger ms-2">❌</button>
    `;
    listContainer.appendChild(wrapper);

    // Create hidden inputs to submit with the form
    const hiddenSpecies = document.createElement("input");
    hiddenSpecies.type = "hidden";
    hiddenSpecies.name = `form-${index}-species`;
    hiddenSpecies.value = species;

    const hiddenCount = document.createElement("input");
    hiddenCount.type = "hidden";
    hiddenCount.name = `form-${index}-count`;
    hiddenCount.value = count;

    formContainer.appendChild(hiddenSpecies);
    formContainer.appendChild(hiddenCount);

    // Clear input fields
    speciesInput.selectedIndex = 0;
    countInput.value = "";

    // When user clicks remove this catch
    wrapper.querySelector(".remove-catch").addEventListener("click", () => {
      wrapper.remove();
      hiddenSpecies.remove();
      hiddenCount.remove();
      updateFormCount(); // Update form count after removal
    });
  });

  /**
   * Recalculate total number of catch forms based on remaining inputs
   */
  function updateFormCount() {
    const inputs = formContainer.querySelectorAll('input[name$="-species"]');
    totalForms.value = inputs.length;
  }
}
