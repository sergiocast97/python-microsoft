people = ['Sergio', 'Cristiana', 'Arianna']

# For loop
print('Names: ')
for name in people :
    print(' - ' + name)

# For in Loop
print('\nNames in range: ')
for i in range(0, 2):
    print( '-' + people[i])

# While loop

print('\nNames: ')

# Declare the index, then run the loop
index = 0
while index < len(people) :
    print('- ' + people[index])
    index = index + 1