from transformers import GPT2LMHeadModel, GPT2Tokenizer
from nltk.tokenize import sent_tokenize
import re

# This function will generate text using pretrained model
# and return the text 
def generate_text(query):
    '''
    This function
    - loads the pretrained model and tokenizer
    - uses the tokenizer and model to generate a response against the prompt/query
    - cleans and returns the generated response
    '''
    # Load fine-tuned model and tokenizer
    fine_tuned_model = GPT2LMHeadModel.from_pretrained('../GPT-2_model/fine_tuned_model/')
    fine_tuned_tokenizer = GPT2Tokenizer.from_pretrained('../GPT-2_model/fine_tuned_model/')
    
    # Generate response
    input_ids = fine_tuned_tokenizer.encode(query, return_tensors='pt')
    max_length = 100
    output = fine_tuned_model.generate(
                    input_ids, 
                    max_length=max_length,                     
                    num_return_sequences=1, 
                    pad_token_id=fine_tuned_tokenizer.eos_token_id,
                    no_repeat_ngram_size=3,
            )
    generated_text = fine_tuned_tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Clean and return the generated response
    cleaned_response = ' '.join(sent_tokenize(generated_text)[:3])  # Keep first 3 sentences
    final_response = remove_repeated_sentences_and_prompt(cleaned_response)
    return final_response


# This function removes any repated sentence from the response
def remove_repeated_sentences_and_prompt(text):
    '''
    This function
    - removes the prompt/query from the response
    - removes any repeated sentences from the response
    '''
    # Remove the first sentence from the response (which is the prompt itself)
    text = re.sub(r'^(.*?[.!?])(\s|$)', '', text) 
    
    # Remove any repeated sentences
    sentences = text.split('. ')
    seen_sentences = set()
    unique_sentences = []
    for sentence in sentences:
        if sentence not in seen_sentences:
            unique_sentences.append(sentence)
            seen_sentences.add(sentence)
    return '. '.join(unique_sentences)