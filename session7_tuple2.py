#tuple:
#immutable datastructure
#ordered indexing and slicing
t = (10,20,20,20,30,30,40)
print(t,type(t))
#help(typle)

print(t[0])
print(t[-1])
#print(t[10]) #out of range

print(t[:3])

print(t.index(20))
print(t.count(20))

li = [10,20,30,40,50]

for t in enumerate(li):
	#print(t)
	print(t[0])
#list to tuple
t = tuple(li)
print(t)

#tuple to list
t=("a","b","c",100)
l = list(t)
print(l,type(l))
