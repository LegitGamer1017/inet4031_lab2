# Open the file
with open('fileprocessor.input', 'r') as file:
	# Read each line into a list
	lines = file.readlines()

# Process each line
print("Printing out User Data:")
for line in lines:
	# Skip lines starting with '#'
	if line.startswith('#'):
		user = line.strip().split(':')[0]  # Extract the user name from the skipped line
		print(f"{user} is skipped because it starts with a hashtag (is commented out)")
		continue  # Skip to the next iteration if the line starts with '#'

	# Split each non-commented line into a list using ':' as delimiter
	data = line.strip().split(':')
	# Print the user data
	print(f"The user {data[0]} has a password of {data[1]} and has userid {data[2]} and groupid {data[3]}")

print("End of User Data")
