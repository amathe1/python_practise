names = ['ram', 'RAM', 'PANKAJ', 'PaNkAj']

# Convert all names to lowercase and use a set to find unique names
unique_names = set(name.lower() for name in names)

# Print the count of unique names
print(len(unique_names))  # Output: 2
