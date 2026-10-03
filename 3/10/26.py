class number :
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2


    def __gt__(self,other):
        return self.number1 > other.number2

numbers = number(60,50)    
print(numbers.number1 > numbers.number2)