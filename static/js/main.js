document.addEventListener('DOMContentLoaded', function() {
    const calculatorForm = document.getElementById('calculator-form');
    const resultDiv = document.getElementById('result');

    if (calculatorForm) {
        calculatorForm.addEventListener('submit', function(e) {
            e.preventDefault();
            calculateSteps(calculatorForm, resultDiv);
        });
    }

    function calculateSteps(form, resultElement) {
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        fetch('/api/calculate-steps', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(result => {
            if (result.errors) {
                resultElement.innerHTML = `<p class="error">${result.errors.join('<br>')}</p>`;
            } else {
                resultElement.innerHTML = `<p>Estimated steps to burn ${data.calories} calories: <strong>${result.steps}</strong></p>`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultElement.innerHTML = '<p class="error">An error occurred while calculating steps. Please try again.</p>';
        });
    }

    // Implement smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});