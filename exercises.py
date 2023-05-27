#Add the mathematical functions for the next exercises
import math
#We use the list to put some elements to show
list = [2, 4, 6, 8, 10]
#Print the list that we have writted
print("Available list", list)
#We introduce the numbers of elements that we want to add in the list
element = int(input("How many elements you will add to the list? "))
#There is a loop to repeat the times the storage of new elements
for i in range(element):
    #Here we put the elements what we want
    element = int(input("Enter the element that you want to add {}: ".format(i+1)))
    list.append(element)
#When the loop stops, the list is showed with the new elements.
print("The list has been uptdated!")
for element in list:
    print(element)
#Now we create a tuple with only 7 elements and a message to present the tuple.
tuple = (15, 30, 45, 60, 75, 90, 105)
#While the index is lower than the elements that have been read of tuple it won't end.
index = 0
while index < len(tuple):
#Now print the elements 
    print(tuple[index])
    index + = 1
