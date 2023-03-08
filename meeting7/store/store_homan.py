
PRODUCT = []

def reed_from_database():
    f = open("meeting\AI-training-projects\meeting7\store\database.txt", "r")

    for line in f:
        resut = line.split(",")
        my_dict = {"code" : resut[0], "name" : resut[1], "price" : resut[2], "count" : resut[3]}
        PRODUCT.append(my_dict)

    f.close()    

def show_meno():
    print("[1]-- add")
    print("[2]-- edit")
    print("[3]-- remove")
    print("[4]-- search")
    print("[5]-- show list")
    print("[6]-- buy")
    print("[7]-- exit")

def add():
    code = int(input(" enter code : "))
    name = input(" enter name : ")
    price = int(input(" enter price : "))
    count = int(input(" enter count : "))
    new_product = {"code" : code, "name" : name, "price" : price, "count" : count}
    PRODUCT.append(new_product)

def edit():
    ...

def remove():
    ...

def search():
    ...

def show_list():
    for mahsol in PRODUCT:
        print("name : ", mahsol["name"],"\tcode : ", mahsol["code"], "\tprice : ", mahsol["price"])

def buy():
    ...

def wite_to_database():
    f = open("meeting\AI-training-projects\meeting7\store\database.txt", "w")
    for line in PRODUCT:
        f.write(line["code"], ",", line["name"], ",", line["price"], ",",line["count"])

    f.close()    

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
        wite_to_database()
        exit(0)

    else:
        print(" mese adam vared kon :/")