import re

# . - any char
# [a-zA-Z] - char class a or b or c ... or z A or B or ... Z
# [0-9] - digit class 0 or 1 or 2 ... or 9
# 
# + -atleast one [a-z]+
# * -zero or more
# 
# ^ -start of the string
# $ -end of the string
# 
# ? -optional
# () -group 1 2 3
# [a-z]{2,4}

s = "ABCDE1234A"
s = "ABCDE12345A"
s = "aaABCDE1234A"
s = "AaaABCDE1234A"
#compile 
#findall
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]")
l = re.findall(r,s)
print(l)

s="8123456798"
r = re.compile("^[6-9][0-9]{9}$")
l = re.findall(r,s)
print(l)

# dd-mm-yyy
s = "12-05-2018"
# r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
#grouping
r = re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
# l = re.findall(r,s)
# print(l)

#search
#group
#s = "12-05-2018"
m = re.search(r,s)
# print(m)
# print(m.group())

if m:
	print(m.group("date"))
	# print(m.group("month"))
	# print(m.group("year"))
else:
	print("Pattern not found")

#country code
s = "+91 8123456798"
r = re.compile("(\+91?\s)([6-9][0-9]{9})")
m = re.search(r,s)

if m:
	print(m.group(2))
else:
	print("Pattern not found")

# [0-9]	\d
#[^0-9]	\d
#[a-zA-Z0-9] \w
#\W
#space	\s
#\S

