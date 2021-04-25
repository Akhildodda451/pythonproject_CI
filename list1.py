list1=[13,17,21,27,32]
print(list1)
print("length is",len(list1))
print("type is",type(list1))
print(list1[:])
print(list1[1:])
print(list1[:4])
print(list1[0:5])
list1[1]=[127]
list1[2]=[321]
print(list1)
list1.insert(4,451)
list1.append(672)
print(list1)
list1.remove(32)
list1.pop(1)
del list1[1]
list1[3]=[1,2,3,4,5]
print(list1)
for i in list1:
    print(i)
list2=list1.copy()
print(list2)
list3=list1+list2
print(list3)
list1.reverse()
print(list1)