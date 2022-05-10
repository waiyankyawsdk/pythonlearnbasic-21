#break
#continue
#enumerate

for value in range(10) :
	print(value)

l = [10,20,30,40,50,60]
key = 30

for value in l:
	if value == key:
		print("Element found")
		break
	else:
		# continue
		pass
		print("Statement for pass Statement")
else:
		print("Element not found")

print("Statement after the for loop")

#eunmerate method
for index,value in enumerate(l):
	# print(index,value)
	if value == key:
		print("Element found at index",index)
		break
	else:
		continue
		print("Statement after continue Statement")
else:
	print("Element not found")

# for value in l:

# else:
# break
# continue
# pass
# enumerate
