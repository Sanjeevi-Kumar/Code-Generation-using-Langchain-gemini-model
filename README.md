# 🧠 AI Problem Solver using Gemini & Streamlit
This is a simple Streamlit web app that uses **Google Gemini (via LangChain)** to solve programming problems in your desired language.

## 🚀 Features
- ✅ Ask any coding or logical problem
- ✅ Get instant answers in the programming language of your choice
- ✅ Powered by `langchain`, `streamlit`, and Google Gemini (1.5 Flash)
  
## 🛠️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/ai-problem-solver.git
cd ai-problem-solver

### 2. Install Dependencies

pip install -r requirements.txt

#### Example `requirements.txt`:

streamlit
langchain
langchain-google-genai

### 3. Set Up Your API Key

Create a file named `key.py` in the project directory and add:

api_key = "your_google_generative_ai_api_key"
## 🧪 Run the App
streamlit run app.py

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## 🧠 How It Works

- Takes a **problem statement** and **programming language** as input
- Uses a LangChain `PromptTemplate` to format the prompt
- Sends the prompt to Gemini via `ChatGoogleGenerativeAI`
- Displays the AI-generated solution in the browser

## 📁 File Structure

├── app.py             # Main Streamlit application \n
├── key.py             # Contains your Google API key
├── requirements.txt   # Required Python packages
└── README.md          # You're reading it
## 🧑‍💻 Author

**Sanjeevi Kumar M**  
📫 sanjeevikumar365@gmail.com 
🔗 https://www.linkedin.com/in/sanjeevi-kumar-m/

## 📜 License

This project is licensed under the [MIT License](LICENSE).
