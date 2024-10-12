import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Convert to lowercase and remove special characters
    text = re.sub(r'[^\w\s]', '', text.lower())
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def categorize_text(text):
    tokens = preprocess_text(text)
    
    # Keywords for each category
    categories = {
        'terrorism_protest_unrest': ['terrorism', 'protest', 'riot', 'unrest', 'violence', 
                                   'demonstration', 'conflict', 'uprising', 'rebellion', 'attack',
                                   'political', 'war', 'militant', 'strike'],
        'positive_uplifting': ['success', 'achievement', 'breakthrough', 'victory', 'celebration',
                              'progress', 'improvement', 'innovation', 'recovery', 'hope',
                              'inspire', 'positive', 'growth', 'win'],
        'natural_disasters': ['earthquake', 'flood', 'hurricane', 'tornado', 'tsunami',
                             'wildfire', 'disaster', 'storm', 'drought', 'landslide',
                             'volcanic', 'cyclone', 'catastrophe']
    }
    
    # Count keywords for each category
    scores = {category: 0 for category in categories}
    
    for token in tokens:
        for category, keywords in categories.items():
            if token in keywords:
                scores[category] += 1
    
    # Return category with highest score, or 'others' if no keywords found
    max_score = max(scores.values())
    if max_score > 0:
        return max(scores.items(), key=lambda x: x[1])[0]
    return 'others'