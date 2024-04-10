class Base:

    def fn(self):
        print("I am Base Class fn ")

class Child0(Base):

    def fn1(self):
        print("I am Child 0 Class fn1")
        super().fn()

class Child1(Base):

        def fn3(self):
             print("Hey I am Child 1 Class fn 3")
             super().fn()

child0obj= Child0()

child0obj.fn1()

ch1obj = Child1()

ch1obj.fn3()
