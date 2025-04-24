#Creating List

l1=[1,2,3,4]
l2=l1[:]
l3=l1[0:2]
print("l1", l1)
print("l2", l2)
print("l3", l3)

l4=[x**2 for x in range(10)]
print(l4)

l5=[value*3 for value in l1]
print('l5 = l1x3', l5)

l6=[i for i in l4 if i%2==0]
print('l6=l4%2==0',l6)

l7=l8=[1,2,3,4,5]
print("l7", l7)
print("l8", l8)
print("id l7", id(l7))
print("id l8", id(l8))

