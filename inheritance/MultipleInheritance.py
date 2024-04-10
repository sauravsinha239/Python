class Base0:

    def fun1(self):
        print("Hey Buddy i am class Base 0  fun1")

class Base1:

    def fun2(self):
        print("Hey Buddy i am class Base 1  fun2")

class Child(Base0,Base1):

    def out(self):
        print("Multiple Inheritance ")
        print("I am  from child class out function")
        super().fun1()
        super().fun2()

obj = Child()
obj.out()