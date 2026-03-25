#remove elements that are common in both sets.

a={"a","b","c",1,2,3,4,5}
b={"a","b","c","d","e","f","h"}
c=a.symmetric_difference(b)
print(c)