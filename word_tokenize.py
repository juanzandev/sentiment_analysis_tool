import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download resources if not already available
nltk.download('punkt_tab')
nltk.download('stopwords')

text = "I absolutely love this product! It works amazingly well."
# Convert text to lowercase and remove punctuation
text = text.lower().translate(str.maketrans('', '', string.punctuation))

# Tokenize text
tokens = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

print(filtered_tokens)
