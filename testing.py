	row = str(get_row)
	# Determine if the string has a range between XX.50 to XX.59
# Determine if the string has a range between XX.50 to XX.59
	row = [character for character in row if character.isalnum()]
	row = int("".join(row))
	row = str(row)
	if row.endswith("0"):
		row = int(row)
		if(row % 10 !=0):
			row = (row - row % 10) + 10
		row = str(row) + "0"

	print(type(row))
	print(row)
	row = str(row)
	if row.endswith("5", 2,3):
		row = int(row)
		row = round(row,-2)

	elif row.endswith("0", 2,3):
		row = int(row)
		if(row % 10 !=0):
			row = (row - row % 10) + 10
		row = str(row)

	elif row.endswith("1", 2,3) or row.endswith("2", 2,3) or row.endswith("3", 2,3) or row.endswith("4", 2,3):
		row = int(row)
		if(row % 10 !=0):
			row = (row - row % 10) + 10
			get_row = str(row)
		row = str(row)

	else:
		get_row = 0

	get_row = str(row)