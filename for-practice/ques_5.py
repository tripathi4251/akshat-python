#sum of odd numbers upto 1 to n
n = 10
total = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total += i

print("Sum =", total)