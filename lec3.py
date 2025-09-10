# creating a tuple of Indian names
names = ("liju", "narayan", "raj")

print("Tuple of names:", names)

# accessing an element
print("\nFirst name:", names[0])
print("Last name:", names[-1])

# tuple methods
print("\nCount of liju:", names.count("liju"))
print("Index of 'narayan':", names.index("narayan"))

# traversing through tuple
print("\nTraversing names:")
for name in names:
    print(name)

# checking membership
print("\nIs 'priya' in tuple?", "priya" in names)
print("Is 'kiran' in tuple?", "kiran" in names)

# tuple concatenation
more_names = ("liju", "raj")
combined = names + more_names
print("\nConcatenated tuple:", combined)

# tuple repetition 
repeated = names * 2
print("Repeated tuple:", repeated)

# length of tuple
print("\nLength of names tuple:", len(names))

# converting tuple to list
names_list = list(names)
print("Converted to list:", names_list)

# converting back to tuple
names_tuple = tuple(names_list)
print("Converted back to tuple:", names_tuple)


# dictionary of courses and number of students enrolled
courses = {
    "python": 120,
    "css": 95,
    "java": 80,
    "data science": 150,
    "machine learning": 133,
}

print("\nOriginal dictionary:")
print(courses)

# 1. Accessing value using get()
print("\nAccessing values using get():")
print("Students in Python:", courses.get("python"))
print("Students in CSS:", courses.get("css"))
print("Students in Java:", courses.get("java"))

# If key doesn't exist, get() returns default value
print("Students in C++ (not present):", courses.get("c++", "Not available"))

# adding a new course
courses["cyber security"] = 90
print("\nAfter adding cyber security:")
print(courses)

# updating students in an existing course
courses.update({"python": 125})
print("\nAfter updating Python students:")
print(courses)

# removing a course safely using pop()
removed = courses.pop("css")   # instead of "C++"
print(f"\nRemoved CSS with {removed} students")
print(courses)

# removing last inserted item using popitem()
last_item = courses.popitem()
print(f"\nRemoved last inserted item: {last_item}")
print(courses)

# displaying all keys, values, and items
print("\nCourses keys:", courses.keys())
print("Courses values:", courses.values())
print("Courses items:", courses.items())
#checking if a coure exist
if "java" in courses:
    print("\njava courese is available")

#copying dictionary
copy_dict = courses.copy()
print("\ncopied dictionary:", copy_dict)

#clearing dictionary
courses.clear()
print("\ndictionary after  clearing :",courses)