def synonym_antonym_extractor(phrase):
    from nltk.corpus import wordnet
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    print("These are Synonyms")
    print(set(synonyms))

    print()
    print("These are Antonyms")
    print(set(antonyms))


synonym_antonym_extractor(phrase="run")


