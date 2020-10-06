# Multiple Condition

# Taking the country input
country = input('What is your country? ')

if country.lower() == 'canada':

    # Check the province
    province = input('What province do you live in? ')

    # With the in operator, you can check certain items existing in a list
    if province in('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
    # With the or operator, you can check different conditions for the same result
    elif province == 'Ontario' or province == 'Nova Scotia' :
        tax = 0.13
    else:
        tax = 0.15

# For non-canadians, tax is 0
else:
    tax = 0;

print(tax)


# Simple Conditional

# Take GPA and Lowest Grade
gpa = float(input('What is your gpa? '))
lowest_grade = float(input('What is your lowest grade? '))

# AND operator
if gpa >= .85 and lowest_grade >= .70 :
    honour_roll = True
else :
    honour_roll = False

# If the honour roll is true
if honour_roll:
    print('Well done')