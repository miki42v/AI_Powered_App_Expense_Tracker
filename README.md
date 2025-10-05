# AI-Powered Application: Q&A Bot, Summarizer & Expense Tracker

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Deployed on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

A multi-functional web application built for an internship assignment. This project combines a personal expense tracker, a text summarizer, and an AI-powered Q&A bot into a single, user-friendly interface powered by modern, free-to-use AI APIs.

---

## 🚀 Live Demo

You can view and interact with the live, deployed application here:

**[https://my-ai-app-miki42v.onrender.com/](https://my-ai-app-miki42v.onrender.com/)**

---

## ✨ Features

*   **🤖 AI Q&A Bot:** Ask any question and get a response from a powerful, state-of-the-art language model (NVIDIA Llama 3).
*   **📝 Text Summarizer:** Paste any long article or text to get a concise, easy-to-read summary using a dedicated model from the Hugging Face Inference API.
*   **💸 Personal Expense Tracker:** Add expenses by category and amount, and view a running summary of your total spending, broken down by category.

---

## 🛠️ Tech Stack

*   **Language:** Python
*   **Web Framework:** Streamlit
*   **AI APIs:**
    *   **NVIDIA API** for Q&A (Llama 3 Model)
    *   **Hugging Face Inference API** for Summarization
*   **Libraries:** Pandas, Python-Dotenv, OpenAI (as a client for the NVIDIA API)
*   **Deployment:** Render

---

## 💡 My Journey & Key Decisions

This project was an incredible learning experience in solving real-world development challenges. My goal was to build a simple, AI-powered app, but the journey involved several important pivots that demonstrated resourcefulness and problem-solving.

### The Initial Challenge: API Limitations

I began by building all AI features using the OpenAI API. However, I quickly ran into the rate limits and quota restrictions of the free tier, which caused the application to fail. Instead of stopping, I saw this as a classic engineering challenge and researched high-quality, free alternatives.

### The Pivot: A Hybrid AI Solution

1.  **For the Q&A Bot:** I refactored the `AIBot` class to use **NVIDIA's API**, which provides free access to powerful models like Llama 3. I implemented this using their clean, OpenAI-compatible client, which made the code easy to adapt and maintain.

2.  **For the Text Summarizer:** I switched the `TextSummarizer` class to use a dedicated model from the **Hugging Face Inference API**. This was a more efficient and completely free solution for this specific task.

### The Deployment Challenge: Finding the Right Platform

My initial deployment attempts on other platforms were met with persistent `PermissionError` issues related to the cloud environment. After debugging and implementing a configuration fix (`.streamlit/config.toml`), I decided to find a more stable and developer-friendly platform. I ultimately chose to deploy the application on **Render**, which provided a seamless, Git-based workflow and handled the environment perfectly.

This journey taught me how to adapt to API limitations, securely manage multiple API keys in a production environment, debug deployment issues, and choose the right tools and platforms for the job.

---

## Local Development Setup

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/miki42v/AI_Powered_App_Expense_Tracker.git
    cd AI_Powered_App_Expense_Tracker
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file** in the root directory and add your secret API keys:
    ```
    NVIDIA_API_KEY="nvapi-..."
    HUGGINGFACE_API_TOKEN="hf_..."
    ```

4.  **Run the Streamlit app:**
    ```bash
    python -m streamlit run app/main.py
    ```

---

## 📂 Project Structure

The project is organized using an object-oriented approach to ensure modularity and maintainability.

```/
├── .streamlit/               # Streamlit configuration for deployment
│   └── config.toml
├── app/                      # Main application source code
│   ├── ai_bot.py             # AIBot class (NVIDIA API)
│   ├── text_summarizer.py    # TextSummarizer class (Hugging Face API)
│   ├── expense_tracker.py    # ExpenseTracker class
│   └── main.py               # Streamlit UI and main application logic
├── .gitignore                # Files to be ignored by Git
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation (this file)