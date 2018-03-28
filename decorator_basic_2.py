def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display function ran")
display()

@decorator_function
def display_2(name,age):
    print('display_2 ran with argument({},{})')
display_2('deepak',22)
        
        
