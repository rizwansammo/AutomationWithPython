# sort_names.py

# Step 1: Read the content of the file
with open('names.txt', 'r') as file:
    names = file.readlines()

# Step 2: Remove any leading/trailing whitespace characters (like newline)
names = [name.strip() for name in names]

# Step 3: Sort the names alphabetically
names.sort()

# Step 4: Write the sorted names to a new file
with open('sorted_names.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')

print("Names have been sorted and saved to 'sorted_names.txt'")
