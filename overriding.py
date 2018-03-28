class plane :
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
class c (plane):
    def fly(self):
        super().fly()
        print("c plane is flying")
    def land(slef):
        print("c plane is landing")
        #super(c,self).fly()
        #super(c,self).land()
    
ob=c()
ob.fly()


