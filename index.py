#task = Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird



#solution
n = input('type a number' )

if n%2==1:
  print('Weird')
if n in range(2,5) and n%2==0:
  print('Not Weird')
if n in range(5,21) and n%2==0:
  print('weird')
if n>20 and n%2==0:
  print('Not Weird')


