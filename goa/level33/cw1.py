names = ["ანა", "ლუკა", "გიორგი", "მარი", "ნიკო"]

name = input("შეიყვანე სახელი: ")
index = int(input("შეიყვანე ინდექსი: "))

if index > len(names):
     print("ერორი: ინდექსი აღემატება სიის ზომას")
else:
    names.insert(index, name)
    print("განახლებული სია:", names)
