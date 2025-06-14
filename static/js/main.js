// Auto-fade messages after a few seconds
setTimeout(function () {
  const alerts = document.querySelectorAll('.custom-alert');
  alerts.forEach((alert) => {
    alert.style.opacity = '0';
    setTimeout(() => alert.remove(), 500); // Remove after fade-out
  });
}, 3000);


// updates chart
function drawCatchChart(labels, data) {
    // Se till att alla datavärden är heltal (avrundat)
    const roundedData = data.map(value => Math.round(value));

    const ctx = document.getElementById('catchChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Total Catches',
                data: roundedData,
                backgroundColor: 'orange',
                borderColor: 'darkorange',
                borderWidth: 2,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: '#fff',
                        precision: 0 // Viktigt: visa bara heltal
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.2)',
                    }
                },
                x: {
                    ticks: {
                        color: '#fff',
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.2)',
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: 'white'
                    }
                }
            }
        }
    });
}

// Kör funktionen när DOM är redo och grafdata finns
document.addEventListener('DOMContentLoaded', function () {
    if (window.speciesLabels && window.speciesCounts) {
        drawCatchChart(window.speciesLabels, window.speciesCounts);
    }
});

// Monthly data chart
function drawMonthChart(labels, data) {
    const ctx = document.getElementById('monthChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Fångst per månad',
                data: data,
                fill: true,
                backgroundColor: 'rgba(255,165,0,0.2)',
                borderColor: 'orange',
                tension: 0.3
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1,
                        precision: 0,
                        color: '#fff'
                    },
                    grid: {
                        color: 'rgba(255,255,255,0.2)'
                    }
                },
                x: {
                    ticks: {
                        color: '#fff'
                    },
                    grid: {
                        color: 'rgba(255,255,255,0.2)'
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#fff'
                    }
                }
            }
        }
    });
}