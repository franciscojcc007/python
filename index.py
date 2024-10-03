


# def palindrome(txt: str):
#   txt = txt.replace(" ", "").lower()
#   return txt == txt[::-1]

# txt_1 = "la al"
# txt_2 = "am lo es"

# print(palindrome(txt_1))
# print(palindrome(txt_2))



# n = int(input("dame un numero"))

# if n > 0:
#   print(n, "es positivo")
# elif n < 0:
#   print(n, "es negativo")
# else:
#   print("n is zero ")

# names = ["Mario","Jose","Rafael","Ana"]
# print(names[0])
# print()
# names.append("Frank")
# names.sort()
# print(names)
# print()
# names.pop(0)
# print(names)



# s =set()

# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# s.add(5)
# s.add(6)
# print(s)
# print()

# s.remove(3)
# print(s)
# print()
# print(f"tengo {len(s)} elemento en el set")



# house = {"playa":"este","villa":"norte"}
# house["campo"]= "estajero"
# print(house)


# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True


#     def open_seats(self):
#         return self.capacity - len(self.passengers)


# flight = Flight(2)

# people = ["Harry", "Ron", "Hermione", "Ginny"]


# for person in people:
#     if flight.add_passenger(person):
#         print(f"Added {person} to flight successfully")
#     else:
#         print(f"No available seats for {person}")
        



# def announce(f):
#     def wrapper():
#         print("About to run the function")
#         f()
#         print("Done with the function")
#     return wrapper

# @announce
# def hello():
#     print("Hello, world!")

# @announce
# def goodbye():
#     print("Goodbye, world!")

# hello()
# goodbye()

# import sys

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
# except ValueError:
#     print("Error: Invalid input")
#     sys.exit(1)

# try:
#     result = x / y
# except ZeroDivisionError:
#     print("Error: Cannot divide by 0.")
#     # Exit the program
#     sys.exit(1)

# print(f"{x} / {y} = {result}")

# people = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Cho", "house": "Ravenclaw"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

# people.sort(key=lambda person: person["name"])

# print(people)

# import sys

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
# except ValueError:
#     print("Error: Invalid input")
#     sys.exit(1)

# try:
#     result = x / y
# except ZeroDivisionError:
#     print("Error: Cannot divide by 0.")
#     # Exit the program
#     sys.exit(1)

# print(f"{x} / {y} = {result}")