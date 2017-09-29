# If it's raining and sunny, I might look for a rainbow! 
is_raining = True
is_sunny = True

if is_raining and is_sunny:
	print("Is there a rainbow")
	

# 
# 

 # I want to send a promotional email to a customer 
 # if they have not requested to be taken off the email list 
 # and if they're in a location where they'll be able to redeem the offer. 
 # Otherwise, I should not bother them with my message.

def send_email():
 	print("Sending email...")

do_not_email = False
location = "USA"

if (not do_not_email) and (location == "USA" or location == "CAN"):
 	send_email()



 # Imagine an air traffic control program that tracks three variables,
 # altitude, speed and propulsion which for a particular aeroplane have the values specified below.

altitude = 10000
speed = 250
propulsion = "Propeller"

 	
print("altitude < 1000 and speed > 100: "+ str(altitude < 1000 and speed > 100)) 
# Result => False
print("(propulsion == \"Jet\" or propulsion == \"Turboprop\") and speed < 300 and altitude > 20000: "+ str((propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000))
# Result => False
print("not (speed > 400 and propulsion == \"Propeller\"): "+ str(not (speed > 400 and propulsion == "Propeller"))) 
# Result => True
print("(altitude > 500 and speed > 100) or not propulsion = \"Propeller\": "+ str((altitude > 500 and speed > 100) or not (propulsion == "Propeller")))
# Result => True
