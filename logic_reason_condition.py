# condition statement
#if else elif are used to form different action  == !=
#execute code if condition is met


age =21

#execute code if condition is met
if age>18:      
	print("Yor are old enough to drive ")
else:
	print("You are not old enough to drive")

#execute code if condition is met
if age >=21:
	print("You are old enought o drive a bus")


#Multiple conditions
elif age>=18:
	print("you are old enogh to drive a sedan")
else:
	print("You are old enough to drive")

#combine mulltiple conditions with logiical operator
if((age>=1) and (age<=18)):
	print("Your birthday is within this range") #if this condition is met we aint going to the other condition

#multiple conditions
elif (age==21) or (age>=65):
	print("you get a birthday today")
#does the opposite of the elif 
elif not (age==30):
	print("You dont have a birthday")
else:
	print("You get a birthday party")