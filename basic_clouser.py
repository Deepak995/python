def a(msg):
    def b():
        print(msg)
    return b #returning function b not excuting b

f=a("this is the msg for a")# variable a is working like a function
f()
        