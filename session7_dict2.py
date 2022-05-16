li1 = [1,2,3,4,5]
li2 = [1,4,9,16,25]

#zip 
d = dict(zip(li1,li2))
print(d)

#dict.fromkeys
dt = dict.fromkeys(li1)
print(dt)
dt = dict.fromkeys(li1,0)
print(dt)	#all assign zero

d1 = { 1:1, 2:4, 3:9, 4:16}
d2 = { 5:25, 6:36, 7:49}

#update
d1.update(d2)
print(d1)

#pop
#popitem
#clear
#del
#pop (key item)
r = d1.pop(2)
print(d1,r)

#popitem(random item)
r1 = d1.popitem()
print(d1,r)

d1.clear()
print(d1)

del d1
print(d1)