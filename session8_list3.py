li = [10,20,30,40,50]
li[2] = 300
print(li)

#pop
#remove
#clear
#del

r = li.pop()
print(li,r)
r = li.pop(1)
print(li,r)

li.remove(300)
print(li)
#li.remove(20) #not in list

li.clear()
print(li)

del li
# print(li)

#sort
#reverse
ls = [50,40,30,20,10]
ls.sort()
print(ls)
# print(ls[::-1])
ls.reverse()
print(ls)

l3 = sorted(ls)
print(l3)

#index
#count
print(ls.index(30))
print(ls.count(30))

#list concatenation
print(ls + l3)

#times of list 
li = [0.1]
print(li*15)


