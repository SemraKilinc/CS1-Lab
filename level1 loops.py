a = [1,2,3,4,5]
for i in a:
  print i


for i in a:
  b.append(i**2)


for i in range(1,101):
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)

  
for i in even:
  if i%4 == 0:
    four.append(i)
  if i%6 == 0:
    six.append(i)