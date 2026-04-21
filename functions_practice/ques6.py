#check Positive/Negative
# Check if number is positive, negative, or zero.

def check(num):
    if num>=0:
        return "positive"
    elif num<=0:
        return "negative"
    else:
        return "zero"
    
print(check(-5))