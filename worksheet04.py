#1
def func1():
  str = input()
  print(len(str))
print(func1())

#2
def calculateSum(num):
 if num:
  return num + calculateSum(num-1)
 else:
  return 0
res = calculateSum(10)
print(res)

#3
def printEveIndexChar(str):
 for i in range(0, len(str)-1, 2):
    inputStr = input("Enter String ")
    print("Printing only even index chars")
    printEveIndexChar(inputStr)

#4
def isFirst_And_Last_Same(numberList):
 firstElement = numberList[0]
 lastElement = numberList[-1]
 if(firstElement == lastElement):
  return True
 else:
  return False
numList = [10, 20, 30, 40, 10]
print("The first and last number of a list is same")
print("result is", isFirst_And_Last_Same(numList))
