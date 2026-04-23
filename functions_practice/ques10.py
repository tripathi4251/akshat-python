#Check Palindrome
# Check if string reads same forward/backward.

def is_palindrome(s):
 return s==s[::-1]

print(is_palindrome("madam"))


#Count Vowels
# Count vowels in string.

def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
               count+=1
               return count
    
print(count_vowels("hello world"))
