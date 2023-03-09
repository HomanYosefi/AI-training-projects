import qrcode

PRODUCT = []
shoping_list = []
shop = {}

def reed_from_database():
    f = open(r"meeting\AI-training-projects\meeting7\store\database.txt", "r")

    for line in f:
        resut = line.split(",")
        my_dict = {"code" : resut[0], "name" : resut[1], "price" : resut[2], "count" : resut[3].strip("\n")}
        PRODUCT.append(my_dict)

    f.close()    

def show_meno():
    print("[1]-- add")
    print("[2]-- edit")
    print("[3]-- remove")
    print("[4]-- search")
    print("[5]-- show list")
    print("[6]-- buy")
    print("[7]-- qrcode mahsol")
    print("[8]-- exit")

def add():
    code = input(" enter code : ")
    name = input(" enter name : ")
    price = input(" enter price : ")
    count = input(" enter count : ")
    new_product = {"code" : code, "name" : name, "price" : price, "count" : count}
    PRODUCT.append(new_product)

def edit():
    show_list()
    user_input = input("enter code for search and edit : ")
    for product in PRODUCT:
        if product["code"] == user_input:
            print("name : ", product["name"], "\tcode : ",
                  product["code"], "\tprice : ", product["price"])
            edits = int(input("[1]-- name edit \n[2]-- price edit \n[3]-- count edit \n enter number list : "))
            if edits == 1:
                name = input(" enter new name : ")
                product["name"] = name
                print("anjam shod")
            elif edits == 2:
                price = input(" enter new price : ")
                product["price"] = price
                print("anjam shod")
            elif edits == 3:
                count = input(" enter new count : ")
                product["count"] = count
                print("anjam shod")
            else:
                print("lotfan dorost vared konid :/")           
            break
    else:
        print(" not found \n\n\n")

def remove():
    user_input = input("enter code for remove : ")
    for product in PRODUCT:
        if product["code"] == user_input:
            product.clear()
            break
    else:
        print(" not found \n\n\n")

def search():
    user_input  = input("enter name or code for search : ")
    for product in PRODUCT:
        if product["code"] == user_input or product["name"] == user_input:
            print("name : ", product["name"], "\tcode : ", 
            product["code"], "\tprice : ", product["price"])
            break
    else:
        print(" not found \n\n\n")    


def show_list():
    for mahsol in PRODUCT:
        print("name : ", mahsol["name"],"\tcode : ", mahsol["code"], "\tprice : ", mahsol["price"])

def buy():
    while True:
        show_list()
        sum = 0
        user_input = input("enter code for buy : ")
        for product in PRODUCT:
            if product["code"] == user_input:
                more = int(input("enter the number of goods : "))
                sum += 1
                if more <= int(product["count"]):
                    box = int(product["count"])
                    box = box - more
                    product["count"] = str(box)
                    cost = str(int(product["price"]) * more)
                    shop = {"code": product["code"], "name": product["name"], "price": cost, "count": str(more)}
                    shoping_list.append(shop)
                    shop = {}

                else:
                    print("the requested number of goods is not available in the store")    
                
        if sum == 0:
            print(" not found \n\n\n")

        edameh = input("do you want to continue ? yes or no ? ")
        if edameh == "no":
            bill = 0
            print(" your bill : ")
            for i in shoping_list:
                bill = int(i["price"]) + bill
                print(i)

            print(" bill all : ", bill)
            break

def qrcodes():
    qr =[]
    user_input = input("enter code for build qrcode : ")
    for product in PRODUCT:
        if product["code"] == user_input:
            qr.append("name : ", product["name"], "\tcode : ", product["code"], "\tprice : ", product["price"])
            img = qrcode.make(qr)
            img.save("mahsol.png")
            break
    else:
        print(" not found \n\n\n")    

def wite_to_database():
    f = open("meeting\AI-training-projects\meeting7\store\database.txt", "w")
    for line in PRODUCT:
        sum = 0
        for i in line:
            f.write(line[i])
            if sum != 3:
                f.write(",")
            sum += 1    
        f.write("\n")
        #f.write(line["code"], ",", line["name"], ",", line["price"], ",",line["count"])

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
        qrcodes()

    elif choice == 8:
        wite_to_database()
        exit(0)

    else:
        print(" mese adam vared kon :/")