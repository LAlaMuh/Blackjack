# TODO 1. create class Card to create Deck
# creates every color of a given number as a Card class
def deck_carder(*args, **kwargs):
    try:
        number = int(args[0])
    except ValueError:
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
        self.name = f"{args[0]}_{args[1]}"
        self.color = args[0]
        self.number = args[-1]


card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ass"]
card_dict = {}
def deck_bd_card_info():
    for x in card_list:
        g, y, r, b = deck_carder(x)
        placeholdi = {
            x:[
            g.name, [g.color, g.number],
            y.name, [y.color, y.number],
            r.name, [r.color, r.number],
            b.name, [b.color, b.number]
        ]
        }
        card_dict[x] = placeholdi[x]
    return card_dict

#
# print(f"{g.name}:\n  value: {g.color}\n  name: {g.number}")
# print(f"{y.name}:\n  value: {y.color}\n  name: {y.number}")
# print(f"{r.name}:\n  value: {r.color}\n  name: {r.number}")
# print(f"{b.name}:\n  value: {b.color}\n  name: {b.number}")