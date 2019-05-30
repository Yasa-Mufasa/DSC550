'''
This project is to learn TF-IDF. In this project, I will be following along ProgrammingTogether's Python TF-IDF (NLP)
Calculation Introduction, which can be accessed at
https://www.youtube.com/watch?v=jpupXhZ92c8&list=PLy0R06Fv9ZSIHjFje2d53WztJeNjHW0zT&index=1
'''

import math

documents = ['the the universe has very many stars',
             'the galaxy contains many stars',
             'the cold breeze of winter made it very cold outside']

#First, we can tokenize the words
dictOfWords = {}

for index, sentence in enumerate(documents):
    tokenizedWords = sentence.split(' ')
    dictOfWords[index] = [(word,tokenizedWords.count(word)) for word in tokenizedWords]


#second, we can remove the duplicate tokens as we only need one of them for now.
termFrequency = {}

for i in range(0, len(documents)):
    listOfNoDuplicates = []
    for wordFreq in dictOfWords[i]:
        if wordFreq not in listOfNoDuplicates:
            listOfNoDuplicates.append(wordFreq)
        termFrequency[i] = listOfNoDuplicates


#Third, we can calculate the Normal Term Frequency
normalizedTermFrequency = {}
for i in range(0, len(documents)):
    sentence = dictOfWords[i]
    lenOfSentence = len(sentence)
    listOfNormalized = []
    for wordFreq in termFrequency[i]:
        normalizedFreq = wordFreq[1]/float(lenOfSentence)  # Needed to add the float here so the calculation isn't reduced to 0.
        listOfNormalized.append((wordFreq[0],normalizedFreq))
    normalizedTermFrequency[i] = listOfNormalized

# Now we can get to Calculating the IDF

# First, we need to put all of the sentences together and re-tokenize the words

allDocuments = ''
for sentence in documents:
    allDocuments += sentence + ' '
allDocumentsTokenized = allDocuments.split(' ')


allDocumentsNoDuplicates = []

for word in allDocumentsTokenized:
    if word not in allDocumentsNoDuplicates:
        allDocumentsNoDuplicates.append(word)

# Second, we can calculate the number of documents where the term t appears

dictOfNumberOfDocumentsWithTermInside = {}

for index, voc in enumerate(allDocumentsNoDuplicates):
    count = 0
    for sentence in documents:
        if voc in sentence:
            count += 1
    dictOfNumberOfDocumentsWithTermInside[index] = (voc, count)


# Now we can calculate the IDF
dictOFIDFNoDuplicates = {}


for i in range(0, len(normalizedTermFrequency)):
    listOfIDFCalcs = []
    for word in normalizedTermFrequency[i]:
        for x in range(0, len(dictOfNumberOfDocumentsWithTermInside)):
            if word[0] == dictOfNumberOfDocumentsWithTermInside[x][0]:
                listOfIDFCalcs.append((word[0],math.log(len(documents)/dictOfNumberOfDocumentsWithTermInside[x][1])))
    dictOFIDFNoDuplicates[i] = listOfIDFCalcs


# And now to multiply the TF by IDF for the TF-IDF
dictOFTF_IDF = {}
for i in range(0,len(normalizedTermFrequency)):
    listOFTF_IDF = []
    TFsentence = normalizedTermFrequency[i]
    IDFsentence = dictOFIDFNoDuplicates[i]
    for x in range(0, len(TFsentence)):
        listOFTF_IDF.append((TFsentence[x][0],TFsentence[x][1]*IDFsentence[x][1]))
    dictOFTF_IDF[i] = listOFTF_IDF

print(dictOFTF_IDF)
