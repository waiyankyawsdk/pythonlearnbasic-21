#map
#filter
#lambda
#faster than comprehension and for loop

#map
from operator import truediv


# def sqr(num):
#     return num **2

l = [10,20,30,40,50,60]

result = list(map(lambda x:x**2,l))
print(result)

# for value in result:
#     print(value)
# def add(num1,num2):
#     return num1+num2
l1 = [100,200,300,400,500]
l2 = [10,20,30,40,50]

result = list(map(lambda x,y:x +y,l1,l2))
print(result)

#filter
def check_num(num):
    if num%2 == 0:
        return True
    else:
        return False
l = [100,115,120,125,130,140]

result = list(filter(lambda x:x%2 ==0,l))
print(result)
result = list(map(check_num,l))
print(result)

#lambda : anonymous function

d = { 8:50, 3:40, 2:30, 1:20, 5:10}

l = dict(sorted(d.items(),key= lambda x:x[1]))

print(l)