class Bankaccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                 print("Insufficient Balance")
     
            
        

    def get_balance(self):
        return self.__balance
    

a = Bankaccount(1000)
a.deposit(1000)
a.withdraw(255)
print(a.get_balance())