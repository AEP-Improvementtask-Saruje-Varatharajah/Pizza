from __future__ import annotations
from datetime import datetime
from model.order import Order
from data_access.base_data_access import BaseDataAccess

class OrderDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_order(self, order_time: datetime, total_price: float, 
                        applied_discount: float, voucher_code: str, status: str) -> Order:
        if order_time is None:
            raise ValueError("Order time is required")
        if total_price is None:
            raise ValueError("Total price is required")
        if applied_discount is None:
            raise ValueError("Applied discount is required")
        if voucher_code is None:
            raise ValueError("Voucher code is required")
        if status is None:
            raise ValueError("Status is required")

        sql = """
        INSERT INTO "Order" (order_time, total_price, applied_discount, voucher_code, status) 
        VALUES (?, ?, ?, ?, ?)
        """
        params = (order_time, total_price, applied_discount, voucher_code, status)
        last_row_id, row_count = self.execute(sql, params)
        return Order(last_row_id, order_time, total_price, applied_discount, voucher_code, status)

    def read_order_by_id(self, order_id: int) -> Order | None:
        if order_id is None:
            raise ValueError("Order ID is required")

        sql = """
        SELECT order_id, order_time, total_price, applied_discount, voucher_code, status 
        FROM "Order" WHERE order_id = ?
        """
        params = tuple([order_id])
        result = self.fetchone(sql, params)
        if result:
            order_id, order_time, total_price, applied_discount, voucher_code, status = result
            return Order(order_id, order_time, total_price, applied_discount, voucher_code, status)
        else:
            return None

    def read_all_orders(self) -> list[Order]:
        sql = """
        SELECT order_id, order_time, total_price, applied_discount, voucher_code, status 
        FROM "Order" ORDER BY order_time DESC
        """
        orders = self.fetchall(sql)
        return [Order(order_id, order_time, total_price, applied_discount, voucher_code, status)
            for order_id, order_time, total_price, applied_discount, voucher_code, status in orders]

    def read_orders_by_status(self, status: str) -> list[Order]:
        if status is None:
            raise ValueError("Status is required")

        sql = """
        SELECT order_id, order_time, total_price, applied_discount, voucher_code, status 
        FROM "Order" WHERE status = ? ORDER BY order_time DESC
        """
        params = tuple([status])
        orders = self.fetchall(sql, params)
        return [Order(order_id, order_time, total_price, applied_discount, voucher_code, status)
            for order_id, order_time, total_price, applied_discount, voucher_code, status in orders]

    def read_orders_by_voucher_code(self, voucher_code: str) -> list[Order]:
        if voucher_code is None:
            raise ValueError("Voucher code is required")

        sql = """
        SELECT order_id, order_time, total_price, applied_discount, voucher_code, status 
        FROM "Order" WHERE voucher_code = ? ORDER BY order_time DESC
        """
        params = tuple([voucher_code])
        orders = self.fetchall(sql, params)
        return [Order(order_id, order_time, total_price, applied_discount, voucher_code, status)
            for order_id, order_time, total_price, applied_discount, voucher_code, status in orders]

    def update_order(self, order: Order) -> None:
        if order is None:
            raise ValueError("Order cannot be None")

        sql = """
        UPDATE "Order" SET order_time = ?, total_price = ?, applied_discount = ?, 
        voucher_code = ?, status = ? WHERE order_id = ?
        """
        params = tuple([order.order_time, order.total_price, order.applied_discount, 
                       order.voucher_code, order.status, order.order_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_order(self, order: Order) -> None:
        if order is None:
            raise ValueError("Order cannot be None")

        sql = """
        DELETE FROM "Order" WHERE order_id = ?
        """
        params = tuple([order.order_id])
        last_row_id, row_count = self.execute(sql, params)