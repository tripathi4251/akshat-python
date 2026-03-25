#Find elements with no duplicates across multiple lists What to do:
#Given 2–3 lists, print elements that appear only once overall.

l1=[1,2,3]
l2=[2,3,4]
l3=[3,4,5]
all_elements=l1+l2+l3
result=[]
for i in all_elements:
    if all_elements.count(i)==1:
        result.append(i)
        print(set(result))