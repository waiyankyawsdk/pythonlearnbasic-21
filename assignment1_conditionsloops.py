#1. Write a Python program to find those numbers which are divisible by 7 and 5, between 1500 and 2700 (both included).
for value in range(1500,2700):
	if value % 7 == 0 and value % 5 == 0:
		print(value)


#2. Write a Python program to count the number of even and odd numbers from a series of numbers.
#	numbers = (1,2,3,4,5,6,7,8,9)
#	Expected output : Number of even numbers : 5
#					  Number of odd numbers : 4
even = 0 
odd = 0
for numbers in range(0,10):
	if numbers % 2 == 0:
		even+=1
	else:
		odd+=1
print("Number of even number :",even)
print("Number of odd number :",odd)

#3 Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
str_mul_3 = "fizz"
str_mul_5 = "bizz"
str_mul_both = "fizzbizz"
for multiples in range(1,51):
	if multiples%3 == 0:
		if multiples % 5 ==0:
				print(str_mul_both)
				continue
		print(str_mul_3)
		continue
	elif multiples % 5 == 0:
		print(str_mul_5)
		continue
	
	print(multiples)
#4 Write a Python program to calculate the sum and average of n integer numbers.
#
sum = 0
avg = 0
for value in range(1,11):
	sum += value
	avg = sum/10
	print("Sum of integer number:",sum)
	print("Average of integer number:",avg)
#5 Write a Python program to calculate factorial of a number (n!).
#
def factorial(n):
	if n == 0:
		print(1)
	else:
		print (n * (n-1))

factorial(0)