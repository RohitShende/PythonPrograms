class Base1:
    z = 3
    def fun(self):
        print("From Base1")


class Base2:
    y = 2
    def fun(self):
        print("From Base2")


class MultiDerived(Base1, Base2):
    # def fun(self):
    #     print("From MultiDerived")
    x = 1
    pass


print(MultiDerived.mro())   # Method Resolution Order (MRO)
obj = MultiDerived()
print(obj.fun())
print(obj.x, obj.y, obj.z)
