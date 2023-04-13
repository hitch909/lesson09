#реализовать метакласс. позволяющий создавать всегда
#один и тот же объект класса (см. урок)

class TypedMeta(type):
    a = None

    def __call__(cls, a):
        if a == None:
            a = super().__call__(a)
            a.new_attr = 1
        return a


class Myclass(metaclass=TypedMeta):

    def method_1(self):
        pass

    def method_2(self):
        print("небольшая проблемма")


# синглтон
obj_1 = Myclass('a')
obj_2 = Myclass('a')
obj_3 = Myclass('a')
print(obj_1 is obj_3)
