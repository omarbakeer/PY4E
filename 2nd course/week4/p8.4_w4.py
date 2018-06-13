fname = input("Enter file name: ")
fh = open(fname)
lst = list()
cleanlst = list()
for line in fh:
	string = line.rstrip().split()
	for word in string:
		lst.append(word)

for x in lst:
	if x in cleanlst :
		continue
	cleanlst.append(x)
cleanlst.sort()
print(cleanlst)
