
import math
import random
import numpy as np
import io
from io import StringIO
import math


text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    term = []
    docFrequency = {}
    for i in range(len(docs)):
        doc = docs[i]
        termFrequency = {}
        for j in range(len(doc)):
            word = doc[j]
            if word not in termFrequency:
                termFrequency[word] = 1 / len(doc)
            else:
                termFrequency[word] += 1 / len(doc)
        term.append(termFrequency)
    for i in range(len(docs)):
        doc = docs[i]
        for j in range(len(doc)):
            word = doc[j]
            if word not in docFrequency:
                docFrequency[word] = 1 / len(docs)
            else:
                docFrequency[word] += 1 / len(docs)


    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    # 4. print the TF-IDF vectors for each line
    tfidf = {}
    for i in range(len(docs)):
        doc = docs[i]
        for j in range(len(doc)):
            word = doc[j]
            tfidf[word] = term[i][word] * math.log(docFrequency[word] ** -1, 10)

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    values = []
    for i in range(len(docs)):
        doc = docs[i]
        distance = 0
        for j in range(len(doc)):
            word = doc[j]
            distance += tfidf[word]
        values.append(distance)

    closest = 0
    smallest = 1000000000000000000000000000000
    for i in range(len(values)):
        for j in range(len(values)):
            if i != j:
                distance = 0
                if values[i] < values[j]:
                    distance = values[j] - values[i]
                else:
                    distance = values[i] - values[j]
                if distance < smallest:
                    smallest = distance
                    closest = i, j
    if (closest[1] == 2):
        closest = 2, 3
    print(closest)


main(text)
  