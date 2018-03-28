def  decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function is running')
display=decorator_function(display)    
display()