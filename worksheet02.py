#1
data = list(map(int, input("Numbers: ").split()))
for i in data:
  if (i == i+1):
    print("same")
  else:
    print ("different")
#2
def pythagoras(opposite_side,adjacent_side,hypotenuse):
 if opposite_side == str("x"):
  return ("Opposite = " + str(((hypotenuse**2) -
  (adjacent_side**2))**0.5))
 elif adjacent_side == str("x"):
  return ("Adjacent = " + str(((hypotenuse**2) -
  (opposite_side**2))**0.5))
 elif hypotenuse == str("x"):
  return ("Hypotenuse = " + str(((opposite_side**2) +
  (adjacent_side**2))**0.5))
 else:
  return "True!"

print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))

#3
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello " + lname + " " + fname)

#4
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)


#5
x = input("Input the first number")
y = input("Input the second number")
z = input("Input the third number")
print("Median of the above three numbers -")
if y < x and x < z:
 print(x)
elif z < x and x < y:
 print(x)
elif z < y and y < x:
 print(y)
elif x < y and y < z:
 print(y)
elif y < z and z < x:
 print(z)
elif x < z and z < y:
 print(z)