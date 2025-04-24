'''Dictionary'''
D={"item":"Apple", "price":100}
print(D["item"])
print(D["price"])

for key, value in D.items():
    print(key, value, sep=" ")
