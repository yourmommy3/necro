from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
warnings.filterwarnings(action = 'ignore') 
from gensim.models import Word2Vec
 


words = ['happy', 'teacher', 'king', 'queen', 'princess']

model = Word2Vec(words, min_count = 1,vector_size = 5)
print(list(model.wv.vectors))
