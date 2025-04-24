print("<<<        WHILE_LOOP        >>>")
count =1
while count <= 5:
    print("The count is:", count)
    count += 1
print("Loop is over")

print("_______________________________________________________________________________________________________")
print("<<<        FOR_LOOP        >>>")
for i in range(1,10,2):
      print( i, end = '@')
      
print("\n_______________________________________________________________________________________________________")
print("<<<        FOR_LOOP_USING_CONTINUE        >>>")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n")

print("_______________________________________________________________________________________________________")
print("<<<        WHILE_LOOP _USING_BREAK       >>>")
count = 0
while True:
    print(count, end=" ")
    count += 1
    if count >= 5:
        break

print("\n_______________________________________________________________________________________________________")
print("<<<        FOR_LOOP_USING_LIST        >>>")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

print("\n_______________________________________________________________________________________________________")
print("<<<        FOR_LOOP_USING_TUPLE       >>>")
numbers = (1, 2, 3)
for number in numbers:
    print(number)

print("\n_______________________________________________________________________________________________________")
print("<<<        FOR_LOOP_USING_STRING        >>>")
text = "hello"
for character in text:
    print(character)

print("\n_______________________________________________________________________________________________________")
print("<<<        FOR_LOOP_USING_DICTIONARY        >>>")
student_grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}
for student, grade in student_grades.items():
    print(f"{student}: {grade}")



print("\n_______________________________________________________________________________________________________")
print("<<<        FOR_LOOP_for_SUM        >>>")
sum=0
for i in range(101):
    sum+=i
print(sum)

print("\n_______________________________________________________________________________________________________")
print("<<<        FOR_LOOP_USING_PASS        >>>")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        pass
    else:
        print(number)
