def change_pos(my_l):
    for i in range(0,len(my_l),2):
        my_l[i],my_l[i+1]=my_l[i+1],my_l[i]
        return my_l
my_l=[0,1,2,3,4,5]
print(change_pos(my_l))

