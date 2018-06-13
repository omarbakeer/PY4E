fname = input("Enter the file name :")
try:
	fhandle = open(fname,'r')
except:
	print("The file you entered is not found")
	quit()
lineCounter = 0
total = 0.0
for line in fhandle:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	lineCounter = lineCounter + 1
	ncolon = line.find(":")
	subtext = line[ncolon+1:]
	snum = subtext.strip()
	temp = float(snum)
	total = total + temp
avg = total / lineCounter
print("Total value:", "%.4f" %total, "\nNumber of lines:", lineCounter, "\nAverage spam confidence:", avg)
