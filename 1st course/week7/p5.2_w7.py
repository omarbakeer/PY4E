maximum = None
minimum = None
while True:
	entry = input("Enter a number: ")
	if entry == "done":
		break
	try:
		ientry = int(entry)
	except:
		print("INVALID INPUT")
		continue
	if maximum is None and minimum is None:
		maximum = ientry
		minimum = ientry
	elif maximum < ientry:
		maximum = ientry
	elif minimum > ientry:
		minimum = ientry

print("Maximum:",maximum,"\nMinimum:",minimum)
