class Vehicle(object):
    
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2

    def __init__(self, make, model):
        self.make = make
        self.model = model


pleasure = Vehicle('hero', 'pleasure')
print(pleasure.make)
print (pleasure.is_motorcycle())