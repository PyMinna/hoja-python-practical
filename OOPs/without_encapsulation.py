class Bankaccount:
    def __init__(self,balance):
        self.balance = balance
        self.__balance = balance


    def get_balance(self):
        return self.__balance
       
       

a = Bankaccount(2000)
print(a.get_balance())

print(a.balance)
a.balance -= 500
print(a.balance)

