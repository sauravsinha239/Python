class Base:

    def add(self, x,y):
        return x+y
class child(Base):
    def sub(self, x,y):
        print("Add=",super().add(x,y))
        print("Sub = ",x-y)
c1 = child()
c1.sub(10,5)

