###P- Replace somthing from given input
# s1 = 'how are you'
# s1 = s1.replace('how', 'who')
# print(s1)
#
# list = ['where are you']
# list = list[0].replace('where','who')
# print(list)
######################################################
###P- output should be ----->[4, 5, 6, 1, 2, 3]
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
###P- output should be ----->{'sw1': 'vlan1', 'sw2': 'vlan2', 'sw3': 'vlan3'}
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
###P- list all the files in current directory
# import os
# output = os.listdir()
# print(output)
# print(len(output))

######################################################
###P- find the square of each element
# listt = [1,2,3,4,5,6]
# liis1 = [x*x for x in listt]
# print(liis1)

