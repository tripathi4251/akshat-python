#Check if one set is completely inside another.

p={"a","b","c","e","f","d"}
e={"d","b","c","e","f","a"}
z=p.issubset(e)
print(z)


#Check if a set contains all elements of another.
t={"a","b","c"}
f={"a","b","c","d","e"}
y=t.issuperset(f)
print(y)