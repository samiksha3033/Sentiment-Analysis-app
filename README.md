# Sentiment Analysis Web Application (Mock Version)

This project is a Flask-based web application that performs sentiment analysis on user-provided text.  
The main objective of this project is to understand how sentiment analysis functionality can be integrated into a web application, including frontend interaction, backend processing, testing, and error handling.

This version uses **mock (rule-based) sentiment logic** and does not rely on external AI services or APIs.  
A separate version of this project will later be developed using real AI libraries.

## Objectives
- Understand end-to-end web application flow
- Integrate sentiment analysis logic with a Flask backend
- Handle user input, errors, and API responses
- Write unit tests and perform static code analysis
- Build a clean and modular project structure

## Technologies Used
- Python
- Flask
- HTML, CSS, JavaScript
- unittest (Unit Testing)
- Pylint (Static Code Analysis)

## Application Workflow
1. User enters text on the web interface
2. JavaScript sends the input to the Flask backend
3. Backend processes the text using sentiment logic
4. Sentiment result is returned and displayed dynamically


## Testing
Unit tests are written using Python’s `unittest` module to verify different sentiment scenarios.

Note
This project intentionally uses mock sentiment logic to focus on application architecture and integration concepts.
An AI-powered version using open-source NLP libraries will be implemented separately.
