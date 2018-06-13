maximum = None
minimum = None
while True:
	entry = input("Enter a number: ")
	if entry == "done":
		break
	try:
		fentry = float(entry)
	except:
		print("INVALID INPUT")
		continue
	if maximum is None and minimum is None:
		maximum = fentry
		minimum = fentry
	elif maximum < fentry:
		maximum = fentry
	elif minimum > fentry:
		minimum = fentry

print("Maximum:",maximum,"\nMinimum:",minimum)
