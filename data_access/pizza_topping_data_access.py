from __future__ import annotations
from model.pizza_topping import PizzaTopping
from model.pizza import Pizza
from data_access.base_data_access import BaseDataAccess

class PizzaToppingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_pizza_topping(self, pizza: Pizza, topping: Topping, is_standard: bool) -> PizzaTopping:
        if pizza is None:
            raise ValueError("Pizza is required")
        if topping is None:
            raise ValueError("Topping is required")
        if is_standard is None:
            raise ValueError("Is standard is required")

        sql = """
        INSERT INTO Pizza_Topping (topping_id, is_standard, Toppingtoppingid, Pizzenid, Orderorder_id) 
        VALUES (?, ?, ?, ?, ?)
        """
        params = (topping.topping_id, is_standard, topping.topping_id, pizza.pizza_id, 1)
        last_row_id, row_count = self.execute(sql, params)
        return PizzaTopping(last_row_id, pizza, topping, is_standard)

    def read_pizza_topping_by_id(self, pizza_topping_id: int) -> PizzaTopping | None:
        if pizza_topping_id is None:
            raise ValueError("Pizza topping ID is required")

        sql = """
        SELECT pt.pizza_id, pt.topping_id, pt.is_standard,
               p.name, p.price, p.size, p.dough_type,
               t.name, t.category, t.extra_price, t.available
        FROM Pizza_Topping pt
        JOIN Pizzen p ON pt.Pizzenid = p.id
        JOIN Topping t ON pt.topping_id = t.toppingid
        WHERE pt.pizza_id = ?
        """
        params = tuple([pizza_topping_id])
        result = self.fetchone(sql, params)
        if result:
            (pizza_topping_id, topping_id, is_standard, pizza_name, pizza_price, pizza_size, 
             pizza_dough_type, topping_name, topping_category, extra_price, available) = result
            
            pizza = Pizza(pizza_topping_id, pizza_name, pizza_price, pizza_size, pizza_dough_type)
            topping = Topping(topping_id, topping_name, topping_category, extra_price, bool(available))
            return PizzaTopping(pizza_topping_id, pizza, topping, bool(is_standard))
        else:
            return None

    def read_pizza_toppings_by_pizza(self, pizza: Pizza) -> list[PizzaTopping]:
        if pizza is None:
            raise ValueError("Pizza cannot be None")

        sql = """
        SELECT pt.pizza_id, pt.topping_id, pt.is_standard,
               t.name, t.category, t.extra_price, t.available
        FROM Pizza_Topping pt
        JOIN Topping t ON pt.topping_id = t.toppingid
        WHERE pt.Pizzenid = ?
        """
        params = tuple([pizza.pizza_id])
        pizza_toppings = self.fetchall(sql, params)
        
        result = []
        for pizza_topping_id, topping_id, is_standard, topping_name, topping_category, extra_price, available in pizza_toppings:
            topping = Topping(topping_id, topping_name, topping_category, extra_price, bool(available))
            result.append(PizzaTopping(pizza_topping_id, pizza, topping, bool(is_standard)))
        
        return result

    def read_pizza_toppings_by_topping(self, topping: Topping) -> list[PizzaTopping]:
        if topping is None:
            raise ValueError("Topping cannot be None")

        sql = """
        SELECT pt.pizza_id, pt.is_standard,
               p.id, p.name, p.price, p.size, p.dough_type
        FROM Pizza_Topping pt
        JOIN Pizzen p ON pt.Pizzenid = p.id
        WHERE pt.topping_id = ?
        """
        params = tuple([topping.topping_id])
        pizza_toppings = self.fetchall(sql, params)
        
        result = []
        for pizza_topping_id, is_standard, pizza_id, pizza_name, pizza_price, pizza_size, pizza_dough_type in pizza_toppings:
            pizza = Pizza(pizza_id, pizza_name, pizza_price, pizza_size, pizza_dough_type)
            result.append(PizzaTopping(pizza_topping_id, pizza, topping, bool(is_standard)))
        
        return result

    def read_all_pizza_toppings(self) -> list[PizzaTopping]:
        sql = """
        SELECT pt.pizza_id, pt.topping_id, pt.is_standard,
               p.id, p.name, p.price, p.size, p.dough_type,
               t.name, t.category, t.extra_price, t.available
        FROM Pizza_Topping pt
        JOIN Pizzen p ON pt.Pizzenid = p.id
        JOIN Topping t ON pt.topping_id = t.toppingid
        """
        pizza_toppings = self.fetchall(sql)
        
        result = []
        for (pizza_topping_id, topping_id, is_standard, pizza_id, pizza_name, pizza_price, 
             pizza_size, pizza_dough_type, topping_name, topping_category, extra_price, available) in pizza_toppings:
            pizza = Pizza(pizza_id, pizza_name, pizza_price, pizza_size, pizza_dough_type)
            topping = Topping(topping_id, topping_name, topping_category, extra_price, bool(available))
            result.append(PizzaTopping(pizza_topping_id, pizza, topping, bool(is_standard)))
        
        return result

    def update_pizza_topping(self, pizza_topping: PizzaTopping) -> None:
        if pizza_topping is None:
            raise ValueError("Pizza topping cannot be None")

        sql = """
        UPDATE Pizza_Topping SET topping_id = ?, is_standard = ?, 
        Toppingtoppingid = ?, Pizzenid = ? WHERE pizza_id = ?
        """
        params = tuple([pizza_topping.topping.topping_id, pizza_topping.is_standard,
                       pizza_topping.topping.topping_id, pizza_topping.pizza.pizza_id, 
                       pizza_topping.pizza_topping_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_pizza_topping(self, pizza_topping: PizzaTopping) -> None:
        if pizza_topping is None:
            raise ValueError("Pizza topping cannot be None")

        sql = """
        DELETE FROM Pizza_Topping WHERE pizza_id = ?
        """
        params = tuple([pizza_topping.pizza_topping_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_pizza_topping_by_pizza_and_topping(self, pizza: Pizza, topping: Topping) -> None:
        if pizza is None:
            raise ValueError("Pizza cannot be None")
        if topping is None:
            raise ValueError("Topping cannot be None")

        sql = """
        DELETE FROM Pizza_Topping WHERE Pizzenid = ? AND topping_id = ?
        """
        params = tuple([pizza.pizza_id, topping.topping_id])
        last_row_id, row_count = self.execute(sql, params)