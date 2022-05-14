#lists
#1 list are mutable : add update and delete
#2 ordered indexing and slicing
#3 heterogeneous datatype (any)
li = [10,20,0,40,"Python","Java",[100,200,300]]
print(li,type(li))	#[10, 20, 0, 40, 'Python', 'Java', [100, 200, 300]] <class 'list'>


print(li[-1])	#last element [100, 200, 300]
# print(li[20]) #out of range

print(li[1:3])	#[20, 0]
print(li[::-1])	#reverse order [100, 200, 300], 'Java', 'Python', 40, 0, 20, 10]

# for value in li:
# 	print(value)

for value in li[::2]:
	print(value)

#append

#before append id
print(id(li),li)
li.append(600)
#after append id
print(id(li),li)

num1 = 10
print(id(num1))

li.append(700)
print(id(li[0]),li)

#extend
li.extend([500,600,700,800])
print(li)

#Note:
#1 append() and extend() can only add one argument
#2 string are stored separately.
li.extend("Python")
print(li)

#insert
li.insert(1,200)	#insert with index number
print(li)

#list assignment
ls = [1,2,3]
ls1 = ls
ls.append(4)
print(id(ls),id(ls1))
print(ls,ls1)
