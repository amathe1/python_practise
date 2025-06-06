names = ['ram', 'RAM', 'PANKAJ', 'PaNkAj']

unique_names = []
seen = []

for name in names:
    lower_name = name.lower()
    if lower_name not in seen:
        seen.append(lower_name)
        unique_names.append(name)  # Keep the original version if needed

# Print the count of unique names
print("Count:", len(seen))

# Print the unique names (case-insensitive)
print("Unique names (case-insensitive):", seen)
