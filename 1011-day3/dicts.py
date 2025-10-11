phone_numbers = {'Michael' : '9145551234', 'Bob' : '2031295567', 'Alice' : '6031125556'}

print(phone_numbers['Michael'])

print(list(phone_numbers.keys()))
print(list(phone_numbers.values()))

print(phone_numbers.get('Bob')) # same as doing phone_numbers['Bob']

student_rosters = { 'class-1' : ['Bob', 'Alice', 'John'], 'class-2' : ['Gary', 'Grace'] }

print(list(phone_numbers.items()))