file = open("inputs.txt", "r")
str = file.readline().strip()
length = len(str)

start = 0
blocks = []
blocklen = 1

for i, ch in enumerate(str):
    if i + 1 < length and str[i + 1].lower() == ch.lower():
        blocklen += 1
    elif i + 1 < length and str[i + 1].lower() != ch.lower():
        blocks.append(str[start:start+blocklen])
        start = i + 1
        blocklen = 1
    elif i + 1 == length:
        blocks.append(str[start:start+blocklen])

for block in blocks:
    keyblock = 0
    for i, ch in enumerate(block):
        keyblock += (i + 1) * (ord(ch) - 64)
    print(keyblock, end="")