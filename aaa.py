### output should be ---->{'a': 5, 'b': 6, 'c': {'p': 1, 'q': 2}}
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