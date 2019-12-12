def process(path):
	with open(path, "r") as file:
		str = file.read()
	cases = str.split('\n')

	# Getting Athletes info
	athletes = [(int(case.split()[0]),
			     float(case.split()[1]),
				 float(case.split()[1]) / (float(case.split()[0])/100)**2)
			for case in cases if case.split()[2] == "ATHLETE"]

	athletes_bmi_sum = 0
	for athlete in athletes:
		athletes_bmi_sum += athlete[2]
	athletes_average_bmi = athletes_bmi_sum / len(athletes)

	# Getting Normal people info
	normal_people = [(int(case.split()[0]),
			     float(case.split()[1]),
				 float(case.split()[1]) / (float(case.split()[0])/100)**2)
			for case in cases if case.split()[2] == "NORMAL"]
	
	normal_bmi_sum = 0
	for normal in normal_people:
		normal_bmi_sum += normal[2]
	normal_average_bmi = normal_bmi_sum / len(normal_people)


	return athletes , athletes_average_bmi , normal_people, normal_average_bmi