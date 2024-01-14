# app.py
import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Read content from 'resume.txt' and 'job_description.txt'
resume_content = ""
job_description_content = ""

try:
    with open('resume.txt', 'r') as resume_file:
        resume_content = resume_file.read()
except FileNotFoundError:
    print("File not found: resume.txt")

try:
    with open('job_description.txt', 'r') as job_description_file:
        job_description_content = job_description_file.read()
except FileNotFoundError:
    print("File not found: job_description.txt")

combined_content = f"""
Make changes in the resume given below so that it is more suitable to apply for the job description below it:
{resume_content}
{job_description_content}
Please provide the updated resume in HTML format
"""

prompt_parts = [combined_content]

print(combined_content)
response = model.generate_content(prompt_parts)

# Save the response to a new file
response_filepath = 'final_resume.txt'
with open(response_filepath, 'w') as response_file:
    response_file.write(response.text)

print(f"Response saved as '{response_filepath}'.")
