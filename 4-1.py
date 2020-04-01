n=int(input("Enter a number:"))
count=0
while (n>0):
  count=count+1
  n=n//10
print("The number of digits are:",count)


x=int(input("Enter number 1:"))
y=int(input("Enter number 2:"))
sum1=0
sum2=0
for i in range (1,x):
  if x%i==0:
    sum1+=i
for j in range(1,y):
  if y%j==0:
     sum2+=j
if(sum1==x and sum2==y):
  print('Friendly pair')
else:
  print('Not friendly pair')

def maxHandshake(n):
  return int((n*(n-1))/2)
n=int(input("Enter a number:"))
print(maxHandshake(n))


num=int(input("Enter a number:"))
sum=0
tempt=num
while tempt>0:
  digit=tempt%10
  sum+=digit**3
  tempt//=10

if num==sum:
  print(num,"Armstrong")

else:
  print(num,"Not Armstrong")




