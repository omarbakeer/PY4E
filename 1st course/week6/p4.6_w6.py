def computepay(hours , rate):
	bonus = hrs - 40
	return (40 * rate) + (bonus * rate * 1.5)

try:
	hrs = int(input("Enter hours: "))
	rate = float(input("Enter the rate: "))
except:
	print("Invalid input !!")
	quit()
if hrs > 40 :
	payment = computepay(hrs , rate)
else :
	payment = hrs * rate
print(payment)