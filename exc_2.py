
def sort_string(string):
    lowercase = []
    uppercase = []
    for char in string:
        if char.islower():
            lowercase.append(char)
        elif char.isupper():
            uppercase.append(char)
    return ''.join(lowercase) + ''.join(uppercase)

string = str(input("Please enter a string: "))
print(sort_string(string))