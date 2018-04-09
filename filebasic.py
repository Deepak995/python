o = open("palindrome.txt","w")
print(o)
print(o.writelines("go to hell\n"))
list=["hi my name is Deepak i am from jabalpur\n","i like to listen music\n","actully i love music\n"]
o.writelines(list)
print(o.writelines("i will see you there"))
o.close()

"""j=open("palindrome.txt","r")
print(j)
print(j.read())"""

k=open("hello.txt","r")
for line in k:
    g=line.split(".")
    k=open("hello2.txt","w")
    for i in g:
        k.writelines(i)
        k.writelines("\n")
"""fh = open("hello.txt","w") 
lines_of_text = ["One line of text here\n", "and another line here\n", "and yet another here\n", "and so on and so forth\n"] 
fh.writelines(lines_of_text) 
fh.close()""" 