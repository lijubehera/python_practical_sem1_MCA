import matplotlib.pyplot as plt

# sample data
x = [1, 2, 3, 4, 5]
y = [9, 8, 7, 4, 5]
y2 = [1, 5, 89, 52, 45]  # fixed length

# 1. line plot
plt.figure(1)
plt.plot(x, y, label="y=2x", color="blue", marker='o')
plt.plot(x, y2, label="y=x^2", color="red", linestyle='--')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line plot example")
plt.legend()

# 2. bar chart
plt.figure(2)
student = ["Aparna", "Monica", "Rohit", "Sagar"]
marks = [85, 72, 90, 60]
plt.bar(student, marks, color='green')
plt.xlabel("Students")
plt.title("Bar chart example")

# 3. scatter plot
plt.figure(3)
plt.scatter(x, y2, color='purple')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter plot example")

# show all plots
plt.show()
