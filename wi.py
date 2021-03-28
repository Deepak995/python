### P-1 Reverse a list
#l= [1, 4, 6, 2, 19,13]
#for i in l[::-1]:
#     print(i)
# # ################################
### P-2 Prime NO...?
# no = 5
# for i in range(2,no+1):
#     print(i)
#     if i == no and no%i ==0:
#         print("is a prime no")
#         break
#     else:
#         continue
#######################################
### P-3 output should be {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# dicto = {}
# a = [1,2,3,4,5]
# b =  ["a","b","c","d","e"]
# for x,y in zip(a,b):
#     dicto[x] = y
#
# print(dicto)
###################################################
### P-4 Add to no by using oops consept
# class abc:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         c=10+20
#         return c
###########################################################
### P-5 Output should be like
# this ----> {'omp-uptime': '0:12:26:45', 'routes-received': '28', 'routes-installed': '6', 'routes-sent': '4', 'tlocs-received': '21', 'tlocs-installed': '10', 'tlocs-sent': '2', 'services-received': '3', 'services-installed': '0', 'services-sent': '6', 'mcast-routes-received': '3', 'mcast-routes-installed': '1', 'mcast-routes-sent': '2', 'hello-sent': '4487', 'hello-received': '4480', 'handshake-sent': '2', 'handshake-received': '2', 'alert-sent': '0', 'alert-received': '0', 'inform-sent': '16', 'inform-received': '16', 'update-sent': '3127', 'update-received': '2477', 'policy-sent': '0', 'policy-received': '2', 'total-packets-sent': '7632', 'total-packets-received': '6977', 'vsmart-peers': '2'}

# import re
# strr = """oper-state UP
# admin-state UP
# personality vedge
# omp-uptime 0:12:26:45
# routes-received 28
# routes-installed 6
# routes-sent 4
# tlocs-received 21
# tlocs-installed 10
# tlocs-sent 2
# services-received 3
# services-installed 0
# services-sent 6
# mcast-routes-received 3
# mcast-routes-installed 1
# mcast-routes-sent 2
# hello-sent 4487
# hello-received 4480
# handshake-sent 2
# handshake-received 2
# alert-sent 0
# alert-received 0
# inform-sent 16
# inform-received 16
# update-sent 3127
# update-received 2477
# policy-sent 0
# policy-received 2
# total-packets-sent 7632
# total-packets-received 6977
# vsmart-peers 2"""
#
# match = re.findall(r'(\S+)\s+(\S+)',strr)
# #print(match)
# dict1 = {}
# dict2 = {}
# for i in match:
#     if i[1].isalpha():
#         dict1[i[0]] = i[1]
#     else:
#         dict2[i[0]] = i[1]
#
# print(dict1)
# print(dict2)
# print(dict2['mcast-routes-received'])
#########################################################
### P-6 validate an ip address
# # # there should be only 4 octate
# # # all should be digit

# # inputt = input("enter ip")
# # match = re.match(r'(\d+\.\d+\.\d+\.\d+)',inputt)
# # if match:
# #     l = match.group(1).split('.')
# #     print(l)
# #     l1 = [i for i in l if int(i)>=255]
# #     if len(l1) == 0:
# #         print("IP is valid")
# #     else:
# #         print("Ip is not valid")
# # else:
# # #     print("Ip is not valid")
##############################################################
### P-7 count the occurance of each letter
# # s = 'hi i am Deepak hi i am not'
# # s1 = s.split(" ")
# # s2 = set(s1)
# # print(s2)
# # for i in s2:
# #     print("word {0} count {1}".format(i,s1.count(i)))
# #
# # dicto =  {'A':100, 'B':1292, 'C': 210000, 'D' : 88}
# # max = 0
# # for key, value in dicto.items():
# #     if max < value:
# #         max = value
# #         max_key = key
# # print(max_key)
# #
################################################
### P-8 what will be the output?
# # x= ['ab','cd']
# # print(list(x))
# # print(list(list(map(list,x))))

####################################################
### P-9 sort the list without inbuilt function
# l = [5,3,1,-2,-4]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] < l[j]:
#             c = l[i]
#             l[i] = l[j]
#             l[j] = c
# print(l)
#####################################################################
### P-10 input = [1,2,3,4,5,6,7] , output dhould be [4, 5, 6, 7, 1, 2, 3]
# l1 = [1,2,3,4,5,6,7]
# def rev(from_where, li):
#     new = []
#     index = l1.index(from_where)
#     new.extend(li[index::])
#     new.extend(li[0:index:])
#     print(new)
#
# rev(4, l1)
######################################################################
### P-11 print the non matching keys and its value from two dict

# Expected = { "adv" : "efdr", "wdd" : [4,3,1], "pqr" : {"lmn" : "ee3", "edwdw" : "qqdq"}}
#
# Actual = { "adv" : "efdr", "wdd" : [4,2,3], "pqr" : {"edwdw" : "qq\dq", "lmn" : "ee3"}}
#
# def dict_comp(Expected,Actual):
#     for key, value in Actual.items():
#         if key in Expected:
#             if Expected[key] != value and type(value) == str:
#                 print(key)
#                 print(Expected[key])
#                 print(value)
#             elif type(value) == dict:
#                 dict_comp(Expected[key], value)
#             elif type(value) == list:
#                 l=[j for j in value if j not in Expected[key]]
#                 print(l)
#                 if len(l) != 0 and Expected[key] != value:
#                     print(key)
#                     print(Expected[key])
#                     print(value)
#
# dict_comp(Expected, Actual)
#
#####################################################################
### P-12 print occurance of each charector
# p1 = "Dapeak"
# g1 = set(p1)
# countt = 0
# for i in g1:
#     for j in p1:
#         if i == j:
#             countt +=1
#     print("{} is occuring {} times ".format(i, countt))
#     countt = 0
#####################################################################
### P-13 find occurance of each charector and save it in a dictonary
# s1 = "how is the interview"
# dict = {}
# for i in s1:
#     coun = s1.count(i)
#     if coun > 1 and i!= " ":
#         dict[i] = coun
# print(dict)
#
#####################################################################
### P-14 save the input in a file and find the data whoes employee salary < 200000 and emp_age is > 50
# #input = {"status":"success","data":[{"id":1,"employee_name":"Tiger Nixon","employee_salary":320800,"employee_age":61,"profile_image":""},{"id":2,"employee_name":"Garrett Winters","employee_salary":170750,"employee_age":63,"profile_image":""},{"id":3,"employee_name":"Ashton Cox","employee_salary":86000,"employee_age":66,"profile_image":""},{"id":4,"employee_name":"Cedric Kelly","employee_salary":433060,"employee_age":22,"profile_image":""},{"id":5,"employee_name":"Airi Satou","employee_salary":162700,"employee_age":33,"profile_image":""},{"id":6,"employee_name":"Brielle Williamson","employee_salary":372000,"employee_age":61,"profile_image":""},{"id":7,"employee_name":"Herrod Chandler","employee_salary":137500,"employee_age":59,"profile_image":""},{"id":8,"employee_name":"Rhona Davidson","employee_salary":327900,"employee_age":55,"profile_image":""},{"id":9,"employee_name":"Colleen Hurst","employee_salary":205500,"employee_age":39,"profile_image":""},{"id":10,"employee_name":"Sonya Frost","employee_salary":103600,"employee_age":23,"profile_image":""},{"id":11,"employee_name":"Jena Gaines","employee_salary":90560,"employee_age":30,"profile_image":""},{"id":12,"employee_name":"Quinn Flynn","employee_salary":342000,"employee_age":22,"profile_image":""},{"id":13,"employee_name":"Charde Marshall","employee_salary":470600,"employee_age":36,"profile_image":""},{"id":14,"employee_name":"Haley Kennedy","employee_salary":313500,"employee_age":43,"profile_image":""},{"id":15,"employee_name":"Tatyana Fitzpatrick","employee_salary":385750,"employee_age":19,"profile_image":""},{"id":16,"employee_name":"Michael Silva","employee_salary":198500,"employee_age":66,"profile_image":""},{"id":17,"employee_name":"Paul Byrd","employee_salary":725000,"employee_age":64,"profile_image":""},{"id":18,"employee_name":"Gloria Little","employee_salary":237500,"employee_age":59,"profile_image":""},{"id":19,"employee_name":"Bradley Greer","employee_salary":132000,"employee_age":41,"profile_image":""},{"id":20,"employee_name":"Dai Rios","employee_salary":217500,"employee_age":35,"profile_image":""},{"id":21,"employee_name":"Jenette Caldwell","employee_salary":345000,"employee_age":30,"profile_image":""},{"id":22,"employee_name":"Yuri Berry","employee_salary":675000,"employee_age":40,"profile_image":""},{"id":23,"employee_name":"Caesar Vance","employee_salary":106450,"employee_age":21,"profile_image":""},{"id":24,"employee_name":"Doris Wilder","employee_salary":85600,"employee_age":23,"profile_image":""}],"message":"Successfully! All records has been fetched."}
#
# import os
# print(os.getcwd())
# se = open("dat.txt", 'r')
# ab = se.readlines()
# #print(ab[0])
# dat = eval(ab[0])
# #print(dat)
# for i in dat["data"]:
#     if i['employee_salary'] < 200000 and i['employee_age'] > 50:
#         print(i)
#####################################################################
### P-15 find the occurance of each int from list and save it in a dict
# l = [1,2,3,4,4,3,11,9,10,11,10]
#
# def occur(l):
#     count = 0
#     dicto = {}
#     listt = []
#     for i in l:
#         for j in l:
#             if i == j and i != "":
#                 indexx = l.index(j)
#                 l[indexx] = ""
#                 count += 1
#                 listt.append(indexx)
#         data = "".join(str(listt))
#         data = "index:"+data + "count:"+str(count)
#         dicto[i] = data
#         listt = []
#         count = 0
#     print(dicto)
#
# occur(l)
# l = [1,2,3,4,4,3,11,9,10,11,10]
# print(l)
#####################################################################
### P-16  open facebook through selenium
# import selenium
# from selenium import webdriver
# import os
#
# print(os.getcwd())
# driver = webdriver.Chrome("chromedriver.exe")
# driver.get("www.facebook.com")
#########################################################################
##### P-17 print the special charector from given input
# s1 = input("input the string")
# l = ['~','!','@','#','$','%','^','&','*','(',')']
#
# for i in s1:
#     if i in l:
#         print(i)
#####################################################################
##### P-18#reverse the string word by word using class program
# class reverse_one():
#     def __init__(self,strr):
#         self.strr =strr
#     def takein(self):
#         l = self.strr.split(" ")
#         l2 = l[::-1]
#         return " ".join(l2)
#
#
# class B(reverse_one):
#     def give(self):
#         print("input string is : "+self.strr)
#
# s1 = input("input the string")
# objj = B(s1)
# objj.give()
# print(objj.takein())
#####################################################################
###P-19 Replace somthing from given input
# s1 = 'how are you'
# s1 = s1.replace('how', 'who')
# print(s1)
#
# list = ['where are you']
# list = list[0].replace('where','who')
# print(list)
######################################################
###P-20 output should be ----->[4, 5, 6, 1, 2, 3]
# input = [1,2,3,4,5,6]
# output = []
# l = len(input)
# n = int(l/2)
#
# print(l)
#
# for j in range(n,l):
#     output.append(input[j])
# for i in range(0,n):
#     output.append(input[i])
# print(output)
######################################################
###P-21 output should be ----->{'sw1': 'vlan1', 'sw2': 'vlan2', 'sw3': 'vlan3'}
# import re
# swvlans = '''sw1 has vlan1
#         sw2 has vlan2
#         sw3 has vlan3'''
# dictt = {}
# match = re.findall(r'(sw\d+).*(vlan\d+)',swvlans)
# for i in match:
#     print(i[0])
#     print(i[1])
#     print(i)
#     dictt[i[0]] = i[1]
# print(dictt)

######################################################
###P-22 list all the files in current directory
# import os
# output = os.listdir()
# print(output)
# print(len(output))

######################################################
###P- 23 find the square of each element
# listt = [1,2,3,4,5,6]
# liis1 = [x*x for x in listt]
# print(liis1)

#######################################################################
### P - 24 Print the count of maximum consecutive no.??
# stringg = list(input("enter the input : "))
# #print("Beeetween")
# count,max = 0,0
# for i in range(0,len(stringg)):
#     for j in range(i+1,len(stringg)):
#         if stringg[i]==stringg[j]:
#             count = 1
#             for k in range(j, len(stringg)):
#                 if stringg[j]==stringg[k]:
#                     count+=1
#                 else:
#                     break
#                 if count>max:
#                     max=count
#             count = 0
#
# print(max)
#################################################################################################
### P - 25 Sort the list
# l1 = [34, 78, 9, 67, 45, 78, 101, 89]
# def srtt(list):
#     for i in range(len(l1)):
#         for j in range(len(l1)):
#             if l1[i] > l1[j]:
#                 z = l1[i]
#                 l1[i] = l1[j]
#                 l1[j] = z
#     print(l1[1])
# srtt(l1)
################################################################
### P -26 print the square of whatever is in even position
# l = [2, 4, 6, 8, 10, 12, 14, 16]
#
# l2 = [i*i for i in l[1::2]]
# print(l2)
################################################################
### P - 27 What willbe the output ans- error will come
# l = [1, 2, 3, 4, 5 , 'Deepak']
# l.sort()
################################################################
### P - 28 requrment is given below
# // Write a method, which, when given a number,
# // returns true if the string has atleast 2 digits that
# // are consequent digits.
# // Ex: 147 returns a false
# // Ex: 3740576 returns a true since 7,6 are adjacent numbers
# // Ex: 475 returns a false since 4,5 are adjacent numbers,
# // but they are not present side by side.

# inpu = "3740576"
# def adje(st):
#     m = False
#     for i in range(len(st)):
#         for j in range(1,len(st)):
#             if (int(st[j])) == (int(st[i])+1) or  (int(st[i])) == (int(st[j])-1):
#                 if j==i+1 or j== i-1:
#                     m = True
#     return m
#
# print(adje(inpu))
################################################################
### P - 29 filter all th ip from given string
# str = '''
# M    D    T        Host Addr    Message
# Sep 23 09:24:01 192.168.64.1 CRON[15062]: (root) CMD (LD_PRELOAD="$LD_PRELOAD /usr/lib/libkeepalive.so"
# Sep 23 09:24:20 10.0.0.1     nrpe[15079]: CONN_CHECK_PEER: checking if host is allowed: 18.212.4.63 port 22647
# Sep 23 09:24:20 192.168.64.1 nrpe[15080]: WARNING: my_system() seteuid(0): Operation not permitted to host: 18.212.4.63
# Sep 23 09:25:01 172.163.24.0 CRON[15135]: (root) CMD (command -v debian-sa1 > /
# '''
# import re
# dict = {}
# match = re.findall(r"\d+\s+(\d+\.\d+\.\d+\.\d+)",str)
# print(match)
# for i in match:
#     dict[i] = match.count(i)
#
# print(dict)
################################################################
### P - 30 reduce the string
# inputtt = 'abcabc'
# def reduce(stri):
#     list2 = ['a','b','c']
#     list1 = []
#     for i in stri:
#         list1.append(i)
#     i =0
#     for i in range(len(list1)):
#         if i != len(list1)-1:
#             if ord(list1[i])!= ord(list1[i+1]):
#                 list3 =  [j for j in list2 if (j is not list1[i]) and  (j is not list1[i+1])]
#                 list1.pop(i+1)
#                 list1.pop(i)
#                 list1.insert(i,list3[0])
#                 i +=1
#                 return reduce(list1)
#         else:
#             return list1
# t = reduce(inputtt)
# print(t)
# print(len(t))
################################################################
### P - 31 print the patern given below
# #1----------5
# #2----------4
# #3----------3
# #4----------2
# #5----------1
# def reverse_count():
#     insi= eval(input("Enter the no."))
#     for i in range(insi):
#         print('{0}----------{1}'.format(i+1,insi-i))
# reverse_count()
################################################################
### P - 32 Print next 5 ip address
# from ipaddress import IPv4Network
# import ipaddress
# give_in = IPv4Network('192.168.255.0/24')
# def give_next_five_ip():
#     give_in = ipaddress.IPv4Address('192.168.255.252')
#     for ip in range(int(give_in),int(give_in)+5):
#         print(ipaddress.IPv4Address(ip+1))
#give_next_five_ip()
#######################################################################
### P - 33 output should be ---->{'a': 5, 'b': 6, 'c': {'p': 1, 'q': 2}}
# x = {"a":1,"b":2,"c":{"p":1}}
# y = {"a":5,"b":6,"c":{"q":2}}
#
# f = {}
# # output  = {"a":5,"b":6,"c":{"p":1,"q":2}}
#
# def aba(x,y):
#     for k, v in x.items():
#         if k in y and isinstance(v,dict):
#             y[k] = aba(v,y[k])
#     x.update(y)
#     print(x)
#     return x
#
# j = aba(x,y)
# print(x)























































