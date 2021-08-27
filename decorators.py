# Defining the decorator
def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done logging')
    return wrapper

# Set up the Decorator call
@logger
def sample():
    print('--Inside sample function')

# Use the decorator
sample()