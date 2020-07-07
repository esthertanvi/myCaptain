#Assigning elements to list
myList = []
myList = [10, 20, 30, 40]
print("\nlist of numbers: " +str(myList))
myList.append(50)
myList.append(60)
myList.append(70)
print("\nList after addition of three new elements: " +str(myList))


#Accesing elements from a tuple
myTuple = ('C', 'C++', 'Java')
print("\n" +str(myTuple))
print("\nFirst element of the tuple is: " +myTuple[0])
print("\nThird element of the tuple is: " +myTuple[2])

#Deleting different dictionary elements
myDict = {"Tanvi" : 20, "Sudeep" : 22, "Srujana" : 21}
print("\nThe original dictionary is: " +str(myDict))
del myDict["Sudeep"]
print("\nDictionary after removing an element: "+str(myDict))
del myDict["Tanvi"]
print("\nDictionary after removing another element is: "+str(myDict))

