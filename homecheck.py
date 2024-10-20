file_name = &quot;automated_file.txt&quot;
text = &quot;Hello! This is an automated file with text.&quot;
with open(file_name, 'w') as file:
    file.write(text)
print(f&quot;File '{file_name}' has been created and the message has been written.&quot;)
