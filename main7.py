def numbers(num_list):  
    mul = 1  
    for x in num_list:  
        mul = mul * x   
    print(mul) 


items_to_mul = (8, 2, 3, -1, 7) 
numbers(items_to_mul)

def find_max(a,b,c):
  if a > b and a > c:
    max_nu = a
  elif b > a and b > c:
    max_nu = b
  else:
    max_nu = c
  return max_nu

def main ():
  print("max of 1,2,3=",find_max(1,2,3))
main()

def test_prime(n):
 if (n==1):
    return False
 elif (n==2):
    return True;
 else:
    for x in range(2,n):
      if(n % x==0):
        return False

        return True


print(test_prime(2))


def perfect_number(n):
  sum = 0
  for x in range(1,n):
    if n % x == 0:
      sum += x
  return sum == n
print(perfect_number(6))




def pascal_triangle(n):
  trow=[1]
  y=[0]
  for x in range(max(n,0)):
    print(trow)
    trow=[l+r for l,r in zip(trow+y, y+trow)]
  return n>=1
  pascal_triangle(6)
   