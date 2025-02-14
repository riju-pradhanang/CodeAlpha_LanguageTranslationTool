# CodeAlpha_LanguageTranslationTool
Language Translation Tool using Google Translator API

# Overview

This project is a language translation tool built using Python and the Google Translator API. It provides a simple and intuitive way to translate text between different languages. This tool aims to make communication easier and more accessible by breaking down language barriers.


# Features

*   **Google Translator API Integration:** Leverages the power of the Google Translator API for accurate and high-quality translations.
*   **User-Friendly Interface:** Designed with simplicity in mind, making it easy for anyone to use.
*   **Multilingual Support:** Supports a wide range of languages, enabling translation between numerous language pairs.
*   **Python-Based:** Developed in Python, allowing for flexibility and customization.


# Prerequisites

Before you begin, ensure you have the following installed:

*   **Python:** (ideally Python 3.6 or higher) You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   **pip:** Python package installer (usually included with Python installations)
*   **Google Translator Library:** Go to command prompt and type in the given command- pip install googletrans==4.0.0-rc1


# Installation

1.  **Clone the repository:**

    ```
    git clone [(https://github.com/riju-pradhanang/CodeAlpha_LanguageTranslationTool.git)]
    cd CodeAlpha_LanguageTranslationTool
    ```

2.  **Install the required packages:**

    ```
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file. See the "Dependencies" section below.)*

3.  **Obtain a Google Translator API Key:**

    *   Go to the Google AI Studio website: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
    *   Create a project and enable the Translator API.
    *   Obtain your API key.

4.  **Set up your API key:**

    *   You can set the API key as an environment variable named `GOOGLE_API_KEY`.

        ```
        export GOOGLE_API_KEY="YOUR_API_KEY"
        ```

        *(Replace `"YOUR_API_KEY"` with your actual API key.)*

    *   Alternatively, you can directly insert the API key into the script (Not Recommended for Security Reasons):
        *   Open `translator.py` in a text editor.
        *   Locate the line where the API key is being used and replace `YOUR_API_KEY` with your actual key.


# Usage

1.  **Run the script:**

    ```
    python translator.py
    ```

2.  **Follow the prompts:**

    *   The script will ask you to enter the text you want to translate.
    *   Then, it will ask you to specify the source and target languages (e.g., "en" for English, "fr" for French, "es" for Spanish, etc.).

3.  **View the translation:**

    *   The translated text will be displayed in the console.


# Dependencies

Create a file named `requirements.txt` in the project directory and add the following lines:

google-generativeai
python-dotenv

This file lists the Python packages required for the project.  The `pip install -r requirements.txt` command will install these packages.

*   **google-generativeai:** The official Python library for interacting with the Google Gemini API.
*   **python-dotenv:** To load environment variables from a .env file.  (Optional, but recommended for storing your API key securely).


# Code Structure

*   `translator.py`: The main Python script containing the translation logic.
*   `requirements.txt`:  A list of Python dependencies.
*   `.env` (Optional): A file to store your Google Gemini API key as an environment variable. (Remember to add `.env` to your `.gitignore` file!)


# Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request.


# Acknowledgements

*   Google for providing the Gemini API.
*   The Python community for its excellent libraries and resources.


# Contact

Riju Pradhanang - [pradhanangriju@gmail.com]
