'''
Function - a reuseable block of code which perfomes a specific task and executed when it is called.

how to do?

def  # to define a function
fucntion name 
paranthesis... what's inside of it?  -something, that somethings is known as "parameter"
something can be used inside the block of code

calling the function, while calling, argument is the data we give for parameter

===============================================
def function (something):
    if something happens:
        do this

function (something)   # calling the function
===============================================
'''

def greet():
    print("Greetings Rover")

greet()

def greetings(name):
    print(f"Greetings {name}")

greetings ("Rover")


def greet_with(name, location):
    print (f"Hey {name}")
    print (f"What is it like to be in {location}")

greet_with("Rover", "Black Shores")    #  positional arguments

greet_with(location = "Black Shores", name = "Rover")    #  keyword arguments


'''==================================
painting wall, required cans of paint
==================================='''

# import math

# height = float (input ("Height of the wall is : "))
# width = float (input ("Width of the wall is : "))

# def need_cans(height, width):
#     area = height*width
#     required_paint = area/5     # since 1 can cover 5m^2 area
#     return math.ceil(required_paint)

# cans = need_cans(height, width)

# print (f"You required total of {cans} cans")


'''=================
prime number checker
=================='''

# num = int (input ("Number you want to check for prime : "))

# def prime (alpha):
#     if alpha <= 1:
#         return "not prime"
    
#     for n in range (2, alpha - 1):
#         if alpha % n == 0:
#             return "not prime"

#     return "prime"
        
# number = prime (num)

# print (f"The number you have provided is {number}")

'''================================
prime number checker but with lists
================================='''

number = list (range (1, 1001))
prime_numbers = []


def prime_catcher (num):
    for element in number:
        if element <= 1:
            element += 1
            return "not prime"
        
        elif element % num == 0:
            element += 1
            return "not prime"
        
        elif element % num != 0:
            prime_numbers.append(element)
            element += 1
            return "prime"
    
bot = prime_catcher (number)
