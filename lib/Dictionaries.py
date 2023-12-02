from collections import Counter

import string


def word_frequency(sentence):
    
    sentence = sentence.translate(str.maketrans("","",string.punctuation)).lower()

    word_list = sentence.split()
    word_counts = Counter(word_list)
    return dict(word_counts)

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
