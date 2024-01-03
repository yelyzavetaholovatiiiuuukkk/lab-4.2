shopping_dict = {'chleb': 2.5, 'mleko': 3.0, 'jajka': 4.0}

# Wyświetlenie listy zakupów
print("\nLista zakupów:")
for item, price in shopping_dict.items():
    print(f"{item}: {price} zł")

# Podsumowanie wydatków
total_expenses = sum(shopping_dict.values())
print("Podsumowanie wydatków:", total_expenses, "zł")