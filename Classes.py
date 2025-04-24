#Object Oriented Programming
"""left
class ABC:"""

class Sample:
    #class variables
    x,y = 10,20
S =  Sample()
print("value of x = ",S.x)
print("value of y = ",S.y)
print("Value of x and y = ",S.x+S.y)

#Data Abstraction and Data Hiding
"""Data abstraction is a programming technique that simplifies
complex systems by hiding unnecessary details and presenting only
essential information to the user, focusing on what data is and how
it's used, rather than how it's implemented. """
print("_______________________________________________________")


#Class Method and Self Argument
class ABC:
    var = 10
    def display(self):
        print("In class method.....")
obj = ABC()
print(obj.var)
obj.display()

print("\nEG.2")
class Student:
    mark1,mark2,mark3 = 45,91,71
    def process(self):
        sum = Student.mark1+Student.mark2+Student.mark3
        avg = sum/3
        print(sum)
        print(avg)
        return
S = Student()
S.process()

print("\nEG.3")
class Odd_Even:
    even = 0
    def check(self,num):
        if(num%2==0):
            print(num,"is even")
        else:
            print(num,"is odd")
n = Odd_Even()
x = int(input("Enter a number"))
n.check(x)
print("_______________________________________________________")
#constructor
class ABCD():
    def __init__(self,val):
        print("In class method.....")
        self.val = val
        print("The value is ",val)
obj = ABCD(10)

print("\nEG.2")
class Sample:
    def __init__(self,num):
        print("Constructor of the sample")
        self.num = num
        print("The value is : ",num)

S = Sample(10)
