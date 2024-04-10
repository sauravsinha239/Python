class Parents:

    def fn(self):
        print("This is Parents Class")

class Base0(Parents):

    def  Fnb0(self):
        print("This is Base0 Fnb0  function Inherited by Parents")

class Base1:

    def Fnb1(self):
        print("This is Base 1  No Any Class Inherited me ")

class Child(Base0,Base1):
        
        def Chfn(self):

            print("Inherited by Base0 and Base 1")
            super().Fnb0()
            super().Fnb1()
            super().fn()

obj = Child()

obj.Chfn()