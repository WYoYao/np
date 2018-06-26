class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

Hello().hello()

# type()函数可以查看一个类型或变量的类型
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# 我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

def fn(self, name='world'):
    print('Hello, %s.' % name)


#    1.class的名称；
#    2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#    3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello1=type("Hello1",(object,),dict(hello=fn))

Hello1().hello()

# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    # 1.当前准备创建的类的对象；
    # 2.类的名字；
    # 3.类继承的父类集合；
    # 4.类的方法集合。
    def __new__(cls, name, bases, attrs):
        print(cls)
        print( name)
        print(bases)
        print(attrs)
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list,metaclass=ListMetaclass):
    pass

mylist = MyList()
mylist.add(1)
print(mylist)