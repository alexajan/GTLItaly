# FUNCTIONS

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Arguments

def greet_custom_user(username):
    """Display a custom greeting."""
    print("Hello, " + username.title() + "!")

greet_custom_user('alexa')


def describe_pet(pet_name, animal_type='zebra'):
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='henry')
describe_pet('carl', 'giraffe')
describe_pet('giraffe', 'carl')
describe_pet(animal_type='giraffe', pet_name='carl')

# Return values

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

politician_1 = get_formatted_name('michelle', 'bachelet')
politician_2 = get_formatted_name('pEdro', 'kucZynsKi', 'paBlo')
print(politician_1)
print(politician_2)

# Passing an arbitrary number of arguments

def make_sandwiches(size, *condiments):
    """Print the list of condiments that have been requested."""
    print("\nMaking a " + str(size) + "-inch sandwich with the following condiments:")
    for condiment in condiments:
        print("- "  + condiment)

make_sandwiches(16, 'salami', 'lettuce', 'cheese')
