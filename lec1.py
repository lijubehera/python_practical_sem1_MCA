# # check if a number is even or odd
# num = int(input("ENTER A NUMBER : "))
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd.")

# # find the largest among three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("The largest number is:", a)
# elif b >= a and b >= c:
#     print("The largest number is:", b)
# else:
#     print("The largest number is:", c)

#grade calculate based on marks 

# # Grade calculation based on marks
# marks = int(input("Enter your marks (0-100): "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# elif marks >= 35:
#     print("Grade: D")
# else:
#     print("Grade: Fail")
#operation on list

# create a list 
numbers = [4, 55, 6, 25]
print("original list:", numbers)

# access an element
print("first element:", numbers[0])
print("last element:", numbers[-1])

# insert an element
numbers.append(60)
print("after appending 60:", numbers)

# insert at specific position
numbers.insert(2, 52)
print("after inserting 52 at index 2:", numbers)

# delete an element (using existing one, e.g., 55)
numbers.remove(55)
print("after removing 55:", numbers)

# update an element
numbers[1] = 15
print("after updating second element to 15:", numbers)

# search for an element 
if 30 in numbers:
    print("30 is present in the list.")
else:
    print("30 is not in the list.")

# length of the list
print("length of the list:", len(numbers))
