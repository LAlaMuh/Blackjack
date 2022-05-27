# TODO 1. create class Card to create Deck
# creates every color of a given number as a Card class
def deck_carder(*args, **kwargs):
    if args == int
        g = Card("green", args[0])
        y = Card("yellow", args[0])
        r = Card("red", args[0])
        b = Card("black", args[0])
    else:
        if args[0] == "Ass":
            number = 11
        else:
            number = 10
        g = Card("green", args[0], number)
        y = Card("yellow", args[0], number)
        r = Card("red", args[0], number)
        b = Card("black", args[0], number)

    return g, y, r, b


class Card:
    def __init__(self, *args, **kwargs):
        self.name = f"{args[0]}{args[1]}"
        self.color = args[0]
        self.number = args[-1]

g1, y1, r1, b1 = deck_carder(1)

print(f"{g1.name}:\n  value: {g1.color}\n  name: {g1.number}")
print(f"{y1.name}:\n  value: {y1.color}\n  name: {y1.number}")
print(f"{r1.name}:\n  value: {r1.color}\n  name: {r1.number}")
print(f"{b1.name}:\n  value: {b1.color}\n  name: {b1.number}")