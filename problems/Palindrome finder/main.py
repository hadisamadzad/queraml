file = open("inputs.txt", "r")
str = file.read()
words = str.replace('.','').replace(',','').split()

palins = []

for word in words:
    if word.lower() == word[::-1].lower():
        palins.append(word)

if len(palins) == 0:
    print('No palindrome words found :(')
else:
    print('Palindrome words in the text are: ', end='')
    print(*palins, sep=', ')