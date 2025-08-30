from __future__ import annotations
from datetime import datetime

class Order:
    def __init__(self, order_id: int, order_time: datetime, total_price: float, 
                 applied_discount: float, voucher_code: str, status: str):
        if not order_id:
            raise ValueError("Order ID is required")
        if not isinstance(order_id, int):
            raise ValueError("Order ID must be an integer")
        if not order_time:
            raise ValueError("Order time is required")
        if not isinstance(order_time, datetime):
            raise ValueError("Order time must be a datetime")
        if not isinstance(total_price, (int, float)):
            raise ValueError("Total price must be a number")
        if total_price < 0:
            raise ValueError("Total price cannot be negative")
        if not isinstance(applied_discount, (int, float)):
            raise ValueError("Applied discount must be a number")
        if applied_discount < 0:
            raise ValueError("Applied discount cannot be negative")
        if not isinstance(voucher_code, str):
            raise ValueError("Voucher code must be a string")
        if not status:
            raise ValueError("Status is required")
        if not isinstance(status, str):
            raise ValueError("Status must be a string")

        self.__order_id: int = order_id
        self.__order_time: datetime = order_time
        self.__total_price: float = float(total_price)
        self.__applied_discount: float = float(applied_discount)
        self.__voucher_code: str = voucher_code
        self.__status: str = status

    def __repr__(self):
        return f"Order(id={self.__order_id!r}, total_price={self.__total_price!r}, status={self.__status!r})"

    @property
    def order_id(self) -> int:
        return self.__order_id

    @property
    def order_time(self) -> datetime:
        return self.__order_time

    @order_time.setter
    def order_time(self, order_time: datetime) -> None:
        if not order_time:
            raise ValueError("Order time is required")
        if not isinstance(order_time, datetime):
            raise ValueError("Order time must be a datetime")
        self.__order_time = order_time

    @property
    def total_price(self) -> float:
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float) -> None:
        if not isinstance(total_price, (int, float)):
            raise ValueError("Total price must be a number")
        if total_price < 0:
            raise ValueError("Total price cannot be negative")
        self.__total_price = float(total_price)

    @property
    def applied_discount(self) -> float:
        return self.__applied_discount

    @applied_discount.setter
    def applied_discount(self, applied_discount: float) -> None:
        if not isinstance(applied_discount, (int, float)):
            raise ValueError("Applied discount must be a number")
        if applied_discount < 0:
            raise ValueError("Applied discount cannot be negative")
        self.__applied_discount = float(applied_discount)

    @property
    def voucher_code(self) -> str:
        return self.__voucher_code

    @voucher_code.setter
    def voucher_code(self, voucher_code: str) -> None:
        if not isinstance(voucher_code, str):
            raise ValueError("Voucher code must be a string")
        self.__voucher_code = voucher_code

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        if not status:
            raise ValueError("Status is required")
        if not isinstance(status, str):
            raise ValueError("Status must be a string")
        self.__status = status