
# Exercise #1 
# Filter out all of the empty strings from the list below
# places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]



string_list = [" ", "Argentina", " ", "San Diego", " ", " ", " ", "Boston", "New York"] 



while("" in string_list) :
    string_list.remove("")

# Printing modified list 
print ("Modified list is : " + str(string_list))







# ### Exercise 2 
# <p>Write an anonymous function that sorts this list by the last name

# `Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']`
# author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def sort_name(nameList):


    nameList.sort(key=lambda x: x.split()[-1])


    return nameList



nameList = ["Joel Carter", "Victor aNisimov", 
            "Andrew P. Garfield","David hassELHOFF",
            "Gary A.J. Bernstein"]


print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sort_name(nameList))







# Exercise 3 
#Convert the list below from Celsius to Farhenheit, using the map function with a lambda

# [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]


Celsius = [32, 12, 44, 29]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print(Fahrenheit)





# Exercise 4 
# Write a recursion function to perform the fibonacci sequence up to the number passed in

def fibonacci(n):  
    if n <= 1:  
        return n  
    else:  
        return(fibonacci(n-1) + fibonacci(n-2))  
# program will take input from the user  
num = int(input("How many terms? "))  
# program will check if the number of terms is valid  
if num <= 0:  
    print("must enter positive number")  
else:  
    print("Fibonacci sequence:")  
    for i in range(num):  
        print(fibonacci(i))