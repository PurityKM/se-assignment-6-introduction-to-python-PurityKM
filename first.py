# print is a built-in function in Python used to output text to the console.

# Parentheses() are used to enclose the arguments passed to the function. In this case, the argument is "Hello, World!"

# "Hello, World!" is a string literal. In Python, strings are enclosed in either single quotes (') or double quotes (").

print("Hello, World!")

# Integers (int): Whole numbers, positive or negative, without decimals.
age = 23

# Floating-Point Numbers (float): Numbers with a decimal point. 
r = 3.14

# Strings (str): Sequence of characters enclosed in single or double quotes. 
greetings = "Hey"

# Lists (list): Ordered, mutable collection of items, enclosed in square brackets.
animals = ["Dog", "Cat", "Lion"]

# Tuples (tuple): Ordered, immutable collection of items, enclosed in parentheses.
fruits = ("Apple", "Orange", "Apple")

#Dictionaries (dict): Unordered, mutable collection of key-value pairs, enclosed in curly braces.
students_details = {"name": "Ann", "age": 23}

#Sets (set): Unordered collection of unique items, enclosed in curly braces.
prices = (4, 6, 9, 3)

# Booleans (bool): Logical values representing True or False.
isTasty = True

# Conditional statements in Python are used to execute a block of code based on whether a condition is true or false. 

# if Statement: Executes a block of code if the condition is true.
# elif Statement: (short for "else if") Checks another condition if the previous if or elif condition was false.
# else Statement: Executes a block of code if none of the preceding conditions were true.

age = 18

if age < 18:
    print("You are not eligible to be a voter.")
elif age == 18:
    print("You are eligible to be a voter.")
else:
    print("You are an adult.")

# Loops in Python are used to execute a block of code repeatedly, either for a specified number of times or until a condition is met.

# for Loop: Iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence.
fruits = ["Orange", "Pineapple", "Lemon"]

for fruit in fruits:
    print(fruit)
    
# while Loop: Repeats a block of code as long as a condition is true.
num = 0

while num < 5:
    print("Count is:", num)
    num += 1
