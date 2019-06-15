"""
Условные и циклические конструкции языка
"""
a = input("First number >>> ")
b = input("Second number >>> ")

if a > b:
    print(a)
elif a == b:
    print("Equals")
else:
    print(b)

number = 200
while number < 500:
    print("Not ready")
    # number = number + 2
    number += 2
else:
    print("Ready")


users = ['John', 'Artur', 'Kate']

for user in users:
    # print("Hello", user)
    print(f"Hello, {user}!")

