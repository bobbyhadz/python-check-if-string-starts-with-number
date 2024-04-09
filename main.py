# Check if a string starts with a Number in Python

my_str = '248bobby'

if my_str and my_str[0].isdigit():
    # 👇️ this runs
    print('The string starts with a number')
else:
    print('The string does NOT start with a number')

print('248bobby'[0].isdigit())  # 👉️ True
print('bobby'[0].isdigit())  # 👉️ False
print('_bobby'[0].isdigit())  # 👉️ False