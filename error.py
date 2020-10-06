# Declare numbers
x = int( input("First number: "))
y = int( input("Second number: "))


try:                                        # Try to perform the division
    print( x/y )
except ZeroDivisionError as e:              # If dividing by 0, throw and error
    print('Not allowed to divide by zero')
except:                                     # If any other type of issue, throw an error
    print('Something else went wrong')
finally:                                    # This area is always run
    print('This is our cleanup code')


# Type try, then tab to generate error handling code