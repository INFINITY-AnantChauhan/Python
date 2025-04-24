# Example: Program to illustrate class variable to keep count of number of objects created.

class Sample:
    num = 0  # Class variable

    def __init__(self, var):
        Sample.num += 1        # Incrementing the class variable
        self.var = var         # Instance variable

        print("The object value is = ", var)
        print("The count of object created = ", Sample.num)


S1 = Sample(15)
S2 = Sample(35)
S3 = Sample(45)
