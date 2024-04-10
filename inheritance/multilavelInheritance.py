class Base:
        def fun1(self):
                print("Hey Buddy i am Base Class fun1 ")
class Child0(Base):
        
        def fun2(self):
         print("Hey Buddy i am Child0 Class fun2")

class Child1(Child0):
      def fun3(self):
            print("Multilavel Inheritance Example ")
            print("Hey Buddy i am Child1 Class fun3")
            super().fun1()
            super().fun2()
obj = Child1()

obj.fun3()
            