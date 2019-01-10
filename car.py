


class Car(object):

    wheels = 4
    doors=4
    mirrors=2

    @staticmethod
    def make_car_sound():
        print ('VRooooommmm!')
    def __init__(self, make, model):
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')
print (mustang.wheels)
print (Car.wheels)
print (mustang.mirrors)
print (Car.mirrors)
print (mustang.make)
print (mustang.model)
mustang.make_car_sound()
