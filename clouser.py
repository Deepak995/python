def e_mul(x):
    def mul(y):
        return x*y
    return mul
g=e_mul(10)
print(g(3))
