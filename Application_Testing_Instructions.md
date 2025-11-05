# Application Testing Instructions

This document outlines the steps to test the application.

1. Navigate to the **notebooks** directory and run the following notebooks in order:
   - `1_web_scraping.ipynb`
   - `2_model_comparison.ipynb`
   - `3_text_cleaning_for_GPT2.ipynb`

2. Next, open the **GPT-2_model** directory under and run the notebook named `GPT2-with-pandas-text-data.ipynb`.

3. Allow the GPT-2 model training process to complete.

4. Once training is finished, go to the **flask_app** directory under **Application** and open a Terminal window from that directory.

5. In the terminal, run the command:
   ```bash
   python app.py

6. After execution, click the URL displayed in the terminal (e.g., http://127.0.0.1:5000/) to launch the chatbot application.