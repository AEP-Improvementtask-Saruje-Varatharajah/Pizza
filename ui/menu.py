from business_logic.pizza_manager import PizzaManager

def main_menu():
    db_file = "./Pizza/database/pizza.db"
    manager = PizzaManager(db_file)

    while True:
        print("\n--- Pizza Menü ---")
        print("1: Alle Pizzen anzeigen")
        print("2: Pizza nach Zutat suchen")
        print("3: Pizza nach Namen suchen")
        print("4: Preis berechnen (inkl. Rabattcode)")
        print("0: Programm beenden")

        auswahl = input("Was möchtest du tun? (0-4): ").strip()

        if auswahl == "1":
            alle = manager.get_all_pizza()
            for pizza in alle:
                print(pizza)

        elif auswahl == "2":
            zutat = input("Nach welcher Zutat suchst du? ").strip()
            result = manager.search_by_zutat(zutat)
            for pizza in result:
                print(pizza)

        elif auswahl == "3":
            name = input("Wie heisst die Pizza? ").strip()
            pizza = manager.search_by_name(name)
            if pizza:
                print(pizza)
            else:
                print("Pizza nicht gefunden.")

        elif auswahl == "4":
            name = input("Pizza-Name: ").strip()
            code = input("Gutscheincode (optional): ").strip()
            price = manager.calculate_price(name, code if code else None)
            if price is not None:
                print(f"Preis: CHF {price:.2f}")
            else:
                print("Pizza nicht gefunden.")

        elif auswahl == "0":
            print("Tschüss!")
            break

        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")

if __name__ == "__main__":
    main_menu()