def insertionsort(list1):

    for i in range(1,len(list1)):
        term = list1[i]
        while(list1[i-1] > term and i > 0):
            list1[i-1],list1[i] = list1[i],list1[i-1]

            i -= 1
        
    return list1

print('lets insertion sort !')
print(insertionsort([5,6,7,8,3,4,5,2,1]))