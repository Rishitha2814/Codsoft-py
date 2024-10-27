num1=int(input("enter the first value:"))
num2=int(input("enter the second value:"))
operator=input("give a operator:")
if operator == "+":
    print(f"addition of two numbers {num1+num2}") 
elif operator == "-":
    print(f"subtraction of two numbers {num1-num2}")
elif operator == "*":
    print(f"multiplication of two numbers {num1*num2}")
elif operator =="/":
    print(f"division of two numbers {num1/num2}")
else:
    print("not valid")

    
