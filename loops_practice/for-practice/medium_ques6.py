
# Find and print the sum of the Fibonacci series. 

n = 7

a = 0
b = 1
sum = 0

for i in range(n):
    print(a)

    sum = sum + a

    c = a + b
    a = b
    b = c

print("Sum =", sum)