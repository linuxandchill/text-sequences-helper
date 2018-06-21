import numpy as np

sentences = ["Hello there how are you?", "Whats up dude how's it going", "I am well thanks"]

token_index = {}

for s in sentences:
    for word in s.split():
        if word not in token_index:
            token_index[word] = len(token_index) + 1

max_len = 10

res = np.zeros(shape=(len(sentences),
    max_len,
    max(token_index.values()) + 1)) 

for i, sentence in enumerate(sentences):
    for j, word in list(enumerate(s.split()))[:max_len]:
        index = token_index.get(word)
        res[i,j,index] = 1
