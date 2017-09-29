def which_prize(score_points):
	"""
	Points 	Prize
	0 - 50 	wooden rabbit
	51 - 150 	No prize
	151 - 180 	wafer-thin mint
	181 - 200 	penguin
	"""
	if 0<= score_points <= 50:
		prize_name = "wooden rabbit"
		prize_message = "\"Congratulations! You have won a {}!\"".format(prize_name)
	elif 51<= score_points <= 150:
		prize_name = "No prize"
		prize_message = "\"Oh dear, no prize this time.\""
	elif 151<= score_points <= 180:
		prize_name = "wafer-thin mint"
		prize_message = "\"Congratulations! You have won a {}!\"".format(prize_name)
	elif 181<= score_points <= 200:
		prize_name = "penguin"
		prize_message = "\"Congratulations! You have won a {}!\"".format(prize_name)

	return prize_message

print(which_prize(188))