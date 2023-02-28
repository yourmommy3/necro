from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#part of morphology

#lemmatization 
lemmatizer = WordNetLemmatizer()
print('\nlemmatization')
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
print("better :", lemmatizer.lemmatize("better", pos ="a"))
print("Lemmatisation:", lemmatizer.lemmatize("Lemmatisation"))
print("un=happiness :", lemmatizer.lemmatize("un-happiness"))


#stemming
ps = PorterStemmer()
print("\nstemming")
print("rocks :", ps.stem('rocks'))
print("corpora :", ps.stem('corpora'))
print("Lemmatisation :", ps.stem('Lemmatisation'))
print("unhappiness :", ps.stem('unhappiness'))