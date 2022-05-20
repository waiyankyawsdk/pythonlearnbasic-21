"""
Docstring : this module contains binart search implementation.



"""




# factorial(5) = 5 * fact(4)
# 					4	* fact(3)
# 							3 * fact(2)
# 								2 * fact(1)
# 									1

def factorial(num): 									
	if num == 1:
		return 1
	else:
		return num * factorial(num -1)

num1 = 5
result = factorial(num1)
print(result)

# factorial(5) = 5 * 24 = 120
# 					4	* 6 = 24
# 							3 * 2 = 6
# 								2 * 1 = 2
# 									1

def binary_search(l,key):
	"""
	Binray search : input a list and key
	return True if key exist else return false
	
	"""


	if len(l) == 0:
		return False
	else:
		mid = len(l) //2

		if l[mid] == key:
			return True
		elif key < l[mid]:
			return binary_search(l[:mid],key)
		else:
			return binary_search(l[mid+1:],key)

l = [100,200,300,400,500,600,700,800,900]
key = 2000
result = binary_search(l,key)
print(result)
#binary search
# l = [100,200,300,400,500,600,700,800,900]
# key = 700

# mid = 9 / 2 = l[4] = 500

# l = [600,700,800,900]

# mid = 4 / 2 = l[2] = 800

# 800 == 700

# [600,700]

# mid = 2 / 2 = 1

# 700 = 700 return True

#print(__name__)
if __name__ == "__main__" :
	l = [100,200,300,400,500,600,700,800,900]
	key = 100
	result = binary_search(l,key)
	print(result)