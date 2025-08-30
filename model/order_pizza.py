from __future__ import annotations
from model.order import Order
from model.pizza import Pizza

class OrderPizza:
    def __init__(self, order_pizza_id: int, pizza: Pizza, order: Order, quantity: int, unit_price: float):
        if not order_pizza_id:
            raise ValueError("Order pizza ID is required")
        if not isinstance(order_pizza_id, int):
            raise ValueError("Order pizza ID must be an integer")
        if not pizza:
            raise ValueError("Pizza is required")
        if not isinstance(pizza, Pizza):
            raise ValueError("Pizza must be an instance of Pizza")
        if not order:
            raise ValueError("Order is required")
        if not isinstance(order, Order):
            raise ValueError("Order must be an instance of Order")
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not isinstance(unit_price, (int, float)):
            raise ValueError("Unit price must be a number")
        if unit_price < 0:
            raise ValueError("Unit price cannot be negative")

        self.__order_pizza_id: int = order_pizza_id
        self.__pizza: Pizza = pizza
        self.__order: Order = order
        self.__quantity: int = quantity
        self.__unit_price: float = float(unit_price)

    def __repr__(self):
        return f"OrderPizza(id={self.__order_pizza_id!r}, pizza={self.__pizza.name!r}, quantity={self.__quantity!r})"

    @property
    def order_pizza_id(self) -> int:
        return self.__order_pizza_id

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
    def order(self) -> Order:
        return self.__order

    @order.setter
    def order(self, order: Order) -> None:
        if not order:
            raise ValueError("Order is required")
        if not isinstance(order, Order):
            raise ValueError("Order must be an instance of Order")
        self.__order = order

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.__quantity = quantity

    @property
    def unit_price(self) -> float:
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, unit_price: float) -> None:
        if not isinstance(unit_price, (int, float)):
            raise ValueError("Unit price must be a number")
        if unit_price < 0:
            raise ValueError("Unit price cannot be negative")
        self.__unit_price = float(unit_price)

    @property
    def total_price(self) -> float:
        return self.__quantity * self.__unit_price