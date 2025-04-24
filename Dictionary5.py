Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'BTech'}
print(sorted(Dict.keys(), reverse=True)) #Desending
print(sorted(Dict.keys())) #Asending
Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'BTech'}
print("KEYS : ", end=' ')
for key in Dict:
    print(key, end=' ')  # Accessing only keys

print("\nVALUES : ", end=' ')
for val in Dict.values():
    print(val, end=' ')  # Accessing only values

print("\nDICTIONARY : ", end=' ')
for key, val in Dict.items():
    print(key, val, "\t", end=' ')  # Accessing keys and values
