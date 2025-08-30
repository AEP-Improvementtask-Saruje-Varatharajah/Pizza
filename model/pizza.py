from __future__ import annotations

class Pizza:
    def __init__(self, pizza_id: int, name: str, price: float, size: str, dough_type: str):
        if not pizza_id:
            raise ValueError("Pizza ID is required")
        if not isinstance(pizza_id, int):
            raise ValueError("Pizza ID must be an integer")
        if not name:
            raise ValueError("Pizza name is required")
        if not isinstance(name, str):
            raise ValueError("Pizza name must be a string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number")
        if not size:
            raise ValueError("Size is required")
        if not isinstance(size, str):
            raise ValueError("Size must be a string")
        if not dough_type:
            raise ValueError("Dough type is required")
        if not isinstance(dough_type, str):
            raise ValueError("Dough type must be a string")

        self.__pizza_id: int = pizza_id
        self.__name: str = name
        self.__price: float = float(price)
        self.__size: str = size
        self.__dough_type: str = dough_type

    def __repr__(self):
        return f"Pizza(id={self.__pizza_id!r}, name={self.__name!r}, price={self.__price!r})"

    @property
    def pizza_id(self) -> int:
        return self.__pizza_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("Pizza name is required")
        if not isinstance(name, str):
            raise ValueError("Pizza name must be a string")
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number")
        self.__price = float(price)

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str) -> None:
        if not size:
            raise ValueError("Size is required")
        if not isinstance(size, str):
            raise ValueError("Size must be a string")
        self.__size = size

    @property
    def dough_type(self) -> str:
        return self.__dough_type

    @dough_type.setter
    def dough_type(self, dough_type: str) -> None:
        if not dough_type:
            raise ValueError("Dough type is required")
        if not isinstance(dough_type, str):
            raise ValueError("Dough type must be a string")
        self.__dough_type = dough_type

    def calculate_price(self, voucher_code: str = None) -> float:
        """Berechnet den Preis mit optionalem Gutscheincode"""
        price = self.__price
        if voucher_code and voucher_code.upper() == "PIZZA10":
            price = price * 0.9
        return price