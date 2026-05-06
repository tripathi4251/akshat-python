
# Find the HCF (Highest Common Factor) of the given numbers.


a = 12
b = 18

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF =", hcf)