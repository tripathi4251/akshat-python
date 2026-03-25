#Count how many elements are common in two sets.

s1={"a","b","c",1,2,3,4,5,"d"}
s2={"a","b","c",1,2,3,6,7,8}
s3=s1.intersection(s2)
print(len(s3))
print(s3)