total = 0
total += 3
print(total)

# def make_averager():
#     count = 0
#     total = 0
#     def averager(new_value):
#         nonlocal count, total
#         count += 1
#         total += new_value
#         return total / count
#     return averager
#
#
# make = make_averager()
# print(make(8))

# def make_averager():
#     series = []
#
#     def averager(new_value):
#         series.append(new_value)
#         print(series)
#         total = sum(series)
#         return total/len(series)
#
#     return averager
# make = make_averager()
# print(int(make(2)))
