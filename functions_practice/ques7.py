#multiply two numbers
#return multiplication of two numbers

def multiply(a,b):
    return a*b
print(multiply(9,10))



#check if a number is divisible or not by 5 and 11
def check(num):
    if num%5==0 and num%11==0:
        return "it is divisible"
    else:
      return  "it is not divisible"

print(check(11))