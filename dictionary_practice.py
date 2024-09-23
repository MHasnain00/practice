d = {"Hasnain": 3177,"Asad":3180}
loop = True
while loop:
    search = input("Enter name to search : ").title()
    if search in d:
        print(f"The P.No of {search} is {d[search]} \n")
    else:
        print("Sorry ! Your result not found\n")
        perm = input("Do you want to update your database with this name ? (y/n)\n").lower()
        if perm == "y" or perm == "yes":
            Pn = int(input(f"Enter the P.No for the name {search}: "))
            if Pn > 9999 or Pn < 1:
                print("Your P.No is incorrect.")
            else:
                d[search] = Pn
        else:
            to = input("Ok. You can update your dictionary anytime.\n")
    to = input("Do you want to continue ? (y/n) : ").lower()
    if to=="y":
                loop = True
    else:
        print("OK. Have a great day !!!")
        loop = False
