

while True:
    eingabe = input("Bitte eine Zahl eingeben: ").strip()

    if not eingabe:
        exit()

    eingabe = int(eingabe)

    if eingabe < 0:
        print("Bitte nur positive Zahlen eingeben")
        #exit()
    elif eingabe == 0 or eingabe == 1:
        #exit()
        pass
    else:

        i = 2
        grossterTeiler = 0
        while i < eingabe:
            teilbar = eingabe % i == 0
            print(i, teilbar)

            if teilbar:
                grossterTeiler = i

            i += 1

        if grossterTeiler:
            print("Zahl ist kein prim!")
            print("Größter Teiler:", grossterTeiler)
        else:
            print("Zahl ist prim!")


