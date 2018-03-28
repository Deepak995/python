f=open("te.txt",'w+')
f.write("123")
f=open("te.txt",'a')
f.write("\nmy name is bla bla bla ")
f=open("te.txt",'a')
f.write("\ni like bla bla bla ")
f=open("te.txt",'a')
f.write("\ni have studied  bla bla bla ")
f=open("te.txt",'r')
print(f.read())
f.close()
f=open("te.txt",'r')
for line in f:
    var=line
    print(var)
    d=len(var)

    for v in d
    print(len(var)-2)
    #for a in len(var)
#print(var)

