# GenAI
This repository focuses on GenAI projects

# 1. Movie recommendation system
## Steps
* Clone the repository using ``git clone``
* Used ``cd <repo name>`` to navigate to the repository folder

### **Installation**  
1. Create a virtual environment:  
   ```bash  
   python -m venv .venv  
   ```  
2. Activate the virtual environment:  
   ```bash  
   source .venv/Scripts/activate  
   ```  
3. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

### **Running the Application**  
1. Add your Google Generative AI API key to a `.env` file in the root directory:
   ```plaintext  
   google_api_key=<your_api_key>  
   ```  
2. Run the Streamlit application:  
   ```bash  
   streamlit run app.py  
   ```  

### **Usage**  
- Enter a movie title, genre, or relevant keywords (e.g., sci-fi, thriller, etc.) in the input field.  
- The app will generate 5 personalized movie recommendations with short descriptions.  

### **Dependencies**  
- Streamlit  
- LangChain  
- google-generativeai  
- langchain-google-genai  
- python-dotenv  

### **Pushing the repository into Github**
- git init
- git add .
- git commit -m "message"
- git push origin main 

















