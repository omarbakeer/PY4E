fname = input("Enter the file name :")
try:
	fhandle = open(fname,'r')
except:
	print("The file you entered is not found")
	quit()
lineCounter = 0
avg = 0.0
for line in fhandle:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	lineCounter = lineCounter + 1
	ncolon = line.find(":")
	subtext = line[ncolon+1:]
	snum = subtext.strip()
	temp = float(snum)
	avg = avg + temp
avg = avg / lineCounter
print("Average spam confidence:", avg)
