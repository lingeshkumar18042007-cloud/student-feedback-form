document.addEventListener('DOMContentLoaded', function() {
    // Form Validation for Feedback Form
    const feedbackForm = document.getElementById('feedbackForm');
    
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function(event) {
            let isValid = true;
            
            // Basic validation check
            const requiredFields = feedbackForm.querySelectorAll('[required]');
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error-border');
                } else {
                    field.classList.remove('error-border');
                }
            });

            if (!isValid) {
                event.preventDefault();
                alert('Please fill out all required fields properly.');
            }
        });

        // Live validation remove error class when typing
        const inputs = feedbackForm.querySelectorAll('input, select');
        inputs.forEach(input => {
            input.addEventListener('input', function() {
                if (this.value.trim()) {
                    this.classList.remove('error-border');
                }
            });
        });
    }

    // Confirmation before deleting feedback
    const deleteForms = document.querySelectorAll('.delete-form');
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!confirm('Are you sure you want to delete this feedback? This action cannot be undone.')) {
                event.preventDefault();
            }
        });
    });

    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.alert');
    if (flashMessages.length > 0) {
        setTimeout(function() {
            flashMessages.forEach(msg => {
                msg.style.transition = 'opacity 0.5s ease';
                msg.style.opacity = '0';
                setTimeout(() => msg.remove(), 500); // Wait for transition
            });
        }, 5000);
    }
});
