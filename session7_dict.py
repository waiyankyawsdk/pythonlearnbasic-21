#dict:
#1 mutable
#2 unordered data structure
#3 keys should be unique
#4 keys should be immutable int float str tuple
d = {"emp_id" : 101, "name":"ABC","email":"abc@gmail.com"}
print(d)

d["contact_no"] = 123456
print(d)
d["contact_no"] = 78912
print(d)
#print(d[0]) 
#print(d["age"])

#get
#setdefault
print(d.get("emp_id"))
print(d.get("age"))
print(d.get("age",-1))
print(d.get("age","key does not exist"))

print(d.setdefault("emp_id"))
print(d.setdefault("age"))
#setdefault added elements into dict
print(d)

for keys in d:
	print(keys,d[keys])

#1:1,2:4,3:9 ... 10:100
dt = {}
for values in range(1,11):
	dt[values] = values * values
print(dt)

#keys
#values
#items

print(d.keys())
print(d.values())
print(d.items())

for t in d.items():
	print(t)