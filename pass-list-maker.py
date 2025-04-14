from itertools import product

str_list: list = []
Pass_list: list = []


def Pass_maker(strings: str, lenght_from: int, lenght_to: int) -> None:

    for i in strings:
        str_list.append(i)

    for i in range(lenght_from, lenght_to + 1):
        Pass_list.extend(product(str_list, repeat=i))

    with open("pass_list.txt", "a") as file:

        for i in Pass_list:

            for n in i:
                file.write(n)

            file.write("\n")


Pass_maker(input("params >>> "), int(input("from >>> ")), int(input("to >>> ")))
