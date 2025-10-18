s = "Python" # ['P', 'y', 't', 'h', 'o', 'n']
print(s[0])
print(s[-1])

word = "abcde"
print(word[0:5:2])
print(word[::-2])

print(s[::-1])

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("Mom".lower())) # .lower() converts a string to all lowercase (.upper() the opposite)

print()

w = "a.b.c.d.e"
u = w.split('.')
print(u)
v = '.'.join(u)
print(v)