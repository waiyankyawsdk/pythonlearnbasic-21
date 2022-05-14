#help(str)
#print(dir(str))
#format

num1 = 100
num2 = 200
print("Value of num is {0} and value of num2 {1}".format(num1,num2))
print("Value of num is {1} and value of num2 {0}".format(num1,num2))
print("Value of num is {val2} and value of num2 {val1}".format(val1=num1,val2=num2))

str = "python sample string"
print(id(str))
s1 = str.capitalize()
print(s1)
print(id(s1))

#upper
#lower
#title

print(str.upper())
print(str.isupper())
print(str.lower())
print(str.title())

#isupper
print(s1.isupper())
print(str.isupper())
#islower
print(str.islower())
#istitle
print(str.istitle())

#split
#join
str2 = "HTML,CSS,Python,Java,Django"
ls = str2.split(",")
# ls = str2.split(" ")
print(ls)

str3 = (" ").join(ls)
print(str3)

#maketrans
#tranlate
st1 = "abcd"
st2 = "1234"
print(str.isupper())
st3 = "Python Sample cat string abcd"

table = str.maketrans(st1,st2)
result = st3.translate(table)
print(result)

#index
#find
#rfind function

print("Python" in str2)
print(str2.index("Python"))
#print(str2.index("python"))

#find : -1 not found
print(str2.find("CSS"))

print(str2.rfind("Python"))

#strip lstrip rstrip
sample = "         This is sample lot of space string        "
sample1 = sample.strip(" ")
print(sample1)
sample = "******This is sample lot of space string*****"
sample1 = sample.lstrip("*")
print(sample1)
sample2 = sample.rstrip("*")
print(sample2)

#center
#ljust
#rjust
p = "python"
exercise = p.center(20,"*")
print(exercise)
exercise1 = p.ljust(20,"*")
print(exercise1)
exercise2 = p.rjust(20,"*")
print(exercise2)

#replace
repl = str2.replace("HTML","HTML5")
print(repl)

help(str)
print(dir(str))




