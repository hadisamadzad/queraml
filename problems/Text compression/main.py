str = ""
file = open("input.txt", "r")
str = file.readline().strip()
length = len(str)
print(str)

start = 0
block = ""
blocklen = 1

for i, ch in enumerate(str):
    if i + 1 < length and str[i + 1] == ch:
        blocklen += 1
    elif i + 1 < length and str[i + 1] != ch:
        print(f'{str[start]}{blocklen}', end="")
        start = i + 1
        blocklen = 1
    elif i + 1 == length:
        print(f'{str[start]}{blocklen}', end="")
