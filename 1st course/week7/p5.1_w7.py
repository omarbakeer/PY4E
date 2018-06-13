total = 0
counter = 0
while True:
	entry = input("Enter a number: ")
	if entry == "done":
		break
	try:
		fentry = float(entry)
	except:
		print("INVALID INPUT")
		continue
	total = total + fentry
	counter = counter + 1

print("total:","%.3f" % total,"\ncounter:",counter,"\naverage:",float(total)/counter)
