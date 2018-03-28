class employee:
        __p=0
        def __init__(self,p):
          self.__p=p
        def setId(self,id):
          self.id=id         
          
        def getter(self):
          print ("the no you have entered is ",self.id)
        def em(self):
          print(self.__p)
          
          
emp = employee(100)
emp.setId(12)         
emp.getter()
emp.em()
          
    
    