n = int(input("Podaj liczbę elementów listy: "))
x = int(input("Podaj długość ciągów znakowych: "))

# Tworzenie listy ciągów znakowych
my_list = [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(x)) for _ in range(n)]

# Konwersja listy na krotkę
my_tuple = tuple(my_list)

# a) Ilość znaków w liście
print("a) Ilość znaków w liście:", sum(len(s) for s in my_list))

# b) Ilość liter 'k' w liście
print("b) Ilość liter 'k' w liście:", sum(s.count('k') for s in my_list))

# c) Ilość ciągów znaków 'kt' w liście
print("c) Ilość ciągów znaków 'kt' w liście:", sum(s.count('kt') for s in my_list))

# d) Ilość ciągów dłuższych niż s
s = int(input("Podaj wartość s: "))
print("d) Ilość ciągów dłuższych niż s:", sum(len(s) for s in my_list if len(s) > s))