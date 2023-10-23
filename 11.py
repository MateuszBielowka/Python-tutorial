plik = open("test.txt", "a")
if plik.writable():
    plik.write(input("wprowadź tekst: ") + "\n")
plik.close()

plik = open("test.txt", "r")
if plik.readable:
    print("Zawartość pliku")
    tekst = plik.readlines()
    print(tekst)
    for l in tekst:
        print(l)