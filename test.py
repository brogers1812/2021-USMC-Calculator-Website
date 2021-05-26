mtc = str(4.20)
mtc = [character for character in mtc if character.isalnum()]
mtc = int("".join(mtc))
mtc = str(mtc)
if mtc.endswith("0"):
	mtc = int(mtc)
	if(mtc % 10 !=0):
		mtc = (mtc - mtc % 10) + 10
	if len((abs(mtc))) == 1:
		mtc = mtc * 10
		print("test")
	else:
		mtc = str(mtc)

print(mtc)
print(type(mtc))