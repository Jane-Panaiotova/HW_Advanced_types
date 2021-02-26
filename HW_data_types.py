#1 define the id of next variables:
int_a = 55
print(id(int_a))
str_b = 'cursor'
print(id(str_b))
set_c = {1, 2, 3}
print(id(set_c))
lst_d = [1, 2, 3]
print(id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))

#2 append 4 and 5 to the lst_d and define the id one more time
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d))

# расширение списка методом .extend
lst_d1 = [1, 2, 3]
a1 = [4, 5]
lst_d1.extend(a1)
print(lst_d1)

#3 define the type of each object from step 1
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

#4 Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

#String formatting:
#5 With .format and curly braces.
str_1 = "Anna has {} apples and {} peaches.".format(8, 3)
print(str_1)

#6 By passing index numbers into the curly braces.
str_2 = "Anna has {1} apples and {0} peaches.".format(8, 3)
print(str_2)

#7 By using keyword arguments into the curly braces.
apples = 1
peaches = 2
str_4 = "Anna has {apples} apples and {peaches} peaches.".format(apples=apples, peaches=peaches)
print(str_4)

#8 With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {0:5} apples and {1:3} peaches.'.format(5, 3))

#9 With f-strings and variables.
apples = 6
peaches = 4
str_1 = f"Anna has {apples} apples and {peaches} peaches."
print(str_1)

#10 With % operator:
apples = 7
peaches = 10
print("Anna has %s apples and %d peaches." % (apples, peaches))

#11 With variable substitutions by name (hint: by using dict):
apples = 2
peaches = 5
using_dict = {"a": apples, "p": peaches}
print("Anna has %(a)s apples and %(p)s peaches" % using_dict)



#Comprehensions
# 12 Convert (1) to list comprehension:
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num**2)
    else:
        lst.append(num**4)
print(lst)

lst_comprehensions1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comprehensions1)

# 13. Convert (2) to regular for with if-else
lst_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

lst_comprehension2 = []
for num in range(10):
    if num % 2 == 0:
        lst_comprehension2.append(num // 2)
    else:
        lst_comprehension2.append(num*10)
print(lst_comprehension2)

# 14. Convert (3) to dict comprehension.
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

dict_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension)

# 15*. Convert (4) to dict comprehension.
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)

dict_comprehension2 = {num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension2)

# 16 Convert (5) to regular for with if.
dict_comprehension3 = {x: x**3 for x in range(10) if x**3 % 4 == 0}
dict_comprehension3 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension3[x] = x**3
print(dict_comprehension3)

# 17*. Convert (6) to regular for with if-else:
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
dict_comprehension4 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension4[x] = x**3
    else:
        dict_comprehension4[x] = x
print(dict_comprehension4)

# 18. Convert (7) to lambda function
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

foo1 = lambda x, y: x if x < y else y

# 19*. Convert (8) to regular function
# foo = lambda x, y, z: z if y < x and x > z else y

x = 2
y = 3
z = 6

def foo2(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo2(x,y, z))


#20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)

#21. Sort lst_to_sort from max to min
#lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort2 = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort2.sort(key=None, reverse=True)
print(lst_to_sort2)

#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort3 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort3)

#23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_D = list(map(pow, list_A, list_B))
print(list_D)

#24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
r = reduce(lambda x, y: x + y, lst_to_sort)
print(r)


#25 Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort4 = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(lst_to_sort4)

#26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
c = list(filter(lambda val: (val < 0), b))
print(c)

#27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
l = list(filter(lambda val: val in list_1, list_2))
print(l)


