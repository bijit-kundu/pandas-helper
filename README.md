# 🐼 Pandas Helper

**Pandas Helper** is a local AI-powered chatbot designed to help users explore and learn the [Pandas](https://pandas.pydata.org/) Python library interactively.  
It assists by providing contextual explanations of Pandas concepts, guiding users to relevant documentation chapters, and simplifying data analysis learning.

---

## 🚀 Features

- 🧠 **AI Chatbot Interface** - Ask questions about Pandas functions, methods, and concepts in natural language.
- 📚 **Contextual Keyword Mapping** - Automatically identifies relevant Pandas keywords and links to the right documentation or learning chapter.
- 🔍 **Smart Suggestions** - Provides explanations based on user queries.
- ⚡ **Lightweight & Local** - Runs locally without the need for internet access or hosting.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas** 
- **nltk** 
- **Spacy** 
- **Transformers (openai-community/gpt2)**
- **Flask** *(for the user interface)*

---

## 💻 Installation & Execution

1. 📂 Clone this repository:
   ```bash
   git clone https://github.com/bijit-kundu/pandas-helper.git
   cd pandas-helper  
2. 💻 Launch Jupyter Lab:
   ```bash  
   jupyter lab
3. 🛠️ Create a virtual environment (optional but recommended)
   ```bash
   python3 -m venv venv
4. ⚡ Activate the environment and install dependencies
   ```bash
   !source venv/bin/activate && pip install -r requirements.txt
5. 📓 Navigate to the **notebooks** directory and run the following notebooks in order:   
   a) `1_web_scraping.ipynb`  
   b) `2_model_comparison.ipynb`  
   c) `3_text_cleaning_for_GPT2.ipynb`
6. 🤖 Next, open the **GPT-2_model** directory under and run the notebook named `GPT2-with-pandas-text-data.ipynb`.  
7. ⏳ Allow the GPT-2 model training process to complete.
8. 🖥️ Once training is finished, go to the **flask_app** directory under Application and open a terminal window from that directory.
9. 🏃 In the terminal window, run the command:
   ```bash
   python app.py
10. 🌐 After execution, click the URL displayed in the terminal (e.g., `http://127.0.0.1:5000/`) to launch the chatbot application.
11. ❓ Start by entering your questions related to the Pandas library.

