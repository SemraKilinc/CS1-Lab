#1
num = input("Enter a number: ")
mod = num % 2
if mod > 0:
  print("odd number")
else:
  print("even number")

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
  print(num, "multiple of 4")
elif num % 2 == 0:
  print(num, "is an even number")
else:
  print(num, "is an odd number")

if num % check == 0:
  print(num, "divides evenly by", check)
else:
  print(num, "does not divide evenly by", check)

#2
num=input("Enter a number:")
if 0<=num>=10:
  request=input("Enter another number:")
elif 10<=num>=20:
  ask=input("Enter another intiger:")
elif 20<=num>=100:
  print("Your choice is between 20-100.")
else:
  print("Just practicing.")

#4
x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))

#5