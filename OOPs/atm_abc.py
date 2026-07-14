from abc import ABC,abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class MyBankAccount(ATM):
        def withdraw(self,amount):
            self.__verify_pin()
            self.__check_balance()
            self.__update_server()
            print("withdraw", amount)
            print("Cash withdrawn successfully.")

        def __verify_pin(self):
            print("Pin verified")

        def __check_balance(self):
            print("Balance checked")

        def __update_server(self):
            print("Server updated")

a = MyBankAccount()
a.withdraw(1000)