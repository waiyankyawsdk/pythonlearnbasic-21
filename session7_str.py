# string
# s = '' "" """ """
# 1 Strings are immutable
# 
str ="Python sample string"
print(type(str))

#immutable id change
s1 = "Python"
print(id(s1))
s1 = "Java"
print(id(s1))

#string location Indexing
print(str[0])
print(str[3])
print(str[-3])
# print(str[100])
 
# Slicing 0:6 means 0~5
print(str[0:6])
print(str[7:])  #go to end
print(str[:6])  #0:6

#stride
print(str[::2])
print(str[::3])
#reverse order
print(str[::-1])

print(str[6:0])

for value in str[::2]:
	print(value)

#help(str)