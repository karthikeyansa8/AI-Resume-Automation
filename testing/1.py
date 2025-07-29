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


c=0
for i in range(1,20):
    for j in range(1,i):
        for k in range(1,j):
            c+=1
print(c)