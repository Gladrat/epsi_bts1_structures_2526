# list

l = []
print(type(l))

# ARRAY
    # collection
    # arrangés par un index (commence à 0)
    # immuable (taille fixe)
    # unidimensionnel
    # type fixe

# 1) une liste de taille fixe remplie de valeurs nulles

# s = 5
# t = [None] * s

# print(t)

# def append(arr, i, val):
#     if i <= len(arr):
#         arr[i] = val
#     else:
#         raise IndexError
    
# append(t, 1, "Jules")
# append(t, 2, True)
# append(t, 3, 42)

# print(t)

import array

arr_i = array.array("i", [1, 2, 3, 4])

string = "Coucou"
string2 = "Coucou"
print(id(string))

string += "!"
string3 = string
print(id(string))

string += "!!!!"
print(id(string3))

print(id(string)) 

print(id(12))
i, j = 12, 12
print(id(i), id(j))