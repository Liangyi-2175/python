origin = 0


def go2(pos):

    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


tourist = go2(origin)
print(tourist(2))
print(tourist.__closure__[0].cell_contents)
print(tourist(3))
print(tourist(5))
print(tourist.__closure__[0].cell_contents)
