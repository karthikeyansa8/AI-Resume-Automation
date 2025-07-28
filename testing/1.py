class A:
    def show(s):
        print("A")
        
class B(A):
    def show(s):
        print("B")
        super().show()
        
class C(B):
    def show(self):
        print("C")
        super().show()

class D(C):
    def show(self):
        print("D")
        super().show()
        
d= D()
d.show()

print(D.mro())


# print(5/2)


print(5|2)