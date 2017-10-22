total = 0
counter = 0
while True:
	entry = input("Enter a number: ")
	if entry == "done":
		break
	try:
		ientry = int(entry)
	except:
		print("INVALID INPUT")
		continue
	total = total + ientry
	counter = counter + 1

print("total:",total,"\ncounter:",counter,"\naverage:",float(total)/counter)
