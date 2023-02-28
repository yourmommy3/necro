from nltk.corpus import wordnet as wn
import nltk
NLTK_TYPE = 'wordnet'
DOG_SYNSET= 'dog.n.01'
CAT_SYNSET = 'cat.n.01'
VEHICLE_SYNSET = 'vehicle.n.01'

def get_all_hyponyms(label):
    syn = wn.synset(label)
    return set([w.lower() for s in syn.closure(lambda s:s.hyponyms()) for w in s.lemma_names()])

def get_all_hyponyms_List(label):
    syn = wn.synset(label)
    return [w.lower() for s in syn.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]


def get_all_hyponyms_List2(label):
    result = []
    syn = wn.synset(label)
    for s in syn.closure(lambda s: s.hyponyms()):
        for w in s.lemma_names():
            result.append(w.lower())

    return result

DOG_HYPONYMS = get_all_hyponyms_List2(DOG_SYNSET)
print("length=",len(DOG_HYPONYMS))
ans = DOG_HYPONYMS[:5]
print(ans)

