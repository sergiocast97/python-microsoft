# Defining a function

def get_initial(name):
    # Getting 1 character from position 0
    initial = name[0:1].upper()
    return initial

# Defaulting force uppercase 
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# Calling the function

name = input('Enter your name: ')
name_initial = get_initial(name)

surname = input('Enter your surname: ')
surname_initial = get_initial(surname)

print('Your initials are ' + name_initial + surname_initial)

# Specifying parameters
test_name = 'Test'
initial = get_initial(
    force_uppercase=True,
    name=test_name
)

# Date function

from datetime import datetime

# Function to print current date and time
def print_time() :
    print('Task completed')
    print(datetime.now())
    print()

# Print timestamps to see how long code takes to run

first_name = 'Susan'
print_time()

for x in range(0,10):
    print(x)

print_time()