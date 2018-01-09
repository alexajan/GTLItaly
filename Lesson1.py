# VARIABLES AND DATA TYPES

# Print "Hello, World!"

print("Hello, world!")
message = "Hello, world!"
print(message)
message = "Hola, mundo!"
print(message)

# Understanding errors

# Error: print mesage

# Strings

print("It's a string")
print('This is also a string')

first_name = 'alexa'
last_name = 'jan'
print(len(last_name))
first_name = first_name.upper()
first_name = first_name.title()
first_name = first_name.lower()
print("Hello " + first_name + " " + last_name)

msg = "bienvenidos"
print(msg[::2])

# Numbers

print(3 + 3 / 2 - 1 * 0)
print(3 ** 2)

# LISTS

# Accessing elements

menu = ["pizza", "spaghetti", "burger"]
print(menu[1].title())
print(menu)

# Adding items

menu.append("salad")
menu.insert(0, "soup")
print(menu)

# Deleting items
del menu[1]
menu.remove("soup")
popped = menu.pop()
print(menu)
print(popped)

# Sorting items
menu.sort(reverse=False)
print(menu)
# Error: print(menu[10])

# Working with lists
appliances = ["magic toaster", "rainbow oven", "unicorn fridge"]
for appliance in appliances:
    print("I am a " + appliance)

num_list = []
for index in range(1, 5):
    num_list.append(index)
    print(num_list)
print(sum(num_list))
print(max(num_list))

# Tuples
tuple_ex = (999, 1000)
# Error: tuple_ex[0] = 0
for num in tuple_ex:
    print("My favorite number is " + str(num))
