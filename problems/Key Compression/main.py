from filereader import read
from filereader import readAndSplitLines

# functions
def encode(text):
    words = input.replace('.','').replace(',','').replace('\'', '').replace('-', '').split()
    dict = {}
    numbers = []
    wordCounter = 0

    for word in words:
        isNewWord = dict.get(word, 'Yes')
        if isNewWord == 'Yes':
            wordCounter += 1
            dict[word] = wordCounter
            numbers.append(wordCounter)
        else:
            numbers.append(dict[word])

    return dict, numbers
    
# input
input = read("input.txt")
print(encode(input))