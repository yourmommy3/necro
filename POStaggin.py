import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stop_words = set(stopwords.words('english'))
txt = "At CES 2023, Qi2 was announced via press release and it turns out that Apple is contributing quite a bit to the new standard. If you're an Android user but still want to take advantage of some of Apple's MagSafe without using a case, this is good news for you. The new standard will add magnets to mobile devices that will help with alignment while charging, just like MagSafe." 
tokenized = sent_tokenize(txt)
for i in tokenized:
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words]
    tagged = nltk.pos_tag(wordsList)
    print(tagged)

