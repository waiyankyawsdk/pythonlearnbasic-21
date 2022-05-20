#1 Code reuse
#2 Modularity

s = "Python,HTML,CSS"
print(s.index("HTML"))

#1 fun call
#2 fun def

#declare
def value_reverse(value):
	if type(value) == list or type(value)==str:
		reverse = value[::-1]
	else:
		temp = str(value)
		reverse = temp[::-1]
	return reverse

#call
s = "Python"
result = value_reverse(s)
print(result)

l = [10,20,30,40]
print(l.append(50))

l = [100,200,300,400]
result = value_reverse(l)
print(result)

num = 100
result = value_reverse(num)
print(result)
