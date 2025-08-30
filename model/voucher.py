from __future__ import annotations
from datetime import datetime

class Voucher:
    def __init__(self, voucher_id: int, code: str, discount_percent: float, 
                 valid_until: datetime, activ: bool):
        if not voucher_id:
            raise ValueError("Voucher ID is required")
        if not isinstance(voucher_id, int):
            raise ValueError("Voucher ID must be an integer")
        if not code:
            raise ValueError("Code is required")
        if not isinstance(code, str):
            raise ValueError("Code must be a string")
        if not isinstance(discount_percent, (int, float)):
            raise ValueError("Discount percent must be a number")
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        if not valid_until:
            raise ValueError("Valid until date is required")
        if not isinstance(valid_until, datetime):
            raise ValueError("Valid until must be a datetime")
        if not isinstance(activ, bool):
            raise ValueError("Active must be a boolean")

        self.__voucher_id: int = voucher_id
        self.__code: str = code
        self.__discount_percent: float = float(discount_percent)
        self.__valid_until: datetime = valid_until
        self.__activ: bool = activ

    def __repr__(self):
        return f"Voucher(id={self.__voucher_id!r}, code={self.__code!r}, discount={self.__discount_percent!r}%)"

    @property
    def voucher_id(self) -> int:
        return self.__voucher_id

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str) -> None:
        if not code:
            raise ValueError("Code is required")
        if not isinstance(code, str):
            raise ValueError("Code must be a string")
        self.__code = code

    @property
    def discount_percent(self) -> float:
        return self.__discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent: float) -> None:
        if not isinstance(discount_percent, (int, float)):
            raise ValueError("Discount percent must be a number")
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        self.__discount_percent = float(discount_percent)

    @property
    def valid_until(self) -> datetime:
        return self.__valid_until

    @valid_until.setter
    def valid_until(self, valid_until: datetime) -> None:
        if not valid_until:
            raise ValueError("Valid until date is required")
        if not isinstance(valid_until, datetime):
            raise ValueError("Valid until must be a datetime")
        self.__valid_until = valid_until

    @property
    def activ(self) -> bool:
        return self.__activ

    @activ.setter
    def activ(self, activ: bool) -> None:
        if not isinstance(activ, bool):
            raise ValueError("Active must be a boolean")
        self.__activ = activ

    def is_valid(self) -> bool:
        return self.__activ and self.__valid_until > datetime.now()