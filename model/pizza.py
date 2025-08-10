class Pizza:
    def __init__(self, name, zutaten, preis):
        self.name = name
        self.zutaten = zutaten
        self.preis = preis

    def __repr__(self):
        zutaten_str = ", ".join(self.zutaten) if isinstance(self.zutaten, list) else self.zutaten
        return f"{self.name} ({zutaten_str}) - CHF {self.preis:.2f}"