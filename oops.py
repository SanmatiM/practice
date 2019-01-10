class Customer(object):


    def __init__(self, name, balance=0.0):

        self.name = name
        self.balance = balance
        print(self.name)
        print(self.balance)

    def withdraw(self, amount):

        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):

        self.balance += amount
        return self.balance


sannu=Customer("Sanmati",1000.0)
print (sannu.withdraw(500))
print (sannu.deposit(1500))
