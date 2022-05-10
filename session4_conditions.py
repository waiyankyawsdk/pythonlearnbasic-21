#Conditional Statements :
# if [condition] : 
#		statements
# elif [conditon] :
# else:
# 		statements
num1 = 100
num2 = 200

# 1 num1 is greater
# 2 num2 is greater
# 3 num1 and num2 are equal\
if num1 > num2:
	print("num1 is greater than num2")
elif num2 > num1:
	print("num2 is greater than num1")
else:
	print("num1 is equal to num2")

if 0:
	print("Statement in if block")
else:
	print("Statement in else block")