from enum import Enum
from enum import IntEnum, unique

@unique
class VIP(IntEnum):
    Yellow = 1
    Green = 1
    Black = 3
    Red = 4


class Common(object):
    Yellow = 4


print(VIP(1))
# for v in VIP.__members__.items():
#     print(v)
# print(VIP.Green)
# result = VIP.Yellow is VIP.Yellow
# print(result)


# print(Common.Yellow)
# print(type(VIP.Yellow.name))
# print(type(VIP.Yellow))
# print(VIP["Yellow"])



