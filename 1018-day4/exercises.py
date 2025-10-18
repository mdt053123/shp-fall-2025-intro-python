class StringAnalyzer:
    def __init__(self, s):
        self.s = s
        
    def is_palindrome(self):
        # return True if self.s is a palindrome, False otherwise
        return self.s == self.s[::-1]
        
    def contains_only_vowels(self):
        # return True if all chars are vowels, False otherwise, vowels are A, E, I, O, U, Y
        for char in self.s.upper():
            if char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and char != 'Y':
                return False
        return True
        
    def contains(self, sub):
        # return True if sub is a substring of self.s, False otherwise
        if not sub: # not sub <=> sub == "", if sub is empty, it must be a substring
            return True
        
        starting_char = sub[0]
        for i in range(len(self.s)):
            if self.s[i] == starting_char:
                if self.s[i : i + len(sub)] == sub:
                    return True
                
        return False
        
str_analyzer = StringAnalyzer("racecar")
print(str_analyzer.is_palindrome()) # True
print(str_analyzer.contains_only_vowels()) # False
print(str_analyzer.contains("ar")) # True