def run():
    cube_dict = {}
    for i in range(1, 101):
        cube_dict[i] = i**3
    print(cube_dict)

def not_cube():
    print("No divisibles")
    not_cube_dict = {}
    for i in range(1, 101):
        if(i % 3 != 0):
            not_cube_dict[i] = i**3
    print(not_cube_dict)

def dict_comprehension():
    print("Dict Comprehension: ")
    dict_comp = {i: i**3 for i in range(1, 101) if i % 3 != 0 }
    print(dict_comp)


def challenge():
    print("Reto: ")
    challenge_dict = {i: i**.5 for i in range(1, 101)}
    print(challenge_dict)


if __name__ == "__main__":
    run()
    not_cube()
    dict_comprehension()
    challenge()