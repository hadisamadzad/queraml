def encode(text):
    words = text.replace('.','').replace(',','').replace('\'', '').replace('-', '').replace('"', '').split()
    word_to_number_map = {}
    numbers = []
    wordCounter = 0

    for word in words:
        isNewWord = word_to_number_map.get(word, 'Yes')
        if isNewWord == 'Yes':
            wordCounter += 1
            word_to_number_map[word] = wordCounter
            numbers.append(wordCounter)
        else:
            numbers.append(word_to_number_map[word])

    return word_to_number_map, numbers
    
    # input
str = input()
print(encode(str))