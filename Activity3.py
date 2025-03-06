list1=[10,6,3,2,7,8]
count=0
for i in list1:
    count+=i
print("The sum of numbers is :" , count)

a=count/len(list1)
print("The average is:" , a)

list1.sort()
print("The smallest element is " , list1[0])
print("The largest element is:" , list1[-1])