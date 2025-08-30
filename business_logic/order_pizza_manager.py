from model.order_pizza import OrderPizza
from model.order import Order
from model.pizza import Pizza
from data_access.order_pizza_data_access import OrderPizzaDataAccess

class OrderPizzaManager:
    def __init__(self):
        self.__order_pizza_da = OrderPizzaDataAccess()

    def create_order_pizza(self, pizza: Pizza, order: Order, quantity: int, unit_price: float) -> OrderPizza:
        return self.__order_pizza_da.create_new_order_pizza(pizza, order, quantity, unit_price)

    def read_order_pizza(self, order_pizza_id: int) -> OrderPizza:
        return self.__order_pizza_da.read_order_pizza_by_id(order_pizza_id)

    def read_order_pizzas_by_order(self, order: Order) -> list[OrderPizza]:
        return self.__order_pizza_da.read_order_pizzas_by_order(order)

    def read_order_pizzas_by_pizza(self, pizza: Pizza) -> list[OrderPizza]:
        return self.__order_pizza_da.read_order_pizzas_by_pizza(pizza)

    def read_all_order_pizzas(self) -> list[OrderPizza]:
        return self.__order_pizza_da.read_all_order_pizzas()

    def update_order_pizza(self, order_pizza: OrderPizza) -> None:
        self.__order_pizza_da.update_order_pizza(order_pizza)

    def delete_order_pizza(self, order_pizza: OrderPizza) -> None:
        self.__order_pizza_da.delete_order_pizza(order_pizza)