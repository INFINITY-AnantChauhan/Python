import re

print("FIRST")

txt = "The rain in Spain"
x = re.findall("a..m", txt)
print(x)


print("Second")

txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)


print("Third")

txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)


print("Forth")

txt = "hello planet"
x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")


print("Fifth")
txt = "hello planet"
x = re.findall("planet$", txt)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")



print("sixth")

txt= "hello planet"
x=re.findall("he.*o",txt)
print(x)


print("seventh")

txt= "hello planet"
x=re.findall("he.+o",txt)
print(x)


print("eigthth")

txt= "hello planet"
x=re.findall("he.(2)o",txt)
print(x)


print("nineth")

txt= "hello planet"
x=re.findall("he.?o",txt)
print(x)


"""print("tenth")
x=re.findall("falls|stays",t)
print(x)
if x:
    print("yes there is atleast one match")
else:
    print("no match")"""


print("11th")
txt = "The rain in Spain"
x= re.findall("\AThe",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")



print("12th")
txt = "The rain in Spain"
x= re.findall(r"\brain",txt)
print(x)
if x:
    print("Yes, there is at least one match")
else:
    print("no match")


print("13th")
txt = "The rain in Spain"
x= re.findall(r"ain\b",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")



print("14th")
txt = "The rain in Spain"
x= re.findall("\D",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")


print("15th")
txt = "The rain in Spain"
x= re.findall("\s",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")



print("16th")
txt = "The rain in Spain"
x= re.findall("\S",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")


print("17th")
txt = "The rain in Spain"
x= re.findall("\w",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")


print("18th")
txt = "The rain in Spain"
x= re.findall("\W",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")


print("19th")
txt = "The rain in Spain"
x= re.findall("\S",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")


print("20th")
txt = "The rain in Spain"
x= re.findall("Spain\Z",txt)
print(x)
if x:
    print("Yes, there is a match")
else:
    print("no match")
