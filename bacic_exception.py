
        
class division:
    def divi(self, a,b):
      try: 
         # a=int(input("enter the value of a  "))
          #b=int(input("enter the value of b"))
          c=a/b
      except ArithmeticError :
          print("enter the right value of b")
      else:
          return c
      print("this is a free statement")


class exe:
        a=int(input("enter the value of a  "))
        b=int(input("enter the value of b"))
        
        ob=division()
        d=ob.divi(a,b)
        print(d)
