import random


print("kazanmak için"
      + "tas vs kait -> kait kazanir \n"
      + "tas vs makas -> tas kazanir \n"
      + "kait vs makas -> makas kazanir \n")

while True:

    print("seçebileceklerin \n 1 - tas \n 2 - kait \n 3 - makas \n")

    
    choice = int(input("seçimini gir:"))

    while choice > 3 or choice < 1:
        choice = int(input('lütfen adam akıllı seçim gir: '))

    if choice == 1:
        choice_name = 'tas'
    elif choice == 2:
        choice_name = 'kait'
    else:
        choice_name = 'makas'

    print('seçimin:', choice_name)
    print("şimdi de bilgisayar seçiyor...")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'tas'
    elif comp_choice == 2:
        comp_choice_name = 'kait'
    else:
        comp_choice_name = 'makas'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    # Determine the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = 'kait'
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
        result = 'tas'
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = 'makas'

    # Print the result
    if result == "DRAW":
        print("berabere")
    elif result == choice_name:
        print("kullanıcı kazandı(üstün)")
    else:
        print("bilgisayar kazandı(dünyayı ele geçirecek)")

    