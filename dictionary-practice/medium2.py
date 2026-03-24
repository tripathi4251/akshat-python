#common keys-find keys that are in both dictionaries

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

for key in d1:
    if key in d2:
        print(key)
