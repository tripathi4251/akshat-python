#Check palindrome
# "madam" → True

str2="hello"
count=0

for ch in str2:
    if ch  not in "aeiou":
        count+=1

    print(count)