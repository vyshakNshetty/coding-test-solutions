# calculator using class

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def operate(self,operation):
        if operation=='add':
            return self.a+self.b
        elif operation=='subtract':
            return self.a-self.b
        elif operation=='multiply':
            return self.a*self.b
        elif operation=='divide':
            return self.a/self.b
        else:
            return 'Invalid operation'
        
calc=Calculator(10.0,5.0)
print(calc.operate('add'))