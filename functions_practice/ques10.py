#Check Palindrome
# Check if string reads same forward/backward.


def is_palindrome(s):
 return s==s[::-1]

print(is_palindrome("madam"))