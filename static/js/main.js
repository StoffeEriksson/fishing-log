// Auto-fade messages
setTimeout(() => {
  document.querySelectorAll(".custom-alert").forEach((alert) => {
    alert.style.opacity = "0";
    setTimeout(() => alert.remove(), 500);
  });
}, 3000);

// Shows statitics
document.addEventListener("DOMContentLoaded", function () {
  if (window.speciesLabels && window.speciesCounts) {
    drawCatchChart(window.speciesLabels, window.speciesCounts);
  }
  if (window.monthLabels && window.monthCounts) {
    drawMonthChart(window.monthLabels, window.monthCounts);
  }

  setupDynamicCatchForm();
});

// Function to display the catch chart
function drawCatchChart(labels, data) {
  const ctx = document.getElementById("catchChart").getContext("2d");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Total Catches",
          data: data.map((v) => Math.round(v)),
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

// Function to display monthly chart
function drawMonthChart(labels, data) {
  const ctx = document.getElementById("monthChart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Fångst per månad",
          data: data,
          fill: true,
          backgroundColor: "rgba(255,165,0,0.2)",
          borderColor: "orange",
          tension: 0.3,
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

// Dynamic catch form
function setupDynamicCatchForm() {
  const addBtn = document.getElementById("add-catch");
  const speciesInput = document.getElementById("species-input");
  const countInput = document.getElementById("count-input");
  const listContainer = document.getElementById("catch-preview");
  const formContainer = document.getElementById("catch-formset");
  const totalForms = document.getElementById("id_form-TOTAL_FORMS");

  if (
    !addBtn ||
    !speciesInput ||
    !countInput ||
    !listContainer ||
    !formContainer ||
    !totalForms
  )
    return;

  addBtn.addEventListener("click", () => {
    const species = speciesInput.value;
    const count = parseInt(countInput.value);
    if (!species || isNaN(count) || count <= 0) return;

    const index = parseInt(totalForms.value);
    totalForms.value = index + 1;

    // Shows the preview
    const displayName = speciesInput.options[speciesInput.selectedIndex].text;
    const wrapper = document.createElement("div");
    wrapper.className = "faded-catch mb-2";
    wrapper.innerHTML = `
      <span>${displayName} – ${count} st</span>
      <button type="button" class="remove-catch btn btn-sm btn-danger ms-2">❌</button>
    `;
    listContainer.appendChild(wrapper);

    // creates the hidden chart
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

    // Clear inputs
    speciesInput.selectedIndex = 0;
    countInput.value = "";

    // Removes catch
    wrapper.querySelector(".remove-catch").addEventListener("click", () => {
      wrapper.remove();
      hiddenSpecies.remove();
      hiddenCount.remove();
      updateFormCount();
    });
  });

  // Function updates form
  function updateFormCount() {
    const inputs = formContainer.querySelectorAll('input[name$="-species"]');
    totalForms.value = inputs.length;
  }
}
