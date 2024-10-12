import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def categorize_text(text):
    tokens = preprocess_text(text)
    
    terrorism_keywords = ['terrorism', 'protest', 'riot', 'unrest', 'violence']
    positive_keywords = ['positive', 'uplifting', 'inspiring', 'hope', 'success']
    disaster_keywords = ['disaster', 'earthquake', 'flood', 'hurricane', 'tornado']
    
    terrorism_count = sum(1 for token in tokens if token in terrorism_keywords)
    positive_count = sum(1 for token in tokens if token in positive_keywords)
    disaster_count = sum(1 for token in tokens if token in disaster_keywords)
    
    if terrorism_count > positive_count and terrorism_count > disaster_count:
        return "Terrorism / protest / political unrest / riot"
    elif positive_count > terrorism_count and positive_count > disaster_count:
        return "Positive/Uplifting"
    elif disaster_count > terrorism_count and disaster_count > positive_count:
        return "Natural Disasters"
    else:
        return "Others"