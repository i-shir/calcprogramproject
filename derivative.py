import math
#Iroha and Emily
#Derivatives
#y=x^2

h=float(input('value of h:'))
a=float(input('value of a:'))
p=a+h
p=p**2
a=a**2

D=(p-a)/h
print('limit =', D)
