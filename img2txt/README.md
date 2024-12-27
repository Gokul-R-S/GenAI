# IMG2TXT

Gemini IMG2TXT is a Streamlit-based application that leverages Google's Gemini API to generate text descriptions from images and input prompts. This tool is designed for creative writing, content generation, and visual-to-text conversion.

## Features

- **Image-to-Text Conversion**: Upload an image, and the app generates a descriptive text based on its content.
- **Prompt-Based Text Generation**: Input a text prompt to guide the description process.
- **Integrated Gemini API**: Utilizes the powerful Gemini 1.5 Flash model for high-quality generative outputs.

## How to Use

1. Clone this repository and navigate to the project directory.
   ```bash
   git clone https://github.com/your-repo-name/img2txt.git
   cd img2txt
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the Google API key:
   - Create a `.env` file in the project directory.
   - Add your API key:
     ```
     google_api_key=YOUR_API_KEY
     ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```
5. Upload an image and/or input a prompt to generate a response.

## Requirements

- Python 3.8+
- Streamlit
- Pillow
- Google Generative AI SDK
- dotenv

## Screenshots

- **Input Interface**: Upload an image and provide a text prompt.
- **Output Interface**: View the generated text description.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---

**Note**: Ensure your API key has appropriate permissions to access the Gemini API for both text and image processing.

