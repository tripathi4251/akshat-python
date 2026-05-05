#sum of digits of a number 1234 inputs
num = 1234
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum =", sum)