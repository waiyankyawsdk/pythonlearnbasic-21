# Datatypes
# 1 int :
num = 100
print(type(num))

#2 float :
num1 = 15.25
print(type(num1))

print(id(num))
print(id(num1 ))

#3 str '' " " """ """
str = " 'Python' sample string"
print(id(str))
print(str,type(str))

#4 list : []
lit = [ 10,20,30,40,50,"Python","Django"]
print(id(lit),list,type(lit))

#append method
lit.append(60)
print(id(lit),lit)

#5 tuple : ()
tup = (10,20,30)

#6 dict :
dicts = {"name":"ABC","email":"abc@gmail.com"}

#7 set {}
st = {10,20,30,40}

#8 boolean : true false

#9 complex : 4 + 3j
#help method
help(complex)