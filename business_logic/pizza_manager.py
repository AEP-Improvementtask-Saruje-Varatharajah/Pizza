from data_access.pizza_data_access import BaseDataAccess

class PizzaManager:
    def __init__(self, db_file):
        self.db = BaseDataAccess(db_file)

    def get_all_pizza(self):
        return self.db.fetchall("SELECT * FROM Pizza")

    def search_by_zutat(self, zutat):
        return self.db.fetchall("SELECT * FROM Pizza WHERE zutaten LIKE ?", ('%' + zutat + '%',))

    def search_by_name(self, name):
        return self.db.fetchone("SELECT * FROM Pizza WHERE name = ?", (name,))

    def calculate_price(self, name, code=None):
        pizza = self.search_by_name(name)
        if pizza is None:
            return None

        # Annahme: Tabelle Pizza hat Spalten (id, name, zutaten, preis)
        _, _, _, base_price = pizza

        if code == "PIZZA10":
            return round(base_price * 0.9, 2)
        else:
            return base_price