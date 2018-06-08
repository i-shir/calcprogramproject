import math
#Iroha and Emily
#Limit
#y=x^2


a=float(input('Place to evaluate limit: '))
tol = float(input('tolerance: '))
h=0.0000001
m=a-h
print('m:',m) 
p=a+h
print('p:',p) 

M=m**2
P=p**2

d=P-M
print ('d:',d)

if (abs(float(d)) <= (tol)):
    print('limit exists')
else:
    print('limit does not exist')
