import re

# Define a custom preprocessor function
def custom_preprocessor(text):
    # The specific repititive string pattern to remove
    large_string_pattern = r'Skip to main content.*?User Guide Essential\.\.\.'
    
    # Remove the large string pattern from the text
    text = re.sub(large_string_pattern, '', text, count = 1)
    
    # Additional preprocessing (e.g., lowercasing, removing punctuation)
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    
    return text


# This function processes the labels
def process_string(input_string):
    # Convert to lowercase
    lowercased_string = input_string.lower()
    
    # Replace white spaces with underscores
    string_with_underscores = re.sub(r'\s+', '_', lowercased_string)
    
    # Remove non-alphanumeric characters (excluding underscores)
    clean_string = re.sub(r'[^\w]', '', string_with_underscores)
    
    return clean_string