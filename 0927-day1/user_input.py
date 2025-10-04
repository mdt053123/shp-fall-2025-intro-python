name = input("Enter a name: ") # input ALWAYS returns type 'str'
print(name)

temp = int(input("Enter temp: ")) # return 'str' and cast as 'int'
print(type(temp))
print(temp)

print("Hello,", name)

print(f"Hello, {name}!")

print(f"My name is {name}, and the temperature today is {temp} degrees!")