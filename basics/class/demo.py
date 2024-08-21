class A:
    def __init__(self) -> None:
        pass
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
    def feature3(self):
        print("feature 3 is working")

class B(A):
    def __init__(self) -> None:
        pass
    def feature4(self):
        print("feature 4 is working")

class C(B):
    def __init__(self) -> None:
        pass
    def feature5(self):
        print("feature 5 is working")

# a = A()
# a.feature1()
# a.feature3()

# b = B()
# b.feature3()

c = C()
c.feature1()
