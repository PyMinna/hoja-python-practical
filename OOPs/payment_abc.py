from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(payment):
    def pay(self, amount):
        print("Paid", amount ,"using UPI")
        
        

class Card(payment):
    def pay(self, amount):
        print('Paid', amount, "using card")
        

u = UPI()
c = Card()
u.pay(500)
c.pay(1000)