slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela"}

print(slownik[7])
slownik[8] = False
print(slownik.get(9, "Inny dzień"))

print("\nPętla")
for l in slownik.values():
    print(l)

print("\n--")
print(slownik.pop(1))
print(slownik)