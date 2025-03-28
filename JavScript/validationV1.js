function validateForm(event) {
    event.preventDefault();
    const formFields = document.querySelectorAll("#registration_form .form-control, #registration_form .form-check-input");
    let isValid = true;

    function createErrorMessages(parentDiv, message) {
        const errorMessage = document.createElement("div"); //<div></div>
        errorMessage.classList.add("text-danger"); //<div class="text-danger"></div>
        errorMessage.innerHTML = message; //<div class="text-danger">`${message}`</div>
        parentDiv.appendChild(errorMessage);


        setTimeout(() => {
            errorMessage.remove();
        }, 5000);
    }

    formFields.forEach(field => {
        let parentDiv = field.closest('.mb-3');
        const label = parentDiv.querySelector("label");

        const existingError = parentDiv.querySelector(".text-danger");
        if (existingError) {
            existingError.remove();
        }

        if (field.id === 'phone_number') {
            const phonePattern = /^[6-9]\d{9}$/;
            if (field.value && !phonePattern.test(field.value.trim())) {
                isValid = false;
                createErrorMessages(parentDiv, "Phone number should only contain 10 digits and should start with (6,7,8 or 9)");
            }
        }
23
        if (field.id === 'email_id') {
            const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (field.value && !emailPattern.test(field.value.trim())) {
                isValid = false;
                createErrorMessages(parentDiv, "Please enter a valid email address");
            }
        }
        if (field.id === 'aadhar_number') {
            const addarPattern = /^\d{12}$/;
            if (field.value && !addarPattern.test(field.value.trim())) {
                isValid = false
                createErrorMessages(parentDiv, "Aadhar number should contain exactly 12 digits");
            }
        }
        if (field.id === 'pin_code') {
            const pinCodePattern = /^\d{6}$/;
            if (field.value && !pinCodePattern.test(field.value.trim())) {
                isValid = false
                createErrorMessages(parentDiv, "Pin code should contain exactly 6 digits");
            }
        }
        if (label && label.textContent.toLowerCase().includes('name')) {
            const namePattern = /^[a-zA-Z\s]+$/;
            if (field.value && !namePattern.test(field.value.trim())) {
                isValid = false;
                createErrorMessages(parentDiv, `${label.textContent} can only contain alphabets and spaces.`);
            }
        }
        if (label && label.textContent.toLowerCase().includes('board')) {
            const namePattern = /^[a-zA-Z\s]+$/;
            if (field.value && !namePattern.test(field.value.trim())) {
                isValid = false;
                createErrorMessages(parentDiv, `${label.textContent} can only contain alphabets,spaces & full-stop(period symbol).`);
            }
        }

        if (field.type === 'radio' || field.type === 'checkbox') {
            const radioChecked = document.querySelector(`input[name="${field.name}"]:checked`);
            if (!radioChecked) {
                isValid = false;
                createErrorMessages(parentDiv, ` ${label.textContent} is required.`);
            }
        } else if (field.value.trim() === "") {
            isValid = false;
            createErrorMessages(parentDiv, `${label.textContent} is required.`);
        }
    });

    if (isValid) {
        alert("Form submitted successfully");
        document.getElementById("registration_form").submit();
        return true;
    } else {
        return false;
    }
}