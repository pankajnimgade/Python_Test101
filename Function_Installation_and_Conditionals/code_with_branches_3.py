# True and False are both booleans but it is not a good idea to use if True: or if False:.
# Boolean operators and, or and not have specific meanings that aren't quite the same as their common meanings - 
# don't fall into the trap of writing plain English unless it's also valid Python!
# Do not compare a variable that is a boolean with == True or == False - 
# it's more readable to avoid such a comparison. If you want to check whether a boolean is False, you can use not, for example

# if not real_grail:
    # print("It's a grail-shaped beacon!")


def punctuate(sentance, phrase_type):
	"""
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create. 
                "exclamation", "question" and "aside" are known values.
    """

	if phrase_type == "exclamation":
	    sentence_punct = sentance + "!"
	elif phrase_type == "question" :
	    sentence_punct = sentance + "?"
	elif phrase_type == "aside" :
	    sentence_punct = "(" + sentance + ".)"
	else:
	    sentence_punct = sentance + "."
	return sentence_punct

def puntuate_2(_sentance,_type_phrase):
	# """
 #    Create a punctuated sentence from a string. Defaults to an ordinary
 #    sentence with a full stop.

 #    sentence: string, the phrase that is to have punctuation added
 #    phrase_type: string, defines what kind of sentence to create. 
 #                "exclamation", "question" and "aside" are known values.
 #    """

	if _type_phrase == "exclamation":
		return _sentance+"!"
	elif _type_phrase == "question":
		return _sentance+"?"
	elif _type_phrase == "aside":
		return "("+_sentance+")"
	else:
		return _sentance

def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
    	top_area = (3.14 * radius**2)*2
    	return side_area + top_area
    else:
    	return side_area


print(cylinder_surface_area(5,5,False))
print(cylinder_surface_area(5,5,True))

    

print(puntuate_2("What is your name", "question"))

print(punctuate("Hello world", "exclamation"))

