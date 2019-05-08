def _val1(name):
    print('this is val1','-->',name)
def _val2(name):
    print('this is val2','-->',name)
def getVal(name):
    if len(name)>5:
        _val1(name)
    else:
        _val2(name)
