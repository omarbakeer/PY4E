try:
	hrs = int(input("Enter hours: "))
	rate = float(input("Enter the rate: "))
except:
	print("Invalid input !!")
	quit()
if hrs > 40 :
	bonus = hrs - 40
	payment = (40 * rate) + (bonus * rate * 1.5)
else :
	payment = hrs * rate
print("Pay:",payment)