def validate_pizza_name(name, available_names):
      Prüft, ob der eingegebene Pizza-Name in der Liste verfügbarer Namen enthalten ist.
    return name in available_names


def validate_rabatt_code(code):

    Prüft, ob der eingegebene Gutscheincode gültig ist.
    Ignoriert Gross-/Kleinschreibung und Leerzeichen.
    """
    return code.strip().upper() == "PIZZA10"