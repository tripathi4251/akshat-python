# Invert dictionary Swap keys and values Example: {"a":1} → {1:"a"}

d={
    "a": 1,
    "b": 2,
}

new_d ={}
for k,v in d.items():
    new_d[v]=k
print(new_d)