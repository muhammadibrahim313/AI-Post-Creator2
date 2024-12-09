import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_ai_model():
    """Initialize AI model with error handling"""
    try:
        return ChatOpenAI(
            temperature=0.7,
            model_name="gpt-3.5-turbo"
        )
    except Exception as e:
        st.error(f"Error initializing AI model: {str(e)}")
        return None

def generate_content(prompt, system_prompt=""):
    """Generate content using the AI model"""
    try:
        model = init_ai_model()
        if not model:
            return "Error: Could not initialize AI model"

        template = ChatPromptTemplate.from_template(
            system_prompt + "\n\n" + prompt if system_prompt else prompt
        )
        chain = template | model | StrOutputParser()
        return chain.invoke({})

    except Exception as e:
        return f"Error: {str(e)}"

def load_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Base Styles */
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: #FF4B4B;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 500;
        color: #FAFAFA;
        margin: 1rem 0;
    }
    
    /* Card Styles */
    .card {
        text-align: left;
        padding: 25px;
        margin: 15px 0;
        background-color: #262730;
        border-radius: 15px;
        border: 1px solid #363636;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    
    .info-card {
        background-color: #1E1E1E;
        border-left: 4px solid #FF4B4B;
    }
    
    .result-card {
        background-color: #1E1E1E;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .analysis-card {
        background-color: #1E1E1E;
        margin-bottom: 20px;
    }
    
    .history-card {
        background-color: #1E1E1E;
        border-left: 4px solid #363636;
    }
    
    /* Content Elements */
    .card h3 {
        color: #FFFFFF;
        margin: 0 0 15px 0;
        font-size: 1.3rem;
        font-weight: 600;
    }
    
    .card p {
        color: #B2B2B2;
        margin: 8px 0;
        line-height: 1.6;
    }
    
    .info-text {
        font-size: 0.9rem;
        color: #B2B2B2;
        font-style: italic;
        line-height: 1.5;
    }
    
    /* Score Display */
    .score-display {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin: 15px 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .score-label {
        text-align: center;
        color: #B2B2B2;
        font-size: 1rem;
        margin-bottom: 15px;
    }
    
    .score-summary {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 10px 0;
        padding: 10px;
        background-color: #1A1A1A;
        border-radius: 5px;
    }
    
    .score-value {
        font-weight: bold;
        font-size: 1.2rem;
    }
    
    /* Analysis Content */
    .analysis-content {
        background-color: #1A1A1A;
        padding: 15px;
        border-radius: 5px;
        margin-top: 10px;
        line-height: 1.6;
    }
    
    .analysis-summary {
        margin-top: 15px;
        padding: 15px;
        background-color: #1A1A1A;
        border-radius: 5px;
        font-size: 0.9rem;
        color: #B2B2B2;
    }
    
    /* Dividers */
    hr {
        border: 0;
        height: 1px;
        background: #363636;
        margin: 20px 0;
    }
    
    /* Links */
    .card a {
        color: #FF4B4B;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .card a:hover {
        color: #FF7676;
        text-decoration: underline;
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1E1E1E;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #363636;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #FF4B4B;
    }
    
    .post-metadata {
        background-color: #1A1A1A;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        font-size: 0.9rem;
    }
    
    .post-content {
        background-color: #1A1A1A;
        padding: 15px;
        border-radius: 5px;
        margin-top: 15px;
        line-height: 1.6;
        white-space: pre-wrap;
    }
    
    .result-card {
        border-left: 4px solid #00C853;
    }
    
    .stButton button {
        width: 100%;
        padding: 0.75rem !important;
        font-size: 1.1rem !important;
    }
    </style>
    """

def show_error(message):
    st.error(f"🚨 {message}")

def show_success(message):
    st.success(f"✅ {message}")

def show_info(message):
    st.info(f"ℹ️ {message}")