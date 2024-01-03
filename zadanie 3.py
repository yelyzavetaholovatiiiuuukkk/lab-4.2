electricity_bills = {'styczeń': 200, 'luty': 220, 'marzec': 180, 'kwiecień': 250}

# a) Wartości statystyczne
values = list(electricity_bills.values())
max_value = max(values)
min_value = min(values)
sum_value = sum(values)
average_value = sum_value / len(values)

print("\nMaksymalna wartość:", max_value)
print("Minimalna wartość:", min_value)
print("Suma wartości:", sum_value)
print("Średnia wartość:", average_value)

# b) Sprawdzenie, czy ostatni miesiąc przekroczył średnią
last_month = list(electricity_bills.values())[-1]
if last_month > average_value:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")
