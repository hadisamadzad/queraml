from filereader import read

input = read("input.txt")
numbers = [int(num) for num in input.split()]
numbers.sort()

count = len(numbers)

mean = "{:.2f}".format(sum(numbers) / count)
median = "{:.2f}".format(0.5 * (numbers[count // 2 - 1] + numbers[count // 2]) if count % 2 == 0 else numbers[count // 2])
mode = max(set(numbers), key=numbers.count)

print(mean)
print(median)
print(mode)