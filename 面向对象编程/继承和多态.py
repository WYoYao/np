class Animal(object):
    def running(self):
        print("running")

    def eating(self):
        print("Eating")


class Dog(Animal):
    # 子类覆盖父类的继承的方法称之为多态
    def running(self):
        print("Dog is running")




# 通过继承得到的父类的属性
Dog().eating()

# 多态 覆盖了父级的方法
Dog().running()
