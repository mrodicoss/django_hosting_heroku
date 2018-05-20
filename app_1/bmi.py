
def calculate_bmi(height, weight):
	if weight < 46 or weight > 200:
		return -1.0
	if height < 1.1 or height > 2.30:
		return -1.0
	try:
		return round(weight / (height * height), 2)
	except ZeroDivisionError:
		return -1.0