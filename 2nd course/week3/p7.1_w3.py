fname = input("Enter the file name :")
try:
	fhandle = open(fname,'r')
except:
	print("The file you entered is not found")
	quit()
for line in fhandle:
	print(line.upper().strip())