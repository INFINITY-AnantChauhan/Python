try:
    raise Exception("Hello","world")
except Exception as errorObj:
    print(type(errorObj))
    print(errorObj.args)
    print(errorObj)
    arg1,arg2 = errorObj.args
    print(arg1)
    print(arg2)
