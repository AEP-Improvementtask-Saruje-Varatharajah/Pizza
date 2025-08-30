from datetime import datetime
from model.order import Order
from data_access.order_data_access import OrderDataAccess

class OrderManager:
    def __init__(self):
        self.__order_da = OrderDataAccess()

    def create_order(self, order_time: datetime, total_price: float, 
                    applied_discount: float, voucher_code: str, status: str) -> Order:
        return self.__order_da.create_new_order(order_time, total_price, applied_discount, voucher_code, status)

    def read_order(self, order_id: int) -> Order:
        return self.__order_da.read_order_by_id(order_id)

    def read_all_orders(self) -> list[Order]:
        return self.__order_da.read_all_orders()

    def read_orders_by_status(self, status: str) -> list[Order]:
        return self.__order_da.read_orders_by_status(status)

    def read_orders_by_voucher_code(self, voucher_code: str) -> list[Order]:
        return self.__order_da.read_orders_by_voucher_code(voucher_code)

    def update_order(self, order: Order) -> None:
        self.__order_da.update_order(order)

    def delete_order(self, order: Order) -> None:
        self.__order_da.delete_order(order)