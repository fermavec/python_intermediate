from functools import reduce

def funcion(func):
    func()

def func1():
    print("Soy una funcion dentro de otra funcion")

def func2():
    print("Hahaha Yo tambien")

funcion(func1)
funcion(func2)

my_list = [1,10,5,8,4,3,2,7,9,6]
#filter
filtered_list = list(filter(lambda x: x%2 == 0, my_list))
print(filtered_list)
#Map
mapped_list = list(map(lambda x: x**2, my_list))
print(mapped_list)
#Reduce
reduced_list = reduce(lambda a, b: a * b, my_list)
print(reduced_list)