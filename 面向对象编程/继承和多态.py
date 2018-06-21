class Animal(object):
    def running(self):
        print("running")


class Dog(Animal):
    def run(self):
        print("Dog is running...")
        return self

    def eat(self):
        print("Eating meat...")
        return self


Dog().run()
Dog().running()

