#loops in python
#1 for loop
#2 while loop

#Iterable datatypes:
# str list tuple dict set

# for [variable_name] in [iterable datatype]:
# 		statements

# l = [10,20,30,40,50]

sum = 0
for value in range(1,21):
	sum = sum + value
	print(value,sum)

#range(5) 0 1 2 3 4
#range(10,100) 10 11 12 13 14 ... 99
#range(10,100,5) 10 15 20 25 30 ... 95 100
# li = [1,2,3,4,5...20]

for val in range(10,) :
	print(val)
for val in range(10,100) :
	print(val)
for val in range(10,100,5) :
	print(val)