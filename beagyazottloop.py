#nested loops
for i in range(3):
    for j in range(3):
        print(i,j)

for i in range(1):
    print("  *")
    for i in range(1):
        print(" ***")
        for i in range(1):
            print("*****")


for i in range(3):
    for j in range(3 - i - 1):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print("*", end="")
    print()

string="Hello World!"
for s in string:
    print(s)

#any()
#password=input("Enter password: ")
#if len(password)<8:
#    print("The password must be at least 8 characters long")
#elif any(char.isdigit() for char in password):
#    print("The password must contain at least one number")

hw="Hello World!"
if any(char.isupper() for char in hw):
    print("true")
else:
    print("false")

if all(char.isupper() for char in hw):
    print("true")
else:
    print("false")


for char in hw:
    print(char.isupper())

(print(char.isupper()) for char in hw)


error=[]
#any()
password=input("Enter password: ")
if len(password)<8:
    error.append("The password must be at least 8 characters long")
elif not any(char.isdigit() for char in password):
    error.append("The password must contain at least one number")
elif not any(char.isupper() for char in password):
    error.append("The password must contain a capitalized letter")
elif not any(char.islower() for char in password):
    error.append("The password must contain 1 normal letter")
elif any(char.isalnum() for char in password):
    error.append("The password must contain a special character")

print(error)











