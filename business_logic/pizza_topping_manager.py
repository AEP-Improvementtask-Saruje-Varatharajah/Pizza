from model.pizza_topping import PizzaTopping
from model.pizza import Pizza
from model.topping import Topping
from data_access.pizza_topping_data_access import PizzaToppingDataAccess

class PizzaToppingManager:
    def __init__(self):
        self.__pizza_topping_da = PizzaToppingDataAccess()

    def create_pizza_topping(self, pizza: Pizza, topping: Topping, is_standard: bool) -> PizzaTopping:
        return self.__pizza_topping_da.create_new_pizza_topping(pizza, topping, is_standard)

    def read_pizza_topping(self, pizza_topping_id: int) -> PizzaTopping:
        return self.__pizza_topping_da.read_pizza_topping_by_id(pizza_topping_id)

    def read_pizza_toppings_by_pizza(self, pizza: Pizza) -> list[PizzaTopping]:
        return self.__pizza_topping_da.read_pizza_toppings_by_pizza(pizza)

    def read_pizza_toppings_by_topping(self, topping: Topping) -> list[PizzaTopping]:
        return self.__pizza_topping_da.read_pizza_toppings_by_topping(topping)

    def read_all_pizza_toppings(self) -> list[PizzaTopping]:
        return self.__pizza_topping_da.read_all_pizza_toppings()

    def update_pizza_topping(self, pizza_topping: PizzaTopping) -> None:
        self.__pizza_topping_da.update_pizza_topping(pizza_topping)

    def delete_pizza_topping(self, pizza_topping: PizzaTopping) -> None:
        self.__pizza_topping_da.delete_pizza_topping(pizza_topping)

    def delete_pizza_topping_by_pizza_and_topping(self, pizza: Pizza, topping: Topping) -> None:
        self.__pizza_topping_da.delete_pizza_topping_by_pizza_and_topping(pizza, topping)

    def add_topping_to_pizza(self, pizza: Pizza, topping: Topping, is_standard: bool = False) -> PizzaTopping:
        return self.create_pizza_topping(pizza, topping, is_standard)

    def remove_topping_from_pizza(self, pizza: Pizza, topping: Topping) -> None:
        self.delete_pizza_topping_by_pizza_and_topping(pizza, topping)