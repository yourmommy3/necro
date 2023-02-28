def word2vec(word):
    from collections import Counter
    from math import sqrt
    cw = Counter(word)
    sw = set(cw)
    lw = sqrt(sum(c*c for c in cw.values()))

    return cw, sw, lw

def cosdis(v1, v2):
    common = v1[1].intersection(v2[1])
    return 1 - (sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2])

a=word2vec("queen")
b=word2vec("princess")
c=word2vec("teacher")
print(cosdis(a,b))
print(cosdis(a,c))