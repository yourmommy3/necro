import nltk

text = "learn php from guru99"
print("original text: \n"+text)
tokens = nltk.word_tokenize(text)
nouns = []
tag = nltk.pos_tag(tokens)
for i in tag:
    if i[1] == "NN" or i[1] == "NNS" or i[1] == "NNP" or i[1] == "NNPS":
        nouns.append(i[0])
        tokens.remove(i[0])

print("\nnouns") 
print(*nouns)
print("\nafter removing nouns")
print(*tokens)
