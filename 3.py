from math import pi
from math import sin
from math import cos

print('(3 + 4) * 5 = ' + str((3 + 4) * 5))
print('n*(n-1)/2')
n = int(input('Enter the value of n: '))
print(n*(n-1)/2)
print('Area of a sphere: ')
r = float(input('Enter radius: '))
print(4 * pi * r**2)
print('sqrt(rcos2a + rsin2b)')
a = float(input('Enter two angles:'))
b = float(input())
print((r * cos(a)**2 + r * sin(b)**2) ** 0.5 )

print('(y2 - y1)/(x2 - x1)')
y2 = float(input('Enter 4 more numbers: '))
y1 = float(input())
x2 = float(input())
x1 = float(input())

print((y2 - y1) / (x2 - x1))