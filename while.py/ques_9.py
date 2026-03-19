#count digits in a number
num = 4567
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Digits =", count)