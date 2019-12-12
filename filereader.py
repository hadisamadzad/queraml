def read(path):
	with open(path, "r") as file:
		str = file.read()
	return str

def readAndSplitLines(path):
	with open(path, "r") as file:
		str = file.read()
	return str.split('\n')