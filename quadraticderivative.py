import math
#Iroha and Emily
#Derivatives
#y=quadratic

#y=ax^2+bx+c

a=float(input('value of a:'))
b=float(input('value of b:'))
c=float(input('value of c:'))

p=a+h
p=p**2
a=a**2

D=(p-a)/h
print('limit =', D)
