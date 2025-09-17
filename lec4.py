# #normal function to get full name of  a student
# def full_name(first_name, last_name):
#     return first_name + " " + last_name

# #lambda function to calculate percentage

# percentage = lambda obtained,total : (obtained / total)*100
# #student data 
# students = [
#     {"first":"amit","last":"sharma","marks":450,"total":500},
    
#     {"first":"riya","last":"patil","marks":380,"total":500},
#     {"first":"siddhi","last":"mukadam","marks":420,"total":500}

# ]
# #using function
# for s in students:
#     name = full_name(s["first"],s["last"])
#     perc = percentage(s["marks"],s["total"])
#     print(f"student:{name} | percentage:{perc :.2f}%")


# 1. Single inheritance
class Stationery:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Stationery: {self.name}, Price: {self.price}")


class Pen(Stationery):  # single inheritance
    def __init__(self, name, price, ink_color):
        super().__init__(name, price)
        self.ink_color = ink_color

    def display_info(self):
        super().display_info()
        print(f"Ink Color: {self.ink_color}")


# 2. Multiple inheritance
class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

    def show_brand(self):
        print(f"Brand: {self.brand_name}")


class Marker(Stationery, Brand):  # multiple inheritance
    def __init__(self, name, price, tip_size, brand_name):
        Stationery.__init__(self, name, price)
        Brand.__init__(self, brand_name)
        self.tip_size = tip_size

    def display_info(self):
        super().display_info()
        print(f"Tip Size: {self.tip_size}")
        self.show_brand()


# 3. Multilevel inheritance
class WritingInstrument(Stationery):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type


class Pencil(WritingInstrument):  # multilevel (Stationery → WritingInstrument → Pencil)
    def __init__(self, name, price, hardness):
        super().__init__(name, price, "Pencil")
        self.hardness = hardness

    def display_info(self):
        super().display_info()
        print(f"Type: {self.type}, Hardness: {self.hardness}")


# 4. Hierarchical inheritance
class Eraser(Stationery):  # child1
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

    def display_info(self):
        super().display_info()
        print(f"Material: {self.material}")


class Sharpener(Stationery):  # child2
    def __init__(self, name, price, blade_type):
        super().__init__(name, price)
        self.blade_type = blade_type

    def display_info(self):
        super().display_info()
        print(f"Blade Type: {self.blade_type}")


# 5. Hybrid inheritance (multiple + multilevel)
class Highlighter(Marker, WritingInstrument):  
    def __init__(self, name, price, ink_color, brand_name):
        Marker.__init__(self, name, price, "Medium", brand_name)
        WritingInstrument.__init__(self, name, price, "Highlighter")
        self.ink_color = ink_color

    def display_info(self):
        super().display_info()
        print(f"Ink Color: {self.ink_color}, Type: {self.type}")


# ------------------ Testing ------------------
print("---- Single Inheritance ----")
p = Pen("Ball Pen", 10, "Blue")
p.display_info()

print("\n---- Multiple Inheritance ----")
m = Marker("Whiteboard Marker", 30, 2, "Camlin")
m.display_info()

print("\n---- Multilevel Inheritance ----")
pc = Pencil("Apsara Pencil", 5, "HB")
pc.display_info()

print("\n---- Hierarchical Inheritance ----")
e = Eraser("Natraj Eraser", 3, "Rubber")
e.display_info()

s = Sharpener("Demos Sharpener", 7, "Steel Blade")
s.display_info()

print("\n---- Hybrid Inheritance ----")
h = Highlighter("Faber-Castell Highlighter", 40, "Yellow", "Faber-Castell")
h.display_info()
