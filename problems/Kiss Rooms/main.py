from filereader import read
from filereader import readAndSplitLines

# functions
def countKiss(persons):
    return int(0.5 * persons * (persons - 1))
    
def countTotalKiss(persons):
    res = 0
    for i in range(persons):
        res += countKiss(i + 1)
    return res

# input
input = readAndSplitLines("input.txt")
personCount = input.pop(0)
enters = input

# solution
dict = {}

for enter in enters:
    roomIsEmpty = dict.get(enter, 'Yes')
    
    if roomIsEmpty == 'Yes':
        dict.setdefault(enter, 1)
    else:
        dict[enter] = dict[enter] + 1
    
    print(countTotalKiss(dict[enter]))