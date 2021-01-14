# Tuples

# Immutable, ordered item collection. Order and contents are constant. 

my_tuple = (1, 2, 3)
also_a_tuple = 4, 5, 6
single_item_tuple = (True,)

coordinates = (12, -99, 8, 1,2, 3.0, "integer ex")
x, y, z, *w = coordinates

# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

print(z)
print(w)

#Sets 
# Mutable, unordered, unique item collection.
computers = {"Mac", "Dell", "Lenovo", "Asus"}

ages = {12,22,12}

print(ages) #note that duplicates are not considered
print(computers)

tea_types = {"green", "chai"}
tea_types.add("oolong")
tea_types.add("black")
tea_types.add('matcha')

print(tea_types)

# list
# CSV, can hold any data type, even other lists
my_list = ["Volkswagen", "Ferrari", "Ford", "Tesla"]

some_data = [12, "abc123", True, [1,2,3], ("Windows", "Linux")]
print(len(some_data))
print(some_data[3][1])


# list methods
some_list = [0, 1, 3, 4, 0, 0, 0, 0]

some_list.append(5)                        # add to end of list
another_list = [6, 7]
some_list.extend(another_list)             # append list
some_list.insert(2, 2)                     # at index, insert value
some_list.remove(0)                        # remove given value
some_list.pop(4)                           # at index, remove item
# print(f"Index is {some_list.index(4)}")    # returns index of given value
                                            #count
                                            #sort
                                            #reverse
                                            #copy

some_list = [i for i in some_list if i is not 0]

print(some_list)
 

purchases = [
    33.78,
    5.99,
    532.32,
    3.50,
    1300.00,
    19.98,
    12.21,
    44.44,
    66.00,
    17.38
]
                        #[start:stop(noninclusive):step]
last_five = purchases[-5::]
print(last_five) # if given index is negative, loops to end

# dictionary

person = {
    "name": {
        "first": "Guido", 
        "last": "Vanrossum"
        },
    "age": 64,
    "accomplishments": [
        "Invented Python", 
        "Award for the Advancement of Free Software"
    ],
    (0,2): "tuple as key",
    True: "any immutable works as key"
}

t = "test"

person["quote"] = t
person["name"]["last"] = "van Rossum"
print(person)

