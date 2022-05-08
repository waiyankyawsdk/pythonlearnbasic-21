# # Operators in Python
# 1 Arithmetic operators +,-,*,/,//, %, **
#2 Comparison operators <,>,<=,>=,==,!=

num1 = 100
num2 = 200
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

print(10/3)

#floor operator
print(10//3)

#divider operator
print(10%3)

#upper operator
print(10 ** 3)

#2 Comparison operators <,>,<=,>=,==,!=
print(num1 == num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 != num2)

#3 Identity operators : is is not
#is means == but output results (false) because of memory location id is not the same
print(num1 is num2)

l = [10,20,30]
l2 = [10,20,30]
print(l is l2)
print(l is not l2)

#4 Assignment operators =,+=,-=,*=,/=
num1 += 5
print(num1)
num1 -= 5
print(num1)

#5 Bitwise Operators : &,|,^,>>,<<
# bin function
print(bin(num1),bin(num2))
#bitwise &
print(num1 & num2)
print(num1 | num2)
print(2 >> 1)
print(2 << 1)

#6 Logical operators : and or not
print(10==10 and 20==20)
print(10==15 and 20==20)
print(10==15 or 20==20)
print(not(10==10))
print(not(10==15))

#7 Membership operators : in, not in
# check in or not
l1 = [10,20,30,40.50]
print(30 in l1)
print(300 in l1)

str = "Python string"
print("Python" in str)
print("python" in str)
