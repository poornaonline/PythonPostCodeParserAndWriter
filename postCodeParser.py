import json

input_file = open ('postcodes.json')
json_array = json.load(input_file)
postcode_list = []

for item in json_array:
    postcode_details = {"id": None, "postcode": None, "suburb": None, "state": None, "latitude": None, "longitude": None}
    postcode_details['id'] = item['id']
    postcode_details['postcode'] = item['postcode']
    postcode_details['suburb'] = item['suburb']
    postcode_details['state'] = item['state']
    postcode_details['latitude'] = item['latitude']
    postcode_details['longitude'] = item['longitude']
    postcode_list.append(postcode_details)

print_json = json.dumps(postcode_list, sort_keys=False, indent=4)
print(print_json)

with open('parsed_json.json', 'w') as json_file:
    json.dump(postcode_list, json_file)
