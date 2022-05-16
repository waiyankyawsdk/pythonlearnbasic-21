#sets:
#1 Sets are mutable
#2 All elements should be unique
#3 immutable elements in the set - in float tuple str
#4 Unordered

s = {10,20,30,40,10,20,30}
print(s,type(s))

st = {20,40,100,200,300,400}
st.add(500)
print(st)

#union
su = s.union(st)
print(su)

#intersection
si = s.intersection(st)
print(si)

#difference
sd = s.difference(st)
print(sd)	#common elements only

#symmetric_difference
ssd = s.symmetric_difference(st)
print(ssd)	#common element not output

print(s,st)
#update
# s.update(st)
# print(s)

#intersection_update
# s.intersection_update(st)
# print(s)

#difference_update
# s.difference_update(st)
# print(s)

#symmetric_difference_update
# s.symmetric_difference_update(st)
# print(s)

s1 = { 100,200,300,400,500}
s2 = { 100,200,300}
#is s2 of all elments existed in s1? issubset()
print(s2.issubset(s1))
print(s1.issuperset(s2))

li = [100,200,300,400]
ss = set(li)
print(ss)

ls1 = [100,200,300,400,500]
ls2 = [50,100,150,200,250,500,45,35,20,10]

set1 = set(ls1)
set2 = set(ls2)

#union 
set3 = set1.union(set2)
print(set3)

# list3 = list(set3)
# print(list3)

# list3.sort()
# print(list3)


# sorted
#list() + sort()
list3 = sorted(set3)
print(list3)

#pop
#remove
#discard
#clear
#del

print(s)
r = s.pop()
print(s,r)

#del with specific value
s.remove(10)
print(s)

s.discard(20)
print(s)

s.clear()
print(s)
