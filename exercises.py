import math
list = [2, 4, 6, 8, 10]
print("Available list", list)
element = int(input("How many elements you will add to the list? "))
for i in range(element):
    element = int(input("Enter the element that you want to add {}: ".format(i+1)))
    list.append(element)
print("The list has been uptdated!")
for element in list:
    print(element)
