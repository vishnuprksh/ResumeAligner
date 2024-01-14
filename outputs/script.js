// outputs/script.js
document.addEventListener("DOMContentLoaded", function () {
    const htmlInput = document.getElementById("html-input");
    const preview = document.getElementById("preview");

    htmlInput.addEventListener("input", updatePreview);

    function updatePreview() {
        const htmlCode = htmlInput.value;
        preview.innerHTML = htmlCode;
    }

    // Load content from final_resume.txt into html-input textarea
    loadResumeContent();

    function loadResumeContent() {
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const resumeContent = xhr.responseText;
                htmlInput.value = resumeContent;
                updatePreview(); // Update the preview after loading content
            }
        };
        xhr.open("GET", "../final_resume.txt", true);
        xhr.send();
    }
});
