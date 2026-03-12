# list datastructure    
# ordered
# indexed
# changable/mutable

names=["saviour", "john", "joel", "ian"]
names.append("samuel")
names.insert(1, "joy")
print(names)
names[0]="jack"
print(f"My name is {names[0]}")

# tuple datastructure
# ordered
# indexed
# unchangeable/unmutable

country=("kenya", "somalia", "burundi", "ghana")

print(country)
print(f"i was born in {country[2]}")


# set datastructure
# unordered
# no index
cars={"Mazda", "Subaru", "Mercedes", "Toyota", "Nissan"}
print(cars)


# dictionary datastructures
# key value Pair
# mutable
staff={"name":"Saviour", "Age":30, "Salary":"Ksh.500,000"}
print(f"Employee name is {staff["name"]}")
print(f"Employee age is {staff["Age"]}")