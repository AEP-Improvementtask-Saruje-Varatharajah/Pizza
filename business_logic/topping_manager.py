from model.topping import Topping
from data_access.topping_data_access import ToppingDataAccess

class ToppingManager:
    def __init__(self):
        self.__topping_da = ToppingDataAccess()

    def create_topping(self, name: str, category: str, extra_price: float, available: bool, pizzen_id: int = None) -> Topping:
        return self.__topping_da.create_new_topping(name, category, extra_price, available, pizzen_id)

    def read_topping(self, topping_id: int) -> Topping:
        return self.__topping_da.read_topping_by_id(topping_id)

    def read_all_toppings(self) -> list[Topping]:
        rows = self.fetchall(
            "SELECT toppingid, name, category, extra_price, available, Pizzenid FROM Topping ORDER BY name"
        )
        return [Topping(r[0], r[1], r[2], float(r[3]), bool(r[4]), r[5]) for r in rows]

    def read_topping_by_name(self, name: str) -> Topping:
        return self.__topping_da.read_topping_by_name(name)

    def read_toppings_by_pizza_id(self, pizzen_id: int) -> list[Topping]:
        return self.__topping_da.read_toppings_by_pizza_id(pizzen_id)

    def update_topping(self, topping: Topping) -> None:
        self.__topping_da.update_topping(topping)

    def delete_topping(self, topping: Topping) -> None:
        self.__topping_da.delete_topping(topping)