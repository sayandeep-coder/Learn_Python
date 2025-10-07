# 🐍 Python Basics Practice: Lists and Tuples
# --------------------------------------------
# Author: Sayandeep Purkait
# Description: Beginner-level exercises on list creation, sorting, summing, and tuple operations.

# ------------------------------------------------
# 🧠 Question 1:
# Write a Python program to store fruit names entered by the user into a list.
# ------------------------------------------------
print("🧩 Q1: Create a List of Fruits from User Input")

fruits = []
fruit_1 = input("Enter the first fruit name: ")
fruits.append(fruit_1)
fruit_2 = input("Enter the second fruit name: ")
fruits.append(fruit_2)
fruit_3 = input("Enter the third fruit name: ")
fruits.append(fruit_3)

print("Your fruit list:", fruits)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 2:
# Write a Python program to accept marks from the user and display them in sorted order.
# ------------------------------------------------
print("🧩 Q2: Sort Student Marks")

marks = []
marks_1 = int(input("Enter the first mark: "))
marks.append(marks_1)
marks_2 = int(input("Enter the second mark: "))
marks.append(marks_2)
marks_3 = int(input("Enter the third mark: "))
marks.append(marks_3)

marks.sort()
print("Marks in ascending order:", marks)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 3:
# Find the sum of numbers in a list using a for loop.
# ------------------------------------------------
print("🧩 Q3: Sum of List Elements Using a Loop")

numbers = [10, 20, 30, 40]
sum_val = 0
for i in numbers:
    sum_val += i

print("Sum of list elements:", sum_val)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 4:
# Find the sum of numbers in a list using the built-in sum() function.
# ------------------------------------------------
print("🧩 Q4: Sum of List Elements Using sum() Function")

numbers = [10, 20, 30, 40]
total = sum(numbers)
print("Total sum using sum():", total)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 5:
# Count the number of zeros in a tuple using the count() method.
# ------------------------------------------------
print("🧩 Q5: Count Zeros in a Tuple")

a = (7, 0, 8, 0, 0, 9)
zero_count = a.count(0)
print("Number of zeros in the tuple:", zero_count)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 6:
# Demonstrate changing elements in a list vs immutability of tuples.
# ------------------------------------------------
print("🧩 Q6: List vs Tuple Mutability")

# Lists are mutable
my_list = [1, 2, 3]
print("Original list:", my_list)
my_list[1] = 99
print("After modification:", my_list)

# Tuples are immutable
my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)
print("Tuples cannot be changed after creation")
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 7:
# Create a list of numbers and print the maximum and minimum using max() and min().
# ------------------------------------------------
print("🧩 Q7: Find Maximum and Minimum in a List")

numbers = [5, 12, 45, 2, 89, 33]
print("Numbers:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("-" * 50)
