#Count vowels
# "hello" → 2

str="hello"
count=0
for ch in str:
    if ch in "aeiou":
        count+=1

        print(count)
