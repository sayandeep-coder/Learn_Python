# 🐍 Python Basics Practice Questions with Answers
# ------------------------------------------------
# Author: Sayandeep Purkait
# Description: Beginner-friendly Python practice problems covering
# input/output, strings, and basic operations.

import sys

# ------------------------------------------------
# 🧠 Question 1:
# Write a Python program to print your Python version.
# ------------------------------------------------
print("🧩 Q1: Print Python Version")
print(sys.version)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 2:
# Write a Python program that asks for your name and prints a greeting message.
# ------------------------------------------------
print("🧩 Q2: Greeting the User")
name = input("Enter your name: ")
print(f"Good afternoon {name}")
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 3:
# Replace placeholders in a letter template with actual values using replace() method.
# ------------------------------------------------
print("🧩 Q3: Letter Template with Replace Method")
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
replaced_letter = letter.replace("<|Name|>", "Sayan")
new_letter = replaced_letter.replace("<|Date|>", "03/10/25")
print(new_letter)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 4:
# Count the number of double spaces ("  ") in a string.
# ------------------------------------------------
print("🧩 Q4: Count Double Spaces in a String")
text = "hello   sayan deep"
double_spaces = text.count("  ")
print(f"Number of double spaces: {double_spaces}")
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 5:
# Print a formatted letter using escape characters like \n for a new line.
# ------------------------------------------------
print("🧩 Q5: Escape Sequences Example")
letter2 = "Dear Harry\nthis python course is nice\nThanks!"
print(letter2)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 6:
# Find and replace double spaces with single spaces in a given string.
# ------------------------------------------------
print("🧩 Q6: Replace Double Spaces with Single Spaces")
sample_text = "Python  is  very  powerful"
cleaned_text = sample_text.replace("  ", " ")
print("Before:", sample_text)
print("After :", cleaned_text)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 7:
# Take user's age as input and print if they are eligible to vote (age >= 18).
# ------------------------------------------------
print("🧩 Q7: Voting Eligibility Check")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote ✅")
else:
    print("Sorry, you are not eligible to vote ❌")
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 8:
# Create a string and demonstrate different string slicing examples.
# ------------------------------------------------
print("🧩 Q8: String Slicing Examples")
my_str = "PythonProgramming"
print("Original String:", my_str)
print("First 6 letters:", my_str[:6])
print("Last 6 letters:", my_str[-6:])
print("Middle part:", my_str[6:13])
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 9:
# Show how to use len(), upper(), lower(), and title() methods on a string.
# ------------------------------------------------
print("🧩 Q9: Common String Methods")
str_ex = "hello python"
print("Original:", str_ex)
print("Length :", len(str_ex))
print("Uppercase:", str_ex.upper())
print("Lowercase:", str_ex.lower())
print("Title Case:", str_ex.title())
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 10:
# Create a variable of each data type and print their types.
# ------------------------------------------------
print("🧩 Q10: Data Types and Variables")
integer_var = 10
float_var = 12.5
string_var = "Python"
bool_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
set_var = {7, 8, 9}
dict_var = {"name": "Sayan", "age": 20}

print("Integer:", type(integer_var))
print("Float:", type(float_var))
print("String:", type(string_var))
print("Boolean:", type(bool_var))
print("List:", type(list_var))
print("Tuple:", type(tuple_var))
print("Set:", type(set_var))
print("Dictionary:", type(dict_var))
print("-" * 50)
