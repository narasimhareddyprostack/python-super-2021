class Error(Exception):
    """ Test 1 """
    pass
class FirstException(Error):
    """ Test 2"""
    pass
class SecondException(Error):
    """ Test 2"""
    pass

try:
    print(10/0)
except:
    raise FirstException("Please Handle Properly")

    

        