// Auto-fade messages after a few seconds
setTimeout(function () {
  const alerts = document.querySelectorAll('.custom-alert');
  alerts.forEach((alert) => {
    alert.style.opacity = '0';
    setTimeout(() => alert.remove(), 500); // Remove after fade-out
  });
}, 3000);