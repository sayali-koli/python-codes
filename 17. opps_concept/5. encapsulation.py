class Bank:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("invilide amount")
        else:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


s = Bank("sayali", 1000)
print(s.get_balance())
s.deposit(500)
print(s.get_balance())
print(s._Bank__balance)
