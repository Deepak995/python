def decorator_function(original_function):
    def wrapper_function():
        print("this is the wrapper functioon ")
        return original_function()
    return wrapper_function 
@decorator_function
def display():
    print("display function is running ")
display()