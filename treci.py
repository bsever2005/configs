user_num = int(input("Unesi neki broj: "))

if user_num < 0:
    print("Broj je manji od nula")
elif user_num == 0:
    print("Broj je nula")
elif 0 < user_num <= 100:
    print("Ovo je neki broj između 1 i 100")