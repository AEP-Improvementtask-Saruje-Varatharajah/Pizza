def validate_pizza_name(name, available_names):
    return name in available_names

def validate_rabatt_code(code):
    return code.strip().upper() == "PIZZA10"

def get_valid_pizza_input():
    raise NotImplementedError

def get_valid_topping_input():
    raise NotImplementedError

class DiscountInputHelper:
    pass
