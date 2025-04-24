#Q1
f1='apple'
print(f1=='Apple')
print(f1!='Apple')
print(f1>'Apple')
print(f1>'apple')
print(f1=='Apple')
print(f1<'Apple')
print(f1<'apple')
print(f1>'applepie')
print(f1<'applepie')
print("____________________________________________________________\n")
#Q2
F1=input("String1")
f2=input("String2")

if(F1<f2):
    print(F1 + " comes before " + f2 + " in Dictionary.")
elif(F1>f2):
    print(F1 + " comes after "+ f2 + " in Dictionary.")
else:
    print(F1 + " and " + f2 + " are same.")
