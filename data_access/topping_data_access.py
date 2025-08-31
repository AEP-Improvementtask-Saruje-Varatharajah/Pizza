from __future__ import annotations
from model.topping import Topping
from data_access.base_data_access import BaseDataAccess

class ToppingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_topping(self, name: str, category: str, extra_price: float, available: bool, pizzen_id: int = None) -> Topping:
        if name is None:
            raise ValueError("Topping name is required")
        if category is None:
            raise ValueError("Category is required")
        if extra_price is None:
            raise ValueError("Extra price is required")
        if available is None:
            raise ValueError("Available status is required")

        sql = """
        INSERT INTO Topping (name, category, extra_price, available, Pizzenid) VALUES (?, ?, ?, ?, ?)
        """
        params = (name, category, extra_price, available, pizzen_id)
        last_row_id, row_count = self.execute(sql, params)
        return Topping(last_row_id, name, category, extra_price, available, pizzen_id)

    def read_topping_by_id(self, topping_id: int) -> Topping | None:
        if topping_id is None:
            raise ValueError("Topping ID is required")

        sql = """
        SELECT toppingid, name, category, extra_price, available, Pizzenid FROM Topping WHERE toppingid = ?
        """
        params = tuple([topping_id])
        result = self.fetchone(sql, params)
        if result:
            toppingid, name, category, extra_price, available, pizzen_id = result
            return Topping(toppingid, name, category, extra_price, bool(available), pizzen_id)
        else:
            return None

    def read_all_toppings(self) -> list[Topping]:
        sql = """
        SELECT toppingid, name, category, extra_price, available, Pizzenid FROM Topping ORDER BY category, name
        """
        toppings = self.fetchall(sql)
        return [Topping(toppingid, name, category, extra_price, bool(available), pizzen_id)
            for toppingid, name, category, extra_price, available, pizzen_id in toppings]

    def read_topping_by_name(self, name: str) -> Topping | None:
        if name is None:
            raise ValueError("Topping name is required")

        sql = """
        SELECT toppingid, name, category, extra_price, available, Pizzenid FROM Topping 
        WHERE LOWER(name) = LOWER(?) LIMIT 1
        """
        params = tuple([name])
        result = self.fetchone(sql, params)
        if result:
            toppingid, name, category, extra_price, available, pizzen_id = result
            return Topping(toppingid, name, category, extra_price, bool(available), pizzen_id)
        else:
            return None

    def read_toppings_by_pizza_id(self, pizzen_id: int) -> list[Topping]:
        if pizzen_id is None:
            raise ValueError("Pizza ID is required")

        sql = """
        SELECT toppingid, name, category, extra_price, available, Pizzenid FROM Topping 
        WHERE Pizzenid = ? ORDER BY category, name
        """
        params = tuple([pizzen_id])
        toppings = self.fetchall(sql, params)
        return [Topping(toppingid, name, category, extra_price, bool(available), pizzen_id)
            for toppingid, name, category, extra_price, available, pizzen_id in toppings]

    def update_topping(self, topping: Topping) -> None:
        if topping is None:
            raise ValueError("Topping cannot be None")

        sql = """
        UPDATE Topping SET name = ?, category = ?, extra_price = ?, available = ?, Pizzenid = ? WHERE toppingid = ?
        """
        params = tuple([topping.name, topping.category, topping.extra_price, topping.available, topping.pizzen_id, topping.topping_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_topping(self, topping: Topping) -> None:
        if topping is None:
            raise ValueError("Topping cannot be None")

        sql = """
        DELETE FROM Topping WHERE toppingid = ?
        """
        params = tuple([topping.topping_id])
        last_row_id, row_count = self.execute(sql, params)