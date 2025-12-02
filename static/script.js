document.getElementById("contact-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const status = document.getElementById("status");
    const submitBtn = document.getElementById("contact-submit");
    const form = document.getElementById("contact-form");

    const payload = {
        name: document.getElementById("name").value.trim(),
        email: document.getElementById("email").value.trim(),
        message: document.getElementById("message").value.trim(),
    };

    // Disable button and show loading text
    submitBtn.disabled = true;
    const originalText = submitBtn.textContent;
    submitBtn.textContent = "Sending...";

    try {
        const res = await fetch("/send-email", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await res.json();

        status.textContent = data.message;
        status.style.color = data.status === "success" ? "green" : "red";
        

        // 🎉 Alert on success
        if (data.status === "success") {
            alert("Your message has been sent successfully!");

            // Clear form
            form.reset();
        }
        else{
            alert("Failed to send message. Please try again later.");
            form.reset();
            
        }

    } catch (err) {
        status.textContent = "Error sending message.";
        status.style.color = "red";
        console.error(err);
    } finally {
        // Restore button state
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    }
});
