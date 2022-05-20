#1 Positional argument
#2 Default argument

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