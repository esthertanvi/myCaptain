#python program to print all the positive numbers in a range

myList= []
n = int(input("Enter the total number of elements in the list:"))
for i in range(1,n+1):
    a = int(input("enter the value of %d element:" %i))
    myList.append(a)
print("Positive numbers in this list are: ")
for j in range(n):
    if(myList[j]>=0):
        print(myList[j], end=' ')
