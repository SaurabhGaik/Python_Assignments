class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    def show(self):
        print("D")

class E(D):
    def show(self):
        print("E")

e = E()
e.show()
print(E.mro())
