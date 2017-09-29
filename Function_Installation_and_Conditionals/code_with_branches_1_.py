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

print("\n\n")
#Third Example 

#change the age to experiment with the pricing
age = 35

#set the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

#set bus fares
concession_ticket = 1.25
adult_ticket = 2.50

#ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age,ticket_price)
print(message)

	