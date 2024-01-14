
// script.js
function createResume() {
    const resumeText = document.getElementById('resumeInput').value;
    const jobDescription = document.getElementById('jobDescriptionInput').value;

    // Save content as text files
    createFile('resume.txt', resumeText);
    createFile('job_description.txt', jobDescription);

    // Display the result
    document.getElementById('resultContainer').innerHTML = 'Files saved successfully.';
}

// Function to create and save a text file
function createFile(filename, content) {
    console.log("hi")
    const blob = new Blob([content], { type: 'text/plain' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = filename;
    a.click();
}
