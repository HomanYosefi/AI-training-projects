from class_film import Film

PRODUCT = []



def reed_from_database_film():
    f = open(r"data_film.txt", "r")

    for line in f:
        resut = line.split(",")
        my_films = Film(resut[0], resut[1], resut[2],
                        resut[3], resut[4], resut[5], resut[6], resut[7], resut[8], resut[9])
        PRODUCT.append(my_films)

    f.close()


def reed_from_database():
    reed_from_database_film()

def search_plus():
    # search time if a < ... and b > ...:
    ...


def add():
    # add where ? 
    # if 1 ... add_film() ...
    ...


def wite_to_database_film():
    f = open("data_film.txt", "w")
    for line in PRODUCT:
        sum = 0
        for i in line:
            f.write(line[i])
            if sum != 9:
                f.write(",")
            sum += 1
        f.write("\n")

    f.close()


def wite_to_database():
    wite_to_database_film()

def show_meno():
    print("[1]-- add")
    print("[2]-- edit")
    print("[3]-- remove")
    print("[4]-- search")
    print("[5]-- show list")
    print("[6]-- buy")
    print("[7]-- download")
    print("[8]-- exit")


print(" welcome to homan store")
print("loading ...")
reed_from_database()
print("data loaded. ")


while True:
    show_meno()
    choice = int(input("enter your choice : "))

    if choice == 1:
        add()

    elif choice == 2:
        edit()

    elif choice == 3:
        remove()

    elif choice == 4:
        search()

    elif choice == 5:
        show_list()

    elif choice == 6:
        buy()

    elif choice == 7:
        qrcodes()

    elif choice == 8:
        wite_to_database()
        exit(0)

    else:
        print(" mese adam vared kon :/")