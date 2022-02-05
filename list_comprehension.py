def run():
    squares = []
    for i in range(1, 101):
        if (i % 3 != 0):
            squares.append(i**2)
    print(squares)



def list_comprehension():
    print("Resolver lo anterior con List Comprehension:")
    list_squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(list_squares)


def challenge():
    print("Este es el reto:")
    list_challenge = [i for i in range(1, 101) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(list_challenge)


def optimized_challenge():
    print("Este es el reto optimizando recursos:")
    list_challenge2 = [i for i in range(1, 101) if i % 36 == 0]

    print(list_challenge2)


if __name__ == "__main__":
    run()
    list_comprehension()
    challenge()
    optimized_challenge()