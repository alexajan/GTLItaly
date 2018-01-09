# IF STATEMENTS

age = 16
name = "John"
if age == 16 and name.lower() == "john":
    print(name.title() + " is " + str(age))

if age == 16 or name.lower() == "steven":
    print(name.title() + " is " + str(age))

if "h" in name:
    print("h is in the name!")

appliances = ['magic_toaster', 'rainbow_oven', 'unicorn_fridge']
for appliance in appliances:
    if appliance == "magic_toaster":
        print(appliance.upper())
    elif appliance != "rainbow_oven":
        print(appliance.title())
    else:
        print(appliance)

# DICTIONARIES

# Creating them
my_car = {'color': 'turquoise', 'brand': 'bmw'}
print(my_car['color'])

my_car['year'] = 2017
my_car['color'] = 'gold'
print(my_car)
del my_car['year']
print(my_car)

# Looping through the key-value pairs
car_dealership = {'rolls-royce': 2012, 'honda': 2002, 'mercedes': 2017}
car_database = []
for key, value in car_dealership.items():
    car_database.append(key + ": " + str(value))

print(car_database)

# USER INPUT AND WHILE LOOPS

# User input
height = input("How tall are you in inches? ")
if int(height) >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# Modulo
user_num = input("Enter a number, and I'll tell you if it's even or odd: ")
if int(user_num) % 2 == 0:
    print("\nThe number " + str(user_num) + " is even.")
else:
    print("\nThe number " + str(user_num) + " is odd.")

# While loops
index = 1
while index <= 5:
    print(index)
    index += 1

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("Added " + city.title() + " to your travel log!")
