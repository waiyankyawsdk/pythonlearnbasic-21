#iterator
l = [100,200,300,400,500]
i = iter(l)
#print(i)
# print(next(i))
# print(next(i))

# for value in i:
#     print(value)

# #itertools
import itertools

l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
l3 = [1000,2000,3000,4000,5000]

i = itertools.chain(l1,l2,l3)
#print(i)

#islice()
for value in itertools.islice(i,0,10):
    print(value)

# l = [10,20,30,40,50]
# count = 0
# for value in itertools.cycle(l):
#     if count < 20:
#         print(value)
#     else:
#         break
#     count+=1

# l = [10,20,30,40,50]
# count = 0

#repeat
# for value in itertools.repeat(l):
#     if count < 20:
#         print(value)
#     else:
#         break
#     count+=1

l = [10,20,30,40]
#iter
i = iter(l)
#tee
t = itertools.tee(i)
# print(t)
for value in t[0]:
    print(value)

#print(next(i))
#two main reasons why such an “iterator algebra”
#1. improved memory efficiency
#2.faster execuction time.
for value in t[1]:
    print(value)

#range(10,50)
count = 0
for value in itertools.count(10,5):
    if count >20:
        break
    else:
        print(value)
    count+=1

#0~20
count = 0
for value in itertools.count():
    if count >20:
        break
    else:
        print(value)
    count+=1

l = [1,2,3]

#permutations
print(list(itertools.permutations(l,2)))
print(list(itertools.combinations(l,2)))