def run():
    my_list = [1, "Hello", True, 2.5]
    my_dict = {"firstname": "Fernando", "lastname": "Mavec"}

    mega_list = [
        {"firstname": "Fernando", "lastname": "Mavec"},
        {"firstname": "Keanu", "lastname": "Reeves"},
        {"firstname": "Anthony", "lastname": "Bourdain"},
        {"firstname": "Yolan-di", "lastname": "Vi$$er"},
    ]

    mega_dict = {
        "natural_numbers": [1, 2, 3, 4, 5],
        "integer_numbers": [-1, -2, 0, 1, 2],
        "floating_numbers": [1.1, 1.2, 1.3, 1.4, 1.5]
    }

    print("Listas dentro de diccionarios: ")
    for key, value in mega_dict.items():
        print(key, " - ", value)

    print("Diccionarios dentro de listas: ")
    for value in mega_list:
        print(value)



if __name__ == '__main__':
    run()