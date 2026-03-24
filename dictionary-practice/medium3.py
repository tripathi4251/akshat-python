# Squares dictionary Create a dictionary where:
#keys = numbers (1 to n)
#values = squares of those numbers
#Example: 1:1, 2:4, 3:9

n=5
d={}
for i in range(1,n+1):
    d[i]=i*i
    print(d)