i = 0
while i != "Koniec":
    wiek = int(input("Podaj wiek: "))
    kasa = int(input("Podaj ilość pieniędzy na karcie: "))
    print("Wybierz film z listy: 1, 2")
    film =int(input("::"))
    if film == 1:
        if wiek <= 12 or kasa >= 40:
            print("Możesz wejść")
        else: 
            print("Brak wstępu na film 1, bledne dane")
    elif film == 2:
        if wiek >= 18 and kasa >= 30:
            print("Możesz wejść")
        else: 
            print("Brak wstepu na film 2, bledne dane")
    else:
        print ("Błędna nazwa filmu")
    i = input("Wpisz <<Koniec>> jeśli chcesz zamknąć program lub <<Od nowa>> jeśli chcesz uruchomić program od nowa: ")

