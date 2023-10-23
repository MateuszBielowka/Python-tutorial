
def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x-1)

lista = []
n=0
while n<10:
    lista.append (silnia(n))
    n += 1
print(lista)