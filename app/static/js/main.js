/**
 * SkinCheck — Client-side Interaction JavaScript
 * Foundation phase helper script
 */

document.addEventListener('DOMContentLoaded', () => {
  console.log('SkinCheck Web MVC Application initialized successfully.');

  // Auto-dismiss alerts after 5 seconds if present
  const alerts = document.querySelectorAll('.alert-dismissible');
  alerts.forEach((alert) => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      if (bsAlert) {
        bsAlert.close();
      }
    }, 5000);
  });

  // Enable Bootstrap tooltips if any
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl));
});
