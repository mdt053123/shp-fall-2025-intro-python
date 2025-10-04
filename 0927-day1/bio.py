# write a program that asks the user for their name, birth year, favorite hobby, favorite food
# print that information, and calculate their age as of 2025

name = input("Enter name: ")
birth_year = int(input("Enter birth year: "))
hobby = input("Enter hobby: ")
food = input("Enter food: ")

# print info
print(f"Hello, your name is {name}, you were born in {birth_year}, " +
      f"your favorite hobby is {hobby}, your favorite food is {food}.")
# calculate and print age as of 2025
age = 2025 - birth_year
print(f"As of 2025, you are roughly {age} years old.")