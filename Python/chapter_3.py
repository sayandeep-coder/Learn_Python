# 🐍 Python Basics Practice: Dictionaries and Sets
# -------------------------------------------------
# Author: Sayandeep Purkait
# Description: Practice problems on Python dictionaries and sets.

# ------------------------------------------------
# 🧠 Question 1:
# Create a dictionary with English to another language translation.
# Ask the user for an English word and print its meaning.
# ------------------------------------------------
print("🧩 Q1: English to Local Language Dictionary")

d = {
    "hello": "namaste",
    "good": "valo"
}
print("Available words:", list(d.keys()))

user = input("Enter your English word: ")
print("Meaning:", d[user])
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 2:
# Create an empty set and demonstrate adding elements.
# Note: Sets do not allow duplicate values.
# ------------------------------------------------
print("🧩 Q2: Working with Sets")

s = set()
s1 = (1, 2, 4, 2)
s2 = (1, 4, 6)

# Add elements from tuples
s.update(s1)
s.update(s2)

print("Combined set elements (no duplicates):", s)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 3:
# Create a dictionary of 3 users, where each user's name is the key
# and their favorite movie is the value. Use user input to populate it.
# ------------------------------------------------
print("🧩 Q3: Favorite Movies Dictionary")

fav_movies = {}
for i in range(0, 3):
    name = input("Enter your name: ")
    movie = input("Enter your favourite movie: ")
    fav_movies.update({name: movie})

print("Favourite Movies Dictionary:", fav_movies)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 4:
# Demonstrate unique behavior of sets by adding duplicate elements.
# ------------------------------------------------
print("🧩 Q4: Demonstrating Unique Property of Sets")

unique_set = {1, 2, 2, 3, 4, 4, 5}
print("Original set with duplicates removed:", unique_set)
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 5:
# Perform basic set operations: union, intersection, and difference.
# ------------------------------------------------
print("🧩 Q5: Basic Set Operations")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 6:
# Demonstrate dictionary methods: keys(), values(), and items().
# ------------------------------------------------
print("🧩 Q6: Dictionary Methods Example")

student = {
    "name": "Sayan",
    "age": 20,
    "course": "AI & ML"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Key-Value Pairs:", student.items())
print("-" * 50)


# ------------------------------------------------
# 🧠 Question 7:
# Update a dictionary with new key-value pairs using update() method.
# ------------------------------------------------
print("🧩 Q7: Update a Dictionary")

student.update({"college": "Haldia Institute of Technology"})
print("Updated Dictionary:", student)
print("-" * 50)
