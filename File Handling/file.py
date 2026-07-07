file = open("notes.txt", "a")
file.write("\nThankyou")
file.close()


file = open("C:\\Users\\LENOVO\\Desktop\\HOJA PYTHON PRACTICAL\\File Handling\\notes.txt", "a")
file.write("\nThankyou")
file.close()


file = open("notes.txt", "r") 
content = file.read()
print(content)


file = open("notes.txt", "r") 
for f in file:
    print(f.strip())
file.close()


file = open("notes.txt", "r") 
print(file.read(16))
file.close()


with open("notes.txt", "r") as file:
    content = file.read()
    print(content)