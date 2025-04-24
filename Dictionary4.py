Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'BTech'}
print("Name is : ", Dict.pop('Name'))    # returns Name
print("Dictionary after popping Name is : ", Dict)
print("Marks is :", Dict.pop('Marks', -1))    # returns default value
print("Dictionary after popping Marks is : ", Dict)
print("Randomly popping any item :", Dict.popitem())
print("Dictionary after random popping is : ", Dict)
print("Aggregate is :", Dict.pop('Aggr'))    # generates error
print("Dictionary after popping Aggregate is : ", Dict)
