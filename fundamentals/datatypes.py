# TSLD

list_1 = [1,2,3,3,4] # ordered mutable items that allows duplicates which uses [ ] (which is known as array in other languages)
tuple_2 = (1,2,3,3,4) # ordered immutable(cannot be changed)collection of items, it is defined by ( ) "which is called as tuple itself "
set_3 = {1,2,3,3,4} # set is an unordered mutable collection of items does not allow duplicates, defined by { } "which is called as hashset"
dict_4 = {'one': 1, 'two': 2, 'three': 3, 'three': 3 , 'four' : 4 } # dict is mutable collection of key : value pair of items  defined as { } " which is called as hashmap"
    
print(f"{type(list_1)} Value inside is {list_1}")
print(f"{type(tuple_2)} Value inside is {tuple_2}")
print(f"{type(set_3)} Value inside is {set_3}")
print(f"{type(dict_4)} Value inside is {dict_4}")
