phone_balance = 9
bank_balance = 100000000


if phone_balance < 10:
	phone_balance += 10
	bank_balance -= 10


print("Phone Balance: " + str(phone_balance))
print("Bank Balance: " + str(bank_balance))


weight_in_kg = 55
height_in_m = 1.2

if 18.5 <= weight_in_kg/(height_in_m**2) < 25:
	print("BMI is considered 'normal'.")


number = 10

if number % 2 == 0:
	print("{} is even.".format(number))
else:
	print("{} is odd.".format(number))





def garden_calendar(season):
	if season == "spring":
		print("Current season is {}. time to plant the garden!".format(season))
	elif season == "summer":
		print("Current season is {}. time to water the garden!".format(season))
	elif season == "autumn" or season == "fall":
		print("Current season is {}. time to harvest the garden!".format(season))
	elif season == "winter":
		print("Current season is {}. time to stay indoors and drink tea!".format(season))
	else :
		print("Don't recognize the season.")


garden_calendar("winter")

	