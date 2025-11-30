while True:
    lista_liczb = [int(x) for x in input("Podaj ciąg liczb odzielonych spacją: ").split()]
    if len(lista_liczb) == 0:
        print("Nie wprowadzono żadnych danych")
    else:
        break
print(f"Podany ciąg liczb: {lista_liczb}")
print(f"Liczba podanych wartości: {len(lista_liczb)}")
print(f"Suma: {sum(lista_liczb)}")
print(f"Średnia: {sum(lista_liczb) / len(lista_liczb)}")

dod = 0
ujem = 0
zera = 0

for i in lista_liczb:
    if i > 0:
        dod += 1
    elif i < 0:
        ujem += 1
    else:
        zera += 1

print(f"Dodatnie: {dod}, Ujemne: {ujem}, Zera: {zera}")
print(f"Największa: {max(lista_liczb)}")
print(f"Najmniejsza: {min(lista_liczb)}")








input()