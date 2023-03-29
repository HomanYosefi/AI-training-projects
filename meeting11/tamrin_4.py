def tabe(n):
    if n % 2 != 0:
        for i in range(n):
            for j in range(n):
                print("🟥", end="")
            print()

    else:
        print("number is zoj")


n = int(input("enter number : "))
tabe(n)                    