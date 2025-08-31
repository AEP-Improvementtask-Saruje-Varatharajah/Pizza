from __future__ import annotations
from model.pizza import Pizza
from data_access.base_data_access import BaseDataAccess

class PizzaDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_pizza(self, name: str, price: float, size: str, dough_type: str) -> Pizza:
        if name is None:
            raise ValueError("Pizza name is required")
        if price is None:
            raise ValueError("Price is required")
        if size is None:
            raise ValueError("Size is required")
        if dough_type is None:
            raise ValueError("Dough type is required")

        sql = """
        INSERT INTO Pizzen (name, price, size, dough_type, created_at, Toppingtoppingid, Pizzenid, Orderorder_id) 
        VALUES (?, ?, ?, ?, datetime('now'), 1, ?, 1)
        """
        params = (name, price, size, dough_type, 1)
        last_row_id, row_count = self.execute(sql, params)
        return Pizza(last_row_id, name, price, size, dough_type)

    def read_pizza_by_id(self, pizza_id: int) -> Pizza | None:
        if pizza_id is None:
            raise ValueError("Pizza ID is required")

        sql = """
        SELECT id, name, price, size, dough_type FROM Pizzen WHERE id = ?
        """
        params = tuple([pizza_id])
        result = self.fetchone(sql, params)
        if result:
            pizza_id, name, price, size, dough_type = result
            return Pizza(pizza_id, name, price, size, dough_type)
        else:
            return None

    def read_all_pizzas(self) -> list[Pizza]:
        sql = """
        SELECT id, name, price, size, dough_type FROM Pizzen ORDER BY name
        """
        pizzas = self.fetchall(sql)
        return [Pizza(pizza_id, name, price, size, dough_type)
            for pizza_id, name, price, size, dough_type in pizzas]

    def read_pizza_by_name(self, name: str) -> Pizza | None:
        if name is None:
            raise ValueError("Pizza name is required")

        sql = """
        SELECT id, name, price, size, dough_type FROM Pizzen 
        WHERE LOWER(name) = LOWER(?) LIMIT 1
        """
        params = tuple([name])
        result = self.fetchone(sql, params)
        if result:
            pizza_id, name, price, size, dough_type = result
            return Pizza(pizza_id, name, price, size, dough_type)
        else:
            return None

    def read_pizzas_by_toppings(self, required_toppings: list[str]) -> list[Pizza]:
        if not required_toppings:
            return self.read_all_pizzas()

        placeholders = ','.join(['?' for _ in required_toppings])
        
        sql = f"""
        SELECT DISTINCT p.id, p.name, p.price, p.size, p.dough_type 
        FROM Pizzen p
        JOIN Pizza_Topping pt ON p.id = pt.Pizzenid
        JOIN Topping t ON pt.topping_id = t.toppingid
        WHERE LOWER(t.name) IN ({placeholders})
        GROUP BY p.id, p.name, p.price, p.size, p.dough_type
        HAVING COUNT(DISTINCT LOWER(t.name)) = ?
        ORDER BY p.name
        """
        
        params = [topping.lower() for topping in required_toppings] + [len(required_toppings)]
        
        pizzas_data = self.fetchall(sql, params)
        return [Pizza(pizza_id, name, price, size, dough_type)
                for pizza_id, name, price, size, dough_type in pizzas_data]

    def read_toppings_for_pizza(self, pizza_id: int) -> list[str]:
        sql = """
        SELECT t.name FROM Topping t
        JOIN Pizza_Topping pt ON t.toppingid = pt.topping_id
        WHERE pt.Pizzenid = ? AND t.available = 1
        ORDER BY t.name
        """
        params = tuple([pizza_id])
        topping_results = self.fetchall(sql, params)
        return [topping_name for (topping_name,) in topping_results]

    def update_pizza(self, pizza: Pizza) -> None:
        if pizza is None:
            raise ValueError("Pizza cannot be None")

        sql = """
        UPDATE Pizzen SET name = ?, price = ?, size = ?, dough_type = ? WHERE id = ?
        """
        params = tuple([pizza.name, pizza.price, pizza.size, pizza.dough_type, pizza.pizza_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_pizza(self, pizza: Pizza) -> None:
        if pizza is None:
            raise ValueError("Pizza cannot be None")

        sql = """
        DELETE FROM Pizzen WHERE id = ?
        """
        params = tuple([pizza.pizza_id])
        last_row_id, row_count = self.execute(sql, params)