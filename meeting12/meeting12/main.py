from class_film import Film
from class_actor import Actor
from class_mdia import Media
from class_series import Series

PRODUCT = []



def reed_from_database_film():
    f = open(r"data_film.txt", "r")

    for line in f:
        resut = line.split(",")
        my_films = Film(resut[0], resut[1], resut[2],
                        resut[3], resut[4], resut[5], resut[6], resut[7], resut[8], resut[9], resut[10])
        PRODUCT.append(my_films)

    f.close()


def reed_from_database_series():
    f = open(r"data_series.txt", "r")

    for line in f:
        resut = line.split(",")
        my_series = Film(resut[0], resut[1], resut[2],
                        resut[3], resut[4], resut[5], resut[6], resut[7])
        PRODUCT.append(my_series)

    f.close()


def reed_from_database_documentary():
    f = open(r"data_duc.txt", "r")

    for line in f:
        resut = line.split(",")
        my_duc = Film(resut[0], resut[1], resut[2],
                        resut[3], resut[4], resut[5], resut[6], resut[7])
        PRODUCT.append(my_duc)

    f.close()


def reed_from_database():
    reed_from_database_film()
    reed_from_database_series()
    reed_from_database_documentary()

def search():
    while True:
        print("\n\n\n[1]-- search name ")
        print("[2]-- search time n---m ")
        print("[3]-- search kargardan")
        inp_list = int(input("\n enter number of list : "))
        if inp_list == 1:
            name_for_search = input("enter name media for search : ")
            for med in PRODUCT:
                med.search_name()

            break
        elif inp_list == 2:
            time_1 = int(input("enter time 1 : "))
            time_2 = int(input("enter time 2 : "))
            for med in PRODUCT:
                med.search_plus(time_1, time_2)

            break
        elif inp_list == 3:
            name_for_search = input("enter name kargardan for search : ")
            for med in PRODUCT:
                med.search_kargardan()

            break
        else:    
            print("az add hay list entekhab kon :|")    

def add():
    name = input(" enter name media : ")
    kargardan = input("enter name kargardan : ")
    imdb_score = input("enter imdb score : ")
    url = input("enter url : ")
    
    print("[1]-- film")
    print("[2]-- clip")
    print("[3]-- documentry")
    print("[4]-- series")
    number_list = int(input("enter number of list : "))
    if number_list == 1:
        sub_media = "film"
    elif number_list == 2:
        sub_media = "clip"

    # add where ? 
    # if 1 ... add_film() ...
    ...


def wite_to_database_film(med):
    f = open("data_film.txt", "w")
    sum = 0
    for i in med:
        f.write(i)
        if sum != 10:
            f.write(",")
    f.write("\n")

    f.close()


def wite_to_database_series(med):
    f = open("data_series.txt", "w")
    sum = 0
    for i in med:
        f.write(i)
        if sum != 7:
            f.write(",")
    f.write("\n")

    f.close()


def wite_to_database_duc(med):
    f = open("data_duc.txt", "w")
    sum = 0
    for i in med:
        f.write(i)
        if sum != 7:
            f.write(",")
    f.write("\n")

    f.close()

def wite_to_database():
    for med in PRODUCT:
        if med[0] == "film":
            wite_to_database_film(med)
        elif med[0] == "series":
            wite_to_database_series(med)   
        elif med[0] == "documentary":
            wite_to_database_duc(med)


def edit():
    ...


def remove():
    ...


def show_list():
    for vidio in PRODUCT:
        vidio.show_info()

def show_meno():
    print("[1]-- add")
    print("[2]-- edit")
    print("[3]-- remove")
    print("[4]-- search")
    print("[5]-- show all media")
    print("[6]-- buy")
    print("[7]-- download")
    print("[8]-- exit (save edits)")


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
        ...

    elif choice == 7:
        ...

    elif choice == 8:
        wite_to_database()
        exit(0)

    else:
        print(" mese adam vared kon :/")