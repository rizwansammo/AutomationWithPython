# Define the file name
file_name = &quot;automated_file.txt&quot;

# Define the text to write
text = &quot;Hello! This is an automated file with text.&quot;

# Open the file in write mode (this will create the file if it doesn't exist)
with open(file_name, 'w') as file:
    file.write(text)

print(f&quot;File '{file_name}' has been created and the message has been written.&quot;)
