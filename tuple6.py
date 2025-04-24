#an unnamed tuple of values assigned to another unnnamed tuple values
(val1,val2,val3)=(1,2,3)
print(val1,val2,val3)
Tup1=(100,200,300)
(val1,val2,val3)=Tup1
print(val1,val2,val3)

(val1,val2,val3)=(2+4,5/3+4,9%6)
print(val1,val2,val3)

#Tuples for returning multiple values and nested tuples
def max_min(vals):
    x = max(vals)
    y = min(vals)
    return (x,y)
vals = (99,98,90,97,89,86,93,82)
(max_marks,min_marks)=max_min(vals)
print(max_marks)
print(min_marks)

Toppers = (("Arav","BSc",92.0),("Chaitanya","BCA",99.0),("


Tup = (1,2,3,4,5,6,7,8)
print(Tup.index(4))

students = ("Bhavya","Era","Falguni","Huma")
index = students.index("Falguni")
print(index)
                                                         
