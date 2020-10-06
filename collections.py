#  Create and populate a dictionary
sergio = { }
sergio['first'] = 'Sergio'
sergio['last'] = 'Castillo'

#  Create and populate another dictionary
cristiana = { }
cristiana['first'] = 'Cristiana'
cristiana['last'] = 'Constantin'

# Create and populate a list
people = []
people.append(sergio)
people.append(cristiana)
people.append({
    'first' : 'Arianna',
    'last' : 'Castillo'
})

print(people)

# Loop through the list
for person in people :
    print('Person name: ' + person['first'])