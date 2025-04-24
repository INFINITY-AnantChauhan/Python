a = "HELLO I AM ANANT"


for i in range(0, len(a)):
    print(a[i])

print("\n_____________________________________\n")  


for i in range(-1, -len(a) - 1, -1):
    print(a[i])

a = "HELLO I AM ANANT"

print("\n_____________________________________\n")  
for i in range(0, len(a) , 2):
    print(a[i:i+1])
