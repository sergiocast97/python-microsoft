name = input('What is your name?\n')
surname = input('What is your surname?\n')

# String Operations

full_name = name + ' ' + surname

# Uppercase string
print( full_name.upper() )

# Lowercase string
print( full_name.lower() )

# First letter of string becomes uppercase
print( full_name.capitalize() )

# Count the occurrences of a character or string
print( full_name.count('o') )


# String Formatting

# Simple Format
print( 'Hello {} {}'.format( name, surname ) )

# Indexed Format
print( 'Hello {1} {0} {1}'.format( name, surname) )

# Even more simplified Format  
print( f'Hello {name} {surname}' )