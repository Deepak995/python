class overloading:
    def add(self,a,b):
        c=a+b
        print("the addition of the two no is %d" % c)
    def add(self,a,b,c):
        d=a+b+c
        print("the addition of three no is %d" % d)
f=overloading()
f.add(10,15,10)