num1=10
print("Global variable num1 = ", num1)
def fun(num2):
    print("In function - Local variable num2 = ", num2)
    num3 = 30
    print("In function - Local variable num3 = ", num3)

fun(20)
print("num1 Again = ", num1)
print("num3 outside function = ", mum3)
