from utils.deck import create_deck, shuffle

#=============================
#        create player
#=============================
def create_player(name=None):

    hand = []
    won_pile = []

    if not name:
        name = "AI"

    return {"name" : name, "hand" : hand, "won_pile" : []}


# =============================
#       get part of deck
# =============================
def get_part_of_deck(deck, start, end):

    partial_deck = []

    for index in range(start, end):
         partial_deck.append(deck[index])

    return partial_deck


#=============================
#       split deck
#=============================
def split_deck(deck):
    middle_of_deck = len(deck) // 2
    top_half = get_part_of_deck(deck, 0, middle_of_deck)
    bottom_half = get_part_of_deck(deck, middle_of_deck, len(deck))

    return top_half, bottom_half

#=============================
#         init game
#=============================
def init_game() -> dict:

    player1 = create_player()
    player2 = create_player("Yossi Kovan")

    #this is the non shuffled deck
    deck = create_deck()

    #this returns the shuffled deck
    deck = shuffle(deck)

    #this will split the deck and place the values into each of the player hands accordingly
    #this first player gets the top half and the second the bottom half
    player1["hand"],  player2["hand"] = split_deck(deck)

    #this returns the game dict
    return {
        "deck" : deck,
        "player_1" : player1,
        "player2" : player2
    }


def play_round(p1 : dict, p2 : dict):
    pass




