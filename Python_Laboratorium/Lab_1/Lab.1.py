while True:

    while True:
        try:
            height = float(input("Podaj wzrost w cm: "))
            break
        except ValueError:
            print("To nie jest liczba! Podaj prawidłową wartość")
    while True:
        try:
            weight = float(input("Podaj mase ciala w kg: "))
            break
        except ValueError:
            print("To nie jest liczba! Podaj prawidłową wartość")

    BMI = weight / (height / 100) ** 2

    print(f"Twoje BMI to: {round(BMI, 2)}")
    if BMI < 18.5:
        print(" Masz niedowagę")
    elif BMI >= 18.5 and BMI <= 24.9:
        print("waga prawidłowa")
    elif BMI > 24.9 and BMI < 30:
        print("Masz nadwagę")
    else:
        print("Chorujesz na otyłość")

    kolejny = input("Czy chcesz obliczyć BMI dla kolejnej osoby? t/n \n")
    if kolejny != "t":
        break