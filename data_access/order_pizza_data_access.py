from __future__ import annotations
from model.order_pizza import OrderPizza
from model.order import Order
from model.pizza import Pizza
from data_access.base_data_access import BaseDataAccess

class OrderPizzaDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_order_pizza(self, pizza: Pizza, order: Order, quantity: int, unit_price: float) -> OrderPizza:
        if pizza is None:
            raise ValueError("Pizza is required")
        if order is None:
            raise ValueError("Order is required")
        if quantity is None:
            raise ValueError("Quantity is required")
        if unit_price is None:
            raise ValueError("Unit price is required")

        sql = """
        INSERT INTO Order_Pizza (pizza_id, quantity, unit_price, Pizzenid, Orderorder_id) 
        VALUES (?, ?, ?, ?, ?)
        """
        params = (pizza.pizza_id, quantity, unit_price, pizza.pizza_id, order.order_id)
        last_row_id, row_count = self.execute(sql, params)
        return OrderPizza(last_row_id, pizza, order, quantity, unit_price)

    def read_order_pizza_by_id(self, order_pizza_id: int) -> OrderPizza | None:
        if order_pizza_id is None:
            raise ValueError("Order pizza ID is required")

        sql = """
        SELECT op.order_id, op.pizza_id, op.quantity, op.unit_price,
               p.name, p.price, p.size, p.dough_type,
               o.order_time, o.total_price, o.applied_discount, o.voucher_code, o.status
        FROM Order_Pizza op
        JOIN Pizzen p ON op.pizza_id = p.id
        JOIN "Order" o ON op.Orderorder_id = o.order_id
        WHERE op.order_id = ?
        """
        params = tuple([order_pizza_id])
        result = self.fetchone(sql, params)
        if result:
            (order_pizza_id, pizza_id, quantity, unit_price, pizza_name, pizza_price, 
             pizza_size, pizza_dough_type, order_time, total_price, applied_discount, 
             voucher_code, status) = result
            
            pizza = Pizza(pizza_id, pizza_name, pizza_price, pizza_size, pizza_dough_type)
            order = Order(order_pizza_id, order_time, total_price, applied_discount, voucher_code, status)
            return OrderPizza(order_pizza_id, pizza, order, quantity, unit_price)
        else:
            return None

    def read_order_pizzas_by_order(self, order: Order) -> list[OrderPizza]:
        if order is None:
            raise ValueError("Order cannot be None")

        sql = """
        SELECT op.order_id, op.pizza_id, op.quantity, op.unit_price,
               p.name, p.price, p.size, p.dough_type
        FROM Order_Pizza op
        JOIN Pizzen p ON op.pizza_id = p.id
        WHERE op.Orderorder_id = ?
        """
        params = tuple([order.order_id])
        order_pizzas = self.fetchall(sql, params)
        
        result = []
        for order_pizza_id, pizza_id, quantity, unit_price, pizza_name, pizza_price, pizza_size, pizza_dough_type in order_pizzas:
            pizza = Pizza(pizza_id, pizza_name, pizza_price, pizza_size, pizza_dough_type)
            result.append(OrderPizza(order_pizza_id, pizza, order, quantity, unit_price))
        
        return result

    def read_order_pizzas_by_pizza(self, pizza: Pizza) -> list[OrderPizza]:
        if pizza is None:
            raise ValueError("Pizza cannot be None")

        sql = """
        SELECT op.order_id, op.quantity, op.unit_price,
               o.order_id, o.order_time, o.total_price, o.applied_discount, o.voucher_code, o.status
        FROM Order_Pizza op
        JOIN "Order" o ON op.Orderorder_id = o.order_id
        WHERE op.pizza_id = ?
        ORDER BY o.order_time DESC
        """
        params = tuple([pizza.pizza_id])
        order_pizzas = self.fetchall(sql, params)
        
        result = []
        for order_pizza_id, quantity, unit_price, order_id, order_time, total_price, applied_discount, voucher_code, status in order_pizzas:
            order = Order(order_id, order_time, total_price, applied_discount, voucher_code, status)
            result.append(OrderPizza(order_pizza_id, pizza, order, quantity, unit_price))
        
        return result

    def read_all_order_pizzas(self) -> list[OrderPizza]:
        sql = """
        SELECT op.order_id, op.pizza_id, op.quantity, op.unit_price,
               p.name, p.price, p.size, p.dough_type,
               o.order_id, o.order_time, o.total_price, o.applied_discount, o.voucher_code, o.status
        FROM Order_Pizza op
        JOIN Pizzen p ON op.pizza_id = p.id
        JOIN "Order" o ON op.Orderorder_id = o.order_id
        ORDER BY o.order_time DESC
        """
        order_pizzas = self.fetchall(sql)
        
        result = []
        for (order_pizza_id, pizza_id, quantity, unit_price, pizza_name, pizza_price, 
             pizza_size, pizza_dough_type, order_id, order_time, total_price, 
             applied_discount, voucher_code, status) in order_pizzas:
            pizza = Pizza(pizza_id, pizza_name, pizza_price, pizza_size, pizza_dough_type)
            order = Order(order_id, order_time, total_price, applied_discount, voucher_code, status)
            result.append(OrderPizza(order_pizza_id, pizza, order, quantity, unit_price))
        
        return result

    def update_order_pizza(self, order_pizza: OrderPizza) -> None:
        if order_pizza is None:
            raise ValueError("Order pizza cannot be None")

        sql = """
        UPDATE Order_Pizza SET pizza_id = ?, quantity = ?, unit_price = ?, 
        Pizzenid = ?, Orderorder_id = ? WHERE order_id = ?
        """
        params = tuple([order_pizza.pizza.pizza_id, order_pizza.quantity, order_pizza.unit_price,
                       order_pizza.pizza.pizza_id, order_pizza.order.order_id, order_pizza.order_pizza_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_order_pizza(self, order_pizza: OrderPizza) -> None:
        if order_pizza is None:
            raise ValueError("Order pizza cannot be None")

        sql = """
        DELETE FROM Order_Pizza WHERE order_id = ?
        """
        params = tuple([order_pizza.order_pizza_id])
        last_row_id, row_count = self.execute(sql, params)