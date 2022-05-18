li = [100,200,300,400,500]
print(sum(li))
print(max(li))
print(min(li))

num = 25.555
print(round(num))
print(round(num,2))

#print(dir(__builtins__))
#help(__builtins__)

import math

l = [0.1] * 10
print(l)
print(sum(l))
print(math.fsum(l))

#15 16

num1 = 15.5559
print(math.floor(num1),math.ceil(num1))

print(math.sqrt(25))

print(math.factorial(5))

num2 = 45.5556
print(math.modf(num2))

d , i = math.modf(num2)
print(d,i)

print(math.pow(10,2))

print(math.log(10,2))	#log 10 to base 2
print(math.log2(10))

print(math.log10(2))

print(math.sin(0))
print(math.sin(math.radians(30)))
print(math.tan(math.radians(30)))

#help(math)
#print(dir(math))

import random

print(random.random()) #between 0 to 1

l = [ 1,2,3,4,5,6]
print(random.choice(l))

print(random.randint(10,100))
print(random.randint(1,3))
print(random.randrange(1,13))
print(random.randrange(10,100))

print(random.uniform(10,20))


