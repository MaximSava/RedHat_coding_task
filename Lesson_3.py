# 1, 2

try:
    a = 1 / 0
except ZeroDivisionError:
    print("Division by zero")

# 3
# Try finaly block is legal

# 4  This Except handles all exception

# 5 This Exception not wil give all information and this is a bad practice coding style.

# 6
# Except IOError -  Commonly, the IOError is raised when an input output operation like open() file, or a method ...
# Except ZeroDivisionError handles divison by zero

# 7, 8
with open("c:/temp/words.txt", 'w') as file:
    file.write('maxim')
    file.close()

# 9
with open("c:/temp/words.txt", 'r') as file:
    print(file.readlines())
    file.close()

# 10
with open("c:/temp/hebrew.txt", 'w', encoding='utf') as writer:
    writer.write('שלום')
    writer.close()

with open("c:/temp/hebrew.txt", 'r', encoding='utf') as reader:
    print(reader.readlines())
    reader.close()
