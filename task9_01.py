# реализовать дескрипторы

class Descr:
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if value > 35:
            raise ValueError("масса асфальта выше нормы ")
        elif value < 20:
            raise ValueError("масса асфальта ниже нормы ")
        else:
            print('масса асфальта в норме')
            instance.__dict__[self.my_attr] = value


'''новый протокол дескрипторов'''


class Descr_next:

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if type(value) == str:
            raise ValueError("введенные данные должны быть числами ")
        instance.__dict__[self.my_attr] = value


class Road:
    weight = Descr('weight')
    thickness = Descr_next()
    length = Descr_next()
    width = Descr_next()

    def __init__(self, length, width, weight, thickness):
        self.length = length
        self.width = width
        self.weight = weight
        self.thickness = thickness

    def calculation(self):
        return self.length * self.width * self.weight * self.thickness


kl_road = Road(5000, 20, 30, 0.01)
print(f'{kl_road.calculation()} кг')
