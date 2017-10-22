import re

fname = input("Enter the file name:")
try:
	# Open the file and read it and save it in a string variable
	strfile = open(fname).read()
except :
	print("file doesn't exist")
	quit()
# here we look for digits from the file and add them to the list
newlist = re.findall('[0-9]+',strfile)

total = 0
for x in newlist:
	try:
		x= int(x)
	except:
		print(x, "is not an integer")
		quit()
	total = total + x
print("Sum =",total)