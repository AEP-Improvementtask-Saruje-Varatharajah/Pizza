from model.pizza import Pizza
from model.pizza_topping import PizzaTopping
from data_access.pizza_data_access import PizzaDataAccess

class PizzaManager:
    def __init__(self):
        self.__pizza_da = PizzaDataAccess()

    def create_pizza(self, name: str, price: float, size: str, dough_type: str) -> Pizza:
        return self.__pizza_da.create_new_pizza(name, price, size, dough_type)

    def read_pizza(self, pizza_id: int) -> Pizza:
        return self.__pizza_da.read_pizza_by_id(pizza_id)

    def read_all_pizzas(self) -> list[Pizza]:
        return self.__pizza_da.read_all_pizzas()

    def read_pizza_by_name(self, name: str) -> Pizza:
        return self.__pizza_da.read_pizza_by_name(name)

    def read_pizzas_by_toppings(self, required_toppings: list[str]) -> list[Pizza]:
        return self.__pizza_da.read_pizzas_by_toppings(required_toppings)

    def read_toppings_for_pizza(self, pizza_id: int) -> list[str]:
        return self.__pizza_da.read_toppings_for_pizza(pizza_id)

    def update_pizza(self, pizza: Pizza) -> None:
        self.__pizza_da.update_pizza(pizza)

    def delete_pizza(self, pizza: Pizza) -> None:
        self.__pizza_da.delete_pizza(pizza)

    def get_all_pizzas(self) -> list[Pizza]:
        return self.read_all_pizzas()

    def find_pizzas_by_ingredient(self, ingredient: str) -> list[Pizza]:
        return self.read_pizzas_by_toppings([ingredient])

    def find_pizza_by_name(self, name: str) -> Pizza | None:
        return self.read_pizza_by_name(name)

    def display_pizzas(self, pizzas: list[Pizza]) -> None:
        if not pizzas:
            print("Keine Pizzen gefunden.")
            return
        
        for pizza in pizzas:
            print(f"Pizza: {pizza.name}, Preis: {pizza.price:.2f} CHF")
            toppings = self.read_toppings_for_pizza(pizza.pizza_id)
            if toppings:
                print(f"Toppings: {', '.join(toppings)}")
            print("-" * 40)