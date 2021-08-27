# Library to make REST API calls
import requests
# Library to read JSON
import json

# Key to the API
SUBSCRIPTION_KEY = "xxxxxx"
# Service
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"
# Name of the function
address = vision_service_address + "analyze"

# Parameters for the call
parameters = { 'visualFeatures': 'Description,Color', 'language':'en' }

# Open the image
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# Specify suscription key
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
}

# Make a request
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Exception for errors
response.raise_for_status()

# Display response
results = response.json()
print(json.dumps(results))

# Print items from the JSON

print('requestId')
print (results['requestId'])

print('dominantColorBackground')
print(results['color']['dominantColorBackground'])

print('first_tag')
print(results['description']['tags'][0])

for item in results['description']['tags']:
    print(item)

print('caption text')
print(results['description']['captions'][0]['text'])


# Dictionaries

person_dict = { 'first': 'Christopher', 'last':'Harrison'}

# Create Staff Dict
staff_dict = {}
staff_dict['Program Manager'] = person_dict

# Convert to JSON
staff_json = json.dumps(staff_dict)

# Print the Object
print(staff_json)