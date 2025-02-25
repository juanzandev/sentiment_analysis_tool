# Based off of NLTK Tutorial in Python, Demo includes:
# tokenization, 


import nltk
nltk.download('punkt','stopwords','wordnet','vader_lexicon','averaged_perceptron_tagger')     #download punkt,stopwords,wordnet,vader_lexicon,averaged_perceptron_tagger_eng

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from nltk.corpus import wordnet
from nltk.tag import pos_tag
from nltk.tree import Tree
from IPython.display import display


sample_text = "This is a sample text! Let's try NLTK commands with it."                 #sample text used throughout

#Tokenization process
    
    #based on words
st_tword=word_tokenize(sample_text)
print("Sample text tokenzied by word:", st_tword)

    #based on sentences
st_tsentence=sent_tokenize(sample_text)
print("Sample text tokenized by sentance:",st_tsentence)

#Probablity process

st_freq=FreqDist(st_tword)
st_common=st_freq.most_common(4)            #number = amount of words you want
print("4 most coomon words in text:",st_common)

#StopWords
    #using spot words from package

stop_words = set(stopwords.words('english'))      #select stop words and language, also make into a set to get rid of duplicates

    #get rid of stop words from text
st_tkn_without_words=[]

for word in st_tword:
    if word not in stop_words:
        st_tkn_without_words.append(word)

print("Tokenized sample text without stop words:", st_tkn_without_words)

# Lematizer and Stemmer 

sample_words= [ 'do', 'doing', 'go', 'going', 'taking', 'breaking', 'had', 'having', 'has', 'maybe', 'yes', 'no']

lematizer = WordNetLemmatizer()             #reduces word of different forms to one:  build, building, built --> build
stemmer = PorterStemmer()                   # reduces word by dropping affixes: play,playing,plays --> play
                                            # can vary, one may be better than another in different situations, check examples
for word in sample_words:
    stem_word=stemmer.stem(word)
    lemmatizer_word=lematizer.lemmatize(word,'v')            #pass in word and part of speech
    print("The Word:", word,"The Stem of word:",stem_word, "The Lemmatized Word:", lemmatizer_word)


#Sentiment Analyzer

SIA = SentimentIntensityAnalyzer()
print("The Negative Analysis:")
print(SIA.polarity_scores("I hate this movie a lot. The actors are horrible and give nothing new to the franchise."))
print("The Positive Analysis:")
print(SIA.polarity_scores(" I loved this move a lot! It sent chills down my spine.  think the actors brought a lot to the table in this movie."))

#Synonyms/Antonyms

    #definition of word
syn = wordnet.synsets('Review')
print(syn[0].definition())

    #synonyms
synonyms=[]
for syn in wordnet.synsets('Review'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

    #antonyms
antonyms = []
for syn in wordnet.synsets('Review'):                   #if antonyms exist, give them....
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
print(antonyms)

#Part of Speech Tagging

tags = tokens_tag = nltk.pos_tag(st_tword)
tags                                 #assigns a part of speech to each word in a list of tuples

#Chunking and Chinking

    #chunking: find a phrase that works as a unit ( A horse, A heavy horse, ...)

grammar = "NP: {<DT>?<JJ>*<NN>}"      # grammatical unit format you want to extract: optional determiner,any # of adj, ends with a noun 

chunk_parser=nltk.RegexpParser(grammar)

tree=chunk_parser.parse(tags)
print("Extracting unit of determiner, adjective and noun:")
display(tree)

    #chinking: excludes a pattern

grammar2 = """Chunk: }<JJ>{"""              #we want to exclude adjectives (outward curry bracket)

chunk_parser = nltk.RegexpParser(grammar2)

tree2=chunk_parser.parse(tags)
print("Excluding adjectives tags:")
display(tree2)