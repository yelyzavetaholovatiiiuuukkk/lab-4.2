a = random.randint(3, 7)
b = random.randint(3, 7)

# Tworzenie zbiorów X i Y
set_X = {random.randint(0, 10) for _ in range(a)}
set_Y = {random.randint(0, 10) for _ in range(b)}

# a) Czy zbiór X zawiera liczbę 5
print("\na) Zbiór X zawiera liczbę 5:", 5 in set_X)

# b) Czy zbiór X jest podzbiorem zbioru Y
print("b) Zbiór X jest podzbiorem zbioru Y:", set_X.issubset(set_Y))

# c) Czy zbiór Y jest podzbiorem zbioru X
print("c) Zbiór Y jest podzbiorem zbioru X:", set_Y.issubset(set_X))

# d) Czy zbiór X jest nadzbiorem zbioru Y
print("d) Zbiór X jest nadzbiorem zbioru Y:", set_X.issuperset(set_Y))

# e) Czy zbiór Y jest nadzbiorem zbioru X
print("e) Zbiór Y jest nadzbiorem zbioru X:", set_Y.issuperset(set_X))

# f) Suma zbiorów X i Y
print("f) Suma zbiorów X i Y:", set_X.union(set_Y))

# g) Różnica zbiorów X i Y
print("g) Różnica zbiorów X i Y:", set_X.difference(set_Y))

# h) Różnica zbiorów Y i X
print("h) Różnica zbiorów Y i X:", set_Y.difference(set_X))

# i) Iloczyn zbiorów X i Y
print("i) Iloczyn zbiorów X i Y:", set_X.intersection(set_Y))

# j) Różnica symetryczna zbiorów X i Y
print("j) Różnica symetryczna zbiorów X i Y:", set_X.symmetric_difference(set_Y))

# k) Wartość najwyższego elementu w obu zbiorach
max_element = max(max(set_X), max(set_Y))
print("k) Wartość najwyższego elementu w obu zbiorach:", max_element)

# l) Usuń ze zbioru X pierwszy element i dołącz go do zbioru Y
first_element_X = set_X.pop()
set_Y.add(first_element_X)

# m) Przekopiuj wszystkie elementy zbioru X do zbioru Y
set_Y.update(set_X)

# n) Wyczyść oba zbiory
set_X.clear()
set_Y.clear()