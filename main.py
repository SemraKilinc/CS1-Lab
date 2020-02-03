#ex1
print ("ex1.py")
print ("Hello World")
print ("Hello Again")
print ("I like typing this.")
print ("This is fun.")
print ("Yay! Printing.")
print ("I'd much rather you 'not'.")
print ('I "said" do not touch this.')

#ex2
print("ex2.py")
# A comment, this is so you can read your program later.
#Anything after the # is ignored by python.

print ("I could have code like this.") # and the comment after is ignored.

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run"

print("This will run.")

#ex3
print("ex3.py")
print("I will now count my chickens:")
print ("Hens", 25+30/6)
print ("Roosters",100-25*3%4)
print("Now I will count the eggs.")
print (3+2+1-5+4%2-1/4+6)
print ("Is is true that 3+2<5-7?")
print (3+2<5-7)
print ("What is 3+2?",3+2)
print ("What is 5-7?",5-7)
print ("Oh, that's why it's False.")
print ("How about some more.")
print ("Is it greater?",5>-2)
print ("Is it greater or equal?",5>=-2)
print ("Is it less or equal?",5<=-2)

#ex4.pow
cars=100
space_in_a_car= 4.0
drivers= 30
passengers= 90
cars_not_driven=cars-drivers
cars_driven= drivers
carpool_capacity= cars_driven*space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print ("We have",passengers,"to carpool today.")
print ("We need to put about",average_passengers_per_car,"in each car.")