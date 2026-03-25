#Find elements present in one set but not in another.

a={1,2,3}
b={2,3}
print(a-b)


#Find elements present in either set but not both.
c={"car","bike","auto","ricksaw"}
d={"car","bike","cherry","banana"}
e=c.symmetric_difference(d)
print(e)



