### P - Sort the list
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
### P - print the square of whatever is in even position
# l = [2, 4, 6, 8, 10, 12, 14, 16]
#
# l2 = [i*i for i in l[1::2]]
# print(l2)
################################################################
### P - What willbe the output ans- error will come
# l = [1, 2, 3, 4, 5 , 'Deepak']
# l.sort()
################################################################
### P -  requrment is given below
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
### P -  filter all th ip from given string
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
### P -  reduce the string
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
### P -  print the patern given below
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
### P -  Print next 5 ip address
# from ipaddress import IPv4Network
# import ipaddress
# give_in = IPv4Network('192.168.255.0/24')
# def give_next_five_ip():
#     give_in = ipaddress.IPv4Address('192.168.255.252')
#     for ip in range(int(give_in),int(give_in)+5):
#         print(ipaddress.IPv4Address(ip+1))
#give_next_five_ip()
