# basic calculator program (1hr mark)

import math
print("Reminder : this is a basic calc. it can not perform complex calculations")


print("For exponentiation num1 =  base and num2 = power")


operator = input("Enter an operator (+, -, *, /, ^) : ").strip()

num1 = float(input("Enter first number: "))




num2 = float(input("Enter second number/ power : "))

#quotient = num1 / num2
#quotient = round(quotient, 2)

#prod = num1 * num2
#prod = round(prod, 2)



if operator == "+":
    print(f"sum is: {num1 + num2}")


elif operator == "-":
    print(f"difference is: {num1 - num2}")


elif operator == "*":
    print(f"Product is : {round(num1 * num2 , 2)}")

elif operator == "/":
    print(f"Quotient is : {round(num1 / num2 , 2)}")

elif operator == "^":
    print(f"Result is : {pow(num1, num2)}")

else:
    print(f"{operator} is invalid operator ! ")

#Note self : before video => does not give negative value 

    


