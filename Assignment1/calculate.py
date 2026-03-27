#1

n=10
r=5
p=100

A = p * ((1 + r / 100))**n

print(A)

#2

A=10
B=20
str = "There are {} students in the class, with {} who play at least one sport."

print(str.format(B,A))

#3

#Sample output = It goes without saying, “Time is Money”, and none can deny it


print('It goes without saying, "Time is Money", and none can deny it.')

#Ans None of these

#4

x = lambda a,b: a//b
print(x(10,3))


#Ans = 3

#Q5. What will be the output of the following code?

A = 10
B = 12

print("Smaller") if A == B else print("Greater") if A < B else print("True")

#Ans Greater

#Q6. What will be the output of the following code?

import os
import numpy as np
my_list1 = [2,7,3,5,4,6]
print(my_list1)
arr_1 = np.array(my_list1, dtype=int)
print(arr_1)

#Ans = [2,7,3,5,4,6]
#Ans = [2 7 3 5 4 6]

#Q7. Create a string called ‘string’ with the value as “Machine Learning”. Which code(s) is/are appropriate to slice the substring 'Learn' “Learn”?

string = "Machine Learning"

#print(string[slice(13,8,1)])
#print(string[slice(1,8,1)])
#print(string[8:14])
print(string[slice(8,13,1)])

#Ans = print(string[slice(8,13,1)])

#Q8 Create a sequence of numbers from 10 to 25 and increment by 4. What is the index of the value 18?
sequence = list(range(10, 26, 4))
print(sequence)
print("Index of 18 is: ", sequence.index(18))


 #Q9. Which of the following is true with respect to the below codes?
 # 
num1 = 5**4
num2 = pow(5,4)
print(num1, num2)   

#Ans a) num1=num2

#Q10.A Python NameError exception is raised when: -

#a. Trying to access a variable which has not been defined
#d. Accessing the function from a module that has not been imported
 #Both a and d will raise a NameError exception.

#Q11.What type of exception will be raised for the code given below?

x = "string"
#int(x)
#Ans ValueError: invalid literal for int() with base 10: 'string'

#Q12.FileNotFoundError exception is raised by operating system errors when: -

#b. A file or directory is requested but does not exist in the working directory


#Q13.Consider a variable Z. The value of Z is "ID-5632". Data type of Z is: 

z = "ID-5632"
print(type(z))

#Ans str data type 

#Q14.Which of the following variable(s) are character data type?
K= "4"
J= "Welcome"
C = "?"
print(type(J))
print(type(K))
print(type(C))  
#Ans d) all of them

#Q15.Choose the symbol/s that does not have the ability to convert any values to string?

    #a. ( )
    #b. “ ”
    #c. {}
    #d. #
#Ans d) # does not have the ability to convert any values to string

#Q16 Create a dictionary ‘Country’ that maps the following countries to their capitals
country = {"India": "Delhi", "China": "Beijing", "Japan": "Tokyo", "Qatar": "Doha", "France": "Marseilles"}
country["France"] = "Paris"

print(country)

country = {"India": "Delhi", "China": "Beijing", "Japan": "Tokyo", "Qatar": "Doha", "France": "Marseilles"}
country.update({"France": "Paris"})

print(country)

#Q17. Create the tuples given below
#tuple_1 = (1,5,6,7,8)
#tuple_2 = (8,9,4)
#Identify which of the following code does not work on a tuple.

tuple_1 = (1,5,6,7,8)
tuple_2 = (8,9,4)

print(sum(tuple_1))

print(len(tuple_2))

tuple_2 + tuple_1

#tuple_1[3] = 45

#Ans tuple_1[3] = 45 does not work on a tuple as tuples are immutable and cannot be modified after creation.

#18 How many elements in the following data structure?

S = {1,2,3,4,4,4,5,6}

print(len(S))

#Ans . 6

#19Write a function which finds all pythagorean triplets of triangles whose sides are not more than a natural number N

def pythagorean_triangle(N):
    triangle = []
    for a in range(1, N+1):
        for b in range(a, N+1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= N:
                triangle.append((a, b, int(c)))
    return triangle


print(pythagorean_triangle(20))










