class madeexe(Exception):
    def too_young(self):
        print("you are too young for having a lisence")
    def too_old(self):
        print("you are too old for having a lisence")
       
    
class raiseex:
    
    def age_limit(self,a):
        try:
            if a<18:
                raise madeexe
            else:
                print("you can apply for licence")
        except madeexe as e:
            e.too_young()
            
        try:   
            if a>60:
                raise madeexe
            else:
                raise madeexe
        except madeexe as d:
            d.too_old()        
            
            
            
class appliying:
    try:
        r=int(input("enter your age "))
        rai=raiseex()
        rai.age_limit(r)
    
    except "invalid age":
        print("you are too young to apply for the licence")
    finally:
        print("this is finally block after catch")

