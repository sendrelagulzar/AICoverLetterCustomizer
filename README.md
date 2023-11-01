# AICoverLetterCustomizer
## Description:
The Cover Letter Customizer is a Python-based application designed to simplify the process of creating personalized cover letters for project proposals and job applications. This application leverages the power of OpenAI's language model to generate high-quality, customized cover letters tailored to the user's needs.

## Key Components:

Input Options: The application provides two main options for generating cover letters: "Project Description" and "Job Profile." Users can choose the appropriate option based on their specific requirements.

User Input: The user is prompted to enter their name and the name of the client or company to which the cover letter is addressed. Additionally, they are required to provide a project description or job profile, depending on the selected option.

Customized Letter Generation: The application uses OpenAI's language model and predefined prompts to generate cover letters. It contains two primary functions: project() and job(), each designed for generating project proposal cover letters and job application cover letters, respectively. These functions use the provided user inputs to create tailored cover letters.

Streamlit Interface: The application uses Streamlit, a Python library for creating web applications, to provide a user-friendly interface. Users can make their selections and input their details in the sidebar of the application.

Dynamic Response: When users click the "Generate" button, the application generates a customized cover letter based on the selected option and user input. The response is then displayed on the screen for the user to review.

## Usage:

Users select either "Project Description" or "Job Profile" based on their specific needs.
Users enter their name and the name of the client or company they are addressing in the cover letter.
Depending on the selected option, users provide a project description or job profile.
Clicking the "Generate" button triggers the application to generate a customized cover letter using OpenAI's language model.
The generated cover letter is displayed on the screen for the user to copy or further customize.
Note: To use this application, the OpenAI API key must be set in the os.environ['OPENAI_API_KEY'] variable for proper integration with the language model.

This project aims to simplify the process of creating tailored cover letters, saving users time and effort while ensuring a professional and personalized approach in their project proposals and job applications.
