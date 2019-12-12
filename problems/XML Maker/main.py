from mylib import clear

# Clearing the console
clear()

# My Code
file = open("input.txt", "r")
username = file.readline().strip()
password = file.readline().strip()
inputs = file.readline().strip()
name = inputs.split()[0]
age = int(inputs.split()[1])
bmi = float(inputs.split()[2])

print("<user>")
print(f"\t<combo>{username}:{password}</combo>")
print(f"\t<name>{name}</name>")
print(f"\t<age>{age}</age>")
print("\t<bmi>","{:.3f}".format(bmi),"</bmi>", sep="")
print("</user>")