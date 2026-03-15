#1 print 1 to 10 numbers 
for i in range (1,11):
    print(i)

#2 print 1 to 20 numbers
for i in range (1,21):
    if i%2==0:
     print(i)

#3 print 1 to 20 odd numbers
for i in range(1,21):
   if i%2!=0:
      print(i)
   
   #4take a number from the user and print its table
n =int(input("enter number:"))
for i in range(1,11):
    print(n*i)

#5 take out the sum  of 1 to 50 numbers
sum=0
for i in range(1,51):
    sum+=i
    print("sum=", sum)
    

#6 print the reverse counting from 10 to 1
for i in range(10,0,-1):
    print(i) 
