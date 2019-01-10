class Store(object):
    """"Defines a class with name Store"""
    def __init__(self,id,price,quantity):

        self.id=id
        """defines id of the object"""
        self.price=price
        """defines price of the object"""
        self.quantity=quantity
        """defines no. of units of the object"""

    def remov(self,n):
        if self.quantity>n:
            self.quantity-=n
            return self.quantity
        else:
            printf("requested quantity of commodity unavailable")

    def add(self,m):
        self.quantity+=m
        return self.quantity

rice=Store(1,200,30)
wheat=Store(2,400,50)
print (rice.remov(12))
print(wheat.remov(15))


