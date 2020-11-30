



# list_x = [1, 0, 1, 0, 0, 1]
# list_u = ['a', 'B', 'c', 'F']
# r = filter(lambda x: True if x == 1 else False, list_x)
# s = filter(lambda u: u.isupper(), list_u)
# print(list(r))
# print(list(s))






# from functools import reduce
#
# #连续计算，连续调用lambda
# list_x = [1, 2, 3, 4]
# # list_y = [1, 4, 9, 16, 25, 36]
# r = reduce(lambda x, y: x + y, list_x, 20)
# print(r)




# map
# list_x = [1, 2, 3, 4]
# list_y = [1, 4, 9, 16, 25, 36]
#
#
# r = map(lambda x, y: x*x + y, list_x, list_y)
# print(list(r))