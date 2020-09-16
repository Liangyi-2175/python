
def testao(*args,**kwargs):
    return args, kwargs

test=testao(5,9,5,6,7,a=4,b=5)
print(test)