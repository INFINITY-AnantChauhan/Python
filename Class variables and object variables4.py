class ABC():
    def __init__(self,var):
        self.var=var
    def dislay(self):
        print("VAR IS=",self.var)
obj=ABC(10)
obj.display()
ptint("Check if object has attribute var   ",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',50)
print("after setting var ",obj.var)
setattr(obj,'count',10)
print(obj.count)
delattr(obj,'var')
print(obj.var)
