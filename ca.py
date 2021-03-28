# # import re
# # st = """Interface             IP-Address      OK?    Method Status         Protocol
# # GigabitEthernet0/1    unassigned      YES    unset  up             up
# # GigabitEthernet0/2    192.168.190.235 YES    unset  up             up
# # GigabitEthernet0/3    192.168.191.1      YES    unset  down             up
# # GigabitEthernet0/4    192.168.191.2   YES    unset  down             down
# # TenGigabitEthernet2/1 unassigned      YES    unset  up             up
# # TenGigabitEthernet2/2 unassigned      YES    unset  up             up"""
# # match = re.findall(r'.*\d\/\d+\s+(\d+\.\d+\.\d+\.\d+).*\s+(\w+)\s+\w+\n',st)
# # #print (match)
# # for i in match:
# #     if i[1] == "up":
# #         print(i[0])
#
#
# l1 = [-3,-2,4,0,7,3,1,5,2]
# add = 0
# l22 = []
# for i in l1:
#     for j in l1:
#         a=-i-j
#         if a in l1:
#
#         #for a in l1:
#             #if i+j+a == 0:
#             #add = add +l1[j]
#                 #s=set()
#                 #print(i,j,a)
#             #if (i!=j and j!=a and a!=i):
#             #print("333333333333")
#             #print(i,j,a)
#             #break
#             lis = [i,j,a]
#             l2 = l22.append(lis)
#             lis = []
# print(l22)
# lisss = []
# liss1 = []
# for i in l22:
#     lisss.append(sorted(i))
# print(len(lisss))
# for i in lisss:
#     l = lisss.pop()
#     liss1.append(l)
#     while l in lisss:
#         lisss.remove(l)
# print(liss1)
#
#
#
#
# print("**********************************************************************************")
# # l1 = []
# # s3 = ''
# # s4= ''
# # s1 = ''
# # s2 = ''
# # max = 0
# # for i in range(0,len(stri)):
# #     for j in range(len(stri)-1,0,-1):
# #         if stri[i] == stri[j]:
# #             k = i
# #             p = j
# #             while stri[k]==stri[p] and k!=p:
# #                s1 = s3+stri[k]
# #                s2 = s4+stri[p]
# #                s5 = s1 + s2[::-1]
# #                k+=1
# #                p-=1
# #             print(s5)
# #             if len(s5)>=max:
# #                 final_string = s5
# #                 max = len(s5)
# #                 s5 = ""
# #                 s1 = ""
# #                 s2 = ""
# #                 s3 = ""
# #                 s4 = ""
# #
# # print(final_string)
# def ispalindrom(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False
# max = 0
# s1 = ""
# stri = 'abakekayayak'
# for i in range(0, len(stri)):
#     for j in range(i, len(stri)+1):
#         #print(stri[i:j])
#         ret = ispalindrom(stri[i:j])
#         if ret and len(stri[i:j])>=max:
#             max = len(stri[i:j])
#             s1 = stri[i:j]
# print(s1)
#
#
Names= ["Sayali", "Deepak", "Bob", "Bala", "Smita", "Aditya"]

def extector(a):
    #print(a)
    if a[0]=="B":
        return a

ret = map(extector, Names)
print(list(ret))










































