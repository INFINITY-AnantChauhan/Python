str1 = "Hello"
print("str1 is : ", str1)
print("ID of str1 is : ", id(str1))

str2 = "World"
print("str2 is : ", str2)
print("ID of str2 is : ", id(str2))

print("ID of str1 is : ", id(str1))

str1 += str2
print("str1 after concatenation is : ", str1)
print("ID of str1 is : ", id(str1))

str3 = str1
print("str3 = ", str3)
print("ID of str3 is : ", id(str3))
