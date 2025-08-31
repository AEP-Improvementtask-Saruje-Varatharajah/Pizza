from __future__ import annotations

class Topping:
    def __init__(self, topping_id: int, name: str, category: str,
                 extra_price: float, available: bool, pizzen_id: int | None = None):
        if topping_id is None or not isinstance(topping_id, int):
            raise ValueError("topping_id (int) ist erforderlich")
        if not isinstance(name, str):
            raise ValueError("name (str) ist erforderlich")
        if not isinstance(category, str):
            raise ValueError("category (str) ist erforderlich")
        if not isinstance(extra_price, (int, float)):
            raise ValueError("extra_price muss Zahl sein")
        if not isinstance(available, bool):
            raise ValueError("available (bool) ist erforderlich")

        self.__topping_id = topping_id
        self.__name = name
        self.__category = category
        self.__extra_price = float(extra_price)
        self.__available = available
        self.__pizzen_id = pizzen_id

    def __repr__(self):
        return f"Topping(id={self.__topping_id!r}, name={self.__name!r}, category={self.__category!r})"

    @property
    def topping_id(self) -> int: return self.__topping_id
    @property
    def name(self) -> str: return self.__name
    @property
    def category(self) -> str: return self.__category
    @property
    def extra_price(self) -> float: return self.__extra_price
    @property
    def available(self) -> bool: return self.__available
    @property
    def pizzen_id(self) -> int | None: return self.__pizzen_id
