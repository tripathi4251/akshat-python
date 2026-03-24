# remove duplicates from a dictionary


d1 = {
    "a": 1,
    "b": 2,
    "c": 1
}

new_d ={}
for k,v in d1.items():
    if v not in new_d.values():
        new_d[k]=v
        print(new_d)