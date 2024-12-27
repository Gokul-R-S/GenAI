# Healthify

A streamlit-based healthcare advisor application powered by Google's Gemini Pro AI. Get instant health advice and calculate your BMI.

## Features

- AI-powered health advice
- BMI calculator
- Simple and user-friendly interface

## Prerequisites

- Python 3.8 or higher
- Google API key for Gemini Pro

## Installation

1. Clone the repository:
```bash
git clone <repo name>
cd healthify
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/Scripts/activate 
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Google API key:
```
google_api_key=your_api_key_here
```

## Usage

Run the application:
```bash
streamlit run app.py
```

## Dependencies

- streamlit
- google-generativeai
- python-dotenv
- pandas

## Disclaimer

This application provides general health information and should not be considered as medical advice. Always consult healthcare professionals for medical decisions.















