#--------------------single-level --------------------
class Father:
    car="nano"
    money=10000
    bike="hero honda"

class kanha(Father):
    land="10area"
    house="3BHK"
    bike="himalayan"

mother=Father()
sweetHeart=kanha()
Father.money=50000
print(Father.money)
print(mother.money)
print(kanha.money)
print(sweetHeart.money)   

#-----------------------multiple -----------------------
class A:
    x=100
    y=200
    def __init__(self,n):
        self.n=n

class B:
    x=123
    def __init__(self,n,ac):
        self.n=n
        self.ac=ac

class C(A,B):
    pass
print(C.mro()) #C--->A--->B--->object

class D(B,A):
    def __init__(self, n, ac,bc):
        self.n=n
        self.ac=ac
        self.bc=bc
print(D.mro()) #D--->B--->A--->object   


#---------------------Hirarchial---------------------------
class A:
    x=100
    y=200
    def __init__(self,n):
        self.n=n

class B(A):
    x=123
    def __init__(self,n,ac):
        self.n=n
        self.ac=ac

class C(A):
    pass
print(C.mro()) #C--->A--->object 
print(B.mro()) #B--->A--->object 
print(C.x) #100
print(B.x) #123  


#----------------------multi-level---------------------
class A:
    x=100
    y=200
    def __init__(self,n):
        self.n=n

class B(A):
    x=123
    def __init__(self,n,ac):
        self.n=n
        self.ac=ac

class C(B):
    pass
print(C.mro()) #C--->B--->A--->object 
print(C.x) #123   


#--------------------------Hybrid-----------------------
#example of hybrid inheritance with both multiple and multi-level inheritance.
class A:
    x=100
    y=200
    def __init__(self,n):
        self.n=n

class B():
    x=123
    def __init__(self,n,ac):
        self.n=n
        self.ac=ac

class C(A):
    pass

class D(B):
    pass

class E(C,D):
    pass
print(E.mro()) #E--->C--->A--->D--->B--->object   


#example of hybrid inheritance with both  hirarchial,multiple and multi-level inheritance.
class A:
    x=100
    y=200
    def __init__(self,n):
        self.n=n

class B(A):
    x=123
    def __init__(self,n,ac):
        self.n=n
        self.ac=ac

class C(A):
    pass

class D(C,B):
    pass

print(D.mro()) #D--->C--->B--->A--->object