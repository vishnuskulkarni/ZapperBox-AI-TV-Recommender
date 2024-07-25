import json

# Load the JSON data from the file
with open('guide_listings', 'r') as f:
    data = json.load(f)

# Print the keys at the top level of the JSON data
print("Top-level keys:", data.keys())

# Access the 'channels' key
channels = data['channels']

# Print the number of channels
print("Number of channels:", len(channels))

# Print the keys of the first channel
if channels:
    print("Keys of the first channel:", channels[0].keys())

# Print the first program in the first channel
if channels and 'programs' in channels[0]:
    first_program = channels[0]['programs'][0]
    print("First program in the first channel:", first_program)

# Print the name of the first program
if 'name' in first_program:
    print("Name of the first program:", first_program['name'])
