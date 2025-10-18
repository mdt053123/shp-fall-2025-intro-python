class StringAnalyzer:
    def __init__(self, s):
        self.s = s
        
    def is_palindrome(self):
        # return True if self.s is a palindrome, False otherwise
        
    def contains_only_vowels(self):
        # return True if all chars are vowels, False otherwise, vowels are A, E, I, O, U, Y
        
    def contains(self, sub):
        # return True if sub is a substring of self.s, False otherwise
        
str_analyzer = StringAnalyzer("racecar")
print(str_analyzer.is_palindrome()) # True
print(str_analyzer.contains_only_vowels) # False
print(str_analyzer.contains("ace")) # True