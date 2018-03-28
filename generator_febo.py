def febo():
    a,b=0,1
    while True:
        yield (a)
        a,b=b,a+b
for f in febo():
    if f>100:
        break
    print(f)