from register import registartion
from login import login_app


print("Please choose registration or login : \n 1) Registration \n 2) Login")
choice = input("If there is the first time to login my app choose Register : \n")

if choice == "1":
    registartion()
elif choice == "2":
    login_app()
