from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
from custom_preprocessor import custom_preprocessor, process_string
from text_generator import generate_text

app = Flask(__name__)

# Load the names and URLs of the chapters and save inside a dictionary
data = pd.read_csv('../data/pandas_user_guide.csv')
data_dict = data.set_index('link_text')['url'].to_dict()

# Load the model from disk
model = joblib.load('../saved_models/finalized_svm_model.sav')
vectorizer = joblib.load('../saved_models/vectorizer.sav')

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    
    # Call to Python function
    bot_response = predict_chapter(user_message)
    
    return jsonify({'response': bot_response})

def predict_chapter(user_input):
    '''
    This function
    - transforms the user's query using vectorizer
    - using that query predicts the chapter
    - returns the URL of the chapter
    '''
    # Transform query using vectorizer
    query = vectorizer.transform([user_input])
    
    # Predict chapter and return the URL
    prediction = model.predict(query)
    url = data_dict[prediction[0]]
    generated_response = generate_text(user_input)
    
    final_response = f'{generated_response} For further information, check <a href={url} target=\'_blank\'>{prediction[0]}</a>'
    return final_response

if __name__ == '__main__':
    app.run(debug=True)