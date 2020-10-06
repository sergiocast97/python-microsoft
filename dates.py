# Date and Time

# Import the date / time library
from datetime import datetime, timedelta

# Get the current date/time object
today = datetime.now()

# Convert it to string in order to print
print('Today is: ' + str(today))

# Timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# Print specific parts of a date
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

# Formats can be used for actual outputs
date_output = f'Date: {today.day}/{today.month}/{today.year}'
hour_output = f'Hour: {today.hour}:{today.minute}'
print(date_output)
print(hour_output)

# Taking date strings
birth_day = input('When were you born? (dd/mm/yyyy): ')
birth_date = datetime.strptime(birth_day, '%d/%m/%Y')
print('Date of Birth: ' + str(birth_date))

birth_eve = birth_date - one_day
print('Birth Eve: ' + str(birth_eve))