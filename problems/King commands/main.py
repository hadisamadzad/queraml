from mylib import clear

clear()
file = open("input.txt", "r")

inputs = file.readline().strip()
command = inputs.split()[1]

cost = 0.0;

if command == 'water':
    cost = 0.5
elif command == 'dinner':
    cost = 1.0    
elif command == 'judge':
    cost = 50.0
elif command == 'minister':
    cost = 80.0
elif command == 'governer':
    cost = 100.0
elif command == 'ground':
    cost = 45.0
elif command == 'sea':
    cost = 58.0
else:
    cost = 10.0

print(cost)