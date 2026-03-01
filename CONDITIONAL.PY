num= 3
if num>0:
        print(num,"is a positive number.")

num=-1
if num>0:
        print(num,"num is positive")

actual_cost=float(input("Please enter the actual prouduct price:"))
sales_amount=float(input("Please enter the actual sales amount:"))

if (sales_amount>actual_cost):
    amount=sales_amount-actual_cost
    print("total profit+{0}".format(amount))
else:
       print("No Profit!!!!!")

num1=int(input("enter the first munber"))
num2=int(input("enter the second munber"))
if num1>num2:
       print("num1 is greater than num2")
else:
       print("num2 is greater than num1")
if num1 ==num2:
    print("both are equal")