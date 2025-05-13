my_name = "Simon"
user_name = input("შეიყვანე შენი სახელი: ")

if my_name[0].lower() == user_name[0].lower() and my_name[-1].lower() == user_name[-1].lower():
    print(2)
elif my_name[0].lower() == user_name[0].lower() or my_name[-1].lower() == user_name[-1].lower():
    print(1)
else:
    print(0)
