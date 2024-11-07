class Card:
    card_name: str
    set_name: str
    rarity: str
    color: str
    quantity: int

    def __init__(self, card_name, set_name, rarity, color, quantity):
        self.card_name = card_name
        self.set_name = set_name
        self.rarity = rarity
        self.color = color
        self.quantity = quantity
