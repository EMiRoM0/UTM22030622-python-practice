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
#We print the default data
print("Civilian data:")
print("Name: Samuel" )
print("Nationality: Boliviano")
print("Age: 18")
#Now we introduce the new data
name = input("Enter the new name: ")
nationality = input("Enter the new nationality: ")
age = int(input("Enter the new age: "))
#Now the code will show the new data that has been entered
print("Final data:")
print("Name:", name)
print("Nationality:", nationality)
print("Age:", age)
#Now, thanks to the import math we can do this exercise.
#This exercise allows us to perform operations such as adding, subtracting, dividing and multiplying.
#First we define our function to do the operations.
def operation(operating, frstnum, secnum):
#Now with if cycles let's make the selection of operations to perform.
if operating == "+":
result = frstnum+secnum
elif operating == "-":
result = frstnum-secnum
elif operating == "*":
reuslt = frstnum*secnum
elif operating == "/":
#Here we try to verify that the divisor is not zero to avoid errors.
if secnum !=0:
result = frstnum/secnum
#If you put a zero in frstnum or secnum this will happen
else:
print("You can't divide with a zero!")
return None
else:
print("Error, operating invalid")
return None
#Now we print the result in this specific scenario
return result
#Now we begin to insert the indicated actions to perform the operations.
while True:
operating = input("Insert the operation (+,-,/,*)")
frstnum = int(input("Insert your first number"))
secnum = int(input("Insert your second number"))
#After entering the necesary data it will show the final result.
result = operation(operating, frstnum, secnum)
if result is not None:
print("The result is:", result)
#Then an option to repeat the exercise of the operation or cancel the repetition.
continue = input("Do you want to do another operation? y/n")
if continue.lower() !="y":
break
#End of the code.
