fname = input("Enter file name: ")
fh = open(fname)
dic = dict()
lst = list() 
counter = 0
for line in fh:
	if not line.startswith("From "):
		continue
	temp = line.split()
	lst.append(temp[1])

for email in lst:
	dic[email] = dic.get(email,0) + 1

mostSending = None
sendingTimes = None
for email,count in dic.items():
	if mostSending is None or sendingTimes < count:
		mostSending = email
		sendingTimes = count
print(mostSending, sendingTimes)