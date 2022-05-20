#1 Positional argument
#2 Default argument
#3 Keyword argument
#4 Variable length position argument
#5 Varibale length keyword argument

def linear_search(l,key):
	for value in l:
		if key==value:
			return True
		else:
			return False
l = [100,200,300,400,500]
key = 400
result = linear_search(l,key)
# result = linear_search(l)
# result = linear_search(l,key,300)
print(result)

#2 Default argument
#8 char
#1 Upper
#1 lower
#1 Special char
#5 Digits
#
#ord
#chr

print(ord('a'),ord('z'))
print(ord('A'),ord('Z'))
print(chr(97),chr(90))

#random password generate func
import random
def gen_password(length=8):
	l = ['@','#','$','&']

	upper = chr(random.randint(65,90))
	lower = chr(random.randint(97,122))
	special = random.choice(l)
	digit = random.randint(10000,99999)

	password = upper + lower + special + str(digit)
	l = random.sample(password,length)
	password = ("").join(l)
	return password

result = gen_password()
print(result)

#validate func
def validate(username,password):
	if username == "ABC" and password == "Abc@123":
		print("Valid Password")
	else:
		print("Invalid Password")

validate("ABC","Abc@123")
validate("abcdABC","Abc@123")
validate(password="Abc@123",username="ABC")

#help(print)

print(100,200,"\n","Hi")
print(100,200,sep= ",",end = " ")

# l = [100,200,300,400]
# l.append(500,250,350)
# print(l)

#variable length args
def add_value(*args):
	l = []
	for value in args:
		l.append(value)

	return l
result = add_value(100,200,300,400,500)
print(result)
result = add_value(100,200)

result = add_value(100,200,300,400,500)
print(result)

#name,email,contact,dob

def get_details(**kwargs):
	print(kwargs)
get_details(name="ABC",email="abc@gmail.com",contact=2123456,dob = "12-05-1890")