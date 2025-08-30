from __future__ import annotations
from model.pizza import Pizza
from model.topping import Topping

class PizzaTopping:
    def __init__(self, pizza_topping_id: int, pizza: Pizza, topping: Topping, is_standard: bool):
        if not pizza_topping_id:
            raise ValueError("Pizza topping ID is required")
        if not isinstance(pizza_topping_id, int):
            raise ValueError("Pizza topping ID must be an integer")
        if not pizza:
            raise ValueError("Pizza is required")
        if not isinstance(pizza, Pizza):
            raise ValueError("Pizza must be an instance of Pizza")
        if not topping:
            raise ValueError("Topping is required")
        if not isinstance(topping, Topping):
            raise ValueError("Topping must be an instance of Topping")
        if not isinstance(is_standard, bool):
            raise ValueError("Is standard must be a boolean")

        self.__pizza_topping_id: int = pizza_topping_id
        self.__pizza: Pizza = pizza
        self.__topping: Topping = topping
        self.__is_standard: bool = is_standard

    def __repr__(self):
        return f"PizzaTopping(id={self.__pizza_topping_id!r}, pizza={self.__pizza.name!r}, topping={self.__topping.name!r})"

    @property
    def pizza_topping_id(self) -> int:
        return self.__pizza_topping_id

    @property
    def pizza(self) -> Pizza:
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza: Pizza) -> None:
        if not pizza:
            raise ValueError("Pizza is required")
        if not isinstance(pizza, Pizza):
            raise ValueError("Pizza must be an instance of Pizza")
        self.__pizza = pizza

    @property
    def topping(self) -> Topping:
        return self.__topping

    @topping.setter
    def topping(self, topping: Topping) -> None:
        if not topping:
            raise ValueError("Topping is required")
        if not isinstance(topping, Topping):
            raise ValueError("Topping must be an instance of Topping")
        self.__topping = topping

    @property
    def is_standard(self) -> bool:
        return self.__is_standard

    @is_standard.setter
    def is_standard(self, is_standard: bool) -> None:
        if not isinstance(is_standard, bool):
            raise ValueError("Is standard must be a boolean")
        self.__is_standard = is_standard