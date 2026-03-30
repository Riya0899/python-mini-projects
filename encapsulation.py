# hiding the internal properties and methods within a class is called encapsulation

# access modifiers-private,public,protected

class Bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>0:
            self.__balance = amount
        else:
            print("invalid amount")
account=Bankaccount(100)
print(account.get_balance())
account.set_balance(200)
account.set_balance(-50)
# print(account.get_balance())

# calculator-enter two numbers,operator,answ,do you want to continue-y/n?,previous result willl be stored as a first numberagain ask no and op
# star pattern

class Calculator:
    def __init__(self,num1):
        self.__num1 = num1
    def calculate(self,op,num2):
        if op == "+":
            self.__num1 = self.__num1 + num2
        elif op == "-":
            self.__num1 = self.__num1 - num2
        elif op == "*":
            self.__num1 = self.__num1 * num2
        elif op == "/":
            self.__num1 = self.__num1 / num2  
                 
        return self.__num1   

class cal(Calculator):
    def calculate(self,op,num2):
        result = super().calculate(op,num2)
        print("Result:",result)
        return result
    
    
num1=int(input("enter num1: "))
op = input("Enter op(+,-,*,/): ")
num2=int(input("enter num12: "))

calc = cal(num1)
result = calc.calculate(op,num2)

while True:
    ch = input("continue?(yes/no): ")
    
    if ch.lower()=="yes":
        op = input("Enter op(+,-,*,/): ")
        num2=int(input("enter num12: "))
        result = calc.calculate(op,num2)
    else:
        print("final result: ",result)
        break

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.result=0
    def add(self):
        self.result = self.num1 + self.num2
        return self.result

    def subtract(self):
        self.result = self.num1 - self.num2
        return self.result

    def multiply(self):
        self.result = self.num1 * self.num2
        return self.result

    def divide(self):
        if self.num2 != 0:
            self.result = self.num1 / self.num2
            return self.result
        else:
            return "cannot divide by zero"

num1 = int(input("Enter first number: "))
while True:

    op = input("Enter operator (+,-,*,/): ")
    num2 = int(input("Enter second number: "))

    calc = Calculator(num1, num2)

    if op == "+":
        res = calc.add()

    elif op == "-":
        res = calc.subtract()

    elif op == "*":
        res = calc.multiply()

    elif op == "/":
        res = calc.divide()

    else:
        print("Invalid operator")
        continue

    print("Result =", res)

    choice = input("Do you want to continue? (y/n): ")

    if choice== "y":
        num1 = res
    else:
        print("Calculator stopped.")
        break


for rows in range(7):

    for col in range(5):
        if col==0 or (col==4 and (rows!=0 and rows!=3)) or ((rows==0 or rows==3) and (col>0 and col<4)):
            print('*',end="")
        else:
            print(" ",end="")

    print("  ",end="")   

    for col in range(5):
        if col==2 or ((rows==0 or rows==6) and col!=2):
            print("*",end="")
        else:
            print(" ",end="")

    print("  ",end="")

    for col in range(5):
        if (col==2 and rows>1) or (rows==col and col<2) or (rows==0 and col==4) or (rows==1 and col==3):
            print("*",end="")
        else:
            print(" ",end="")

    print("  ",end="")

    for col in range(5):
        if ((col==0 or col==4)and rows!=0) or ((rows==0 or rows==3)and(col>0 and col<4)):
            print("*",end="")
        else:
            print(" ",end="")

    print()   