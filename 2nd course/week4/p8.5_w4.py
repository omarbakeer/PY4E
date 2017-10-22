fname = input("Enter file name: ")
fh = open(fname)
lst = list()
counter = 0
for line in fh:
	if not line.startswith("From "):
		continue
	temp = line.split()
	lst.append(temp[1])
for element in lst:
	counter = counter+1
	print(element)
print("There were",counter,"lines in the file with From as the first word")