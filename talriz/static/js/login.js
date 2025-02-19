document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const loginContainer = document.querySelector(".Login_box");

    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Prevent form from submitting traditionally

        const formData = new FormData(form);

        const response = await fetch(form.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
            },
            body: formData,
        });

        const result = await response.json();

        // Check for errors and display them
        const errorBox = document.getElementById("error-box");
        if (errorBox) errorBox.remove(); // Remove existing errors

        if (!response.ok) {
            const errorMessage = document.createElement("p");
            errorMessage.id = "error-box";
            errorMessage.textContent = result.error;
            errorMessage.style.color = "red";
            errorMessage.style.textAlign = "center";
            loginContainer.insertBefore(errorMessage, form); // Insert above the form
        } else {
            const redirectUrl = form.getAttribute("data-redirect-url"); // Get redirect URL
            window.location.href = redirectUrl; // Redirect on success
        }
    });
});
