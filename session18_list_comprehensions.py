l = [100,200,300,400,500]
l2= [value*value for value in l]

# for value in l:
#     l2.append(value*value)
print(l2)

li = [10,20,25,30,35,60,65,70,85]
li2 = [value for value in li if value%2 == 0]
print(li2)

ls = ['abc','abcd','abcde','zzzz']
ls2 = [len(value) for value in ls]
print(ls2)  #length
#faster than for loop

lt = [(value1,value2)for value1 in range(1,5) for value2 in range(100,103)]
print(lt)
#nested for loop in comprehension

lst = [[1,2,3],[4,5,6],[7,8,9]]
lst2 = [val2 for value in lst for val2 in value]
# for value in lst:
#     for val2 in value:
#         lst2.append(val2)
print(lst2) #[1,2,3,4,5,6,...]

la = [100,105,110,115,120]
#even , odd
lb = ["Even" if value%2 == 0 else "Odd" for value in la]
print(lb)

# 1:1,2:4,3:9,4:16
d = {x: x**2 for x in range(1,11)}
print(d)

#'a':97 , 'b':98,'c':99... 'z':122
d = {chr(x):x for x in range(97,123)}
print(d)

# key:value for key,value in list
d2 = {key:value for key,value in d.items()}
print(d2)

d2 = {value:key for key,value in d.items()}
print(d2)