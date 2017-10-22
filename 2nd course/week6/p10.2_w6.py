name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
dic = dict()
for line in handle :
	if not line.startswith("From "):
		continue
	line = line.split()
	time = line[5]
	time = time.split(":")
	hour = time[0]
	lst.append(hour)

for hours in lst:
	dic[hours] = dic.get(hours,0)+1

for k,v in sorted(dic.items()):
	print(k,v)