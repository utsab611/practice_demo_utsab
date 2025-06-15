class calc:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    
if __name__=="__main__":
    number1=100
    number2=20
    calculator=calc(number1,number2)
    print(f"Adding: {calculator.add()}")
    print(f"Subtracting: {calculator.sub()}")
    print(f"Multiplying: {calculator.mul()}")
    print(f"Dividing: {calculator.div()}")
