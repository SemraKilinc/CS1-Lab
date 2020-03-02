for x in range(2000,3201):
  if(x%7==0):
    if(x%5!=0):
      print(x,end=" ")

def fact(x):
  if x == 0:
    return 1
  return x * fact(x - 1)

x=int(input())
print(fact(x))

Number=int(input("Enter the number:"))
dictionary=dict()
for i in range(1,Number+1):
  dictionary[i]=i*i
print(dictionary)
