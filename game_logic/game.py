from utils.deck import create_deck, shuffle, compare_cards

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
    game_dict = { "deck" : deck, "player_1" : player1, "player_2" : player2}

    return game_dict


#=============================
#         play round
#=============================
def play_round(p1 : dict, p2 : dict):

    p1_cards = p1['hand']
    p2_cards = p2['hand']

    #this will make sure the the players have cards left
    if len(p1_cards) == 0 or len(p2_cards) == 0:
       print("no cards left in pile exiting game!")
       return

    p1_card = p1_cards.pop(0)
    p2_card = p2_cards.pop(0)

    compare_result = compare_cards(p1_card, p2_card)

    match compare_result:
        case "p1" :
            #this will add to the won pile array - both cards
            #print("player 1 Won this round")
            p1["won_pile"].extend([p1_card, p2_card])
        case "p2":
            p2["won_pile"].extend([p1_card, p2_card])
            #print("player 2 Won this round")
        case "WAR":
            print("WAR TIED OCCURRED")

#=============================
#     draw cards (bonus)
#=============================

#this function is not finished
def draw_cards(cards, amount_of_cards):
    """this function will draw a specified amount of cards from the players cards"""
    drawn_cards = []
    for i in range(0, amount_of_cards):
        drawn_cards.append(cards.pop(0))

    return drawn_cards

#=============================
#     handle tie (bonus)
#=============================

#this function is not finished
def handle_tie_in_game(p1, p2):

   tie_over = False

   while not tie_over:

        #this can happen only if both players have 3 cards
        if len(p1["hand"]) > 4 and len(p2["hand"]) > 4:

            upside_down_cards_p1 = draw_cards(p1["hand"], 3)
            upside_down_cards_p2 = draw_cards(p2["hand"], 3)

            last_cards_p1 = p1["hand"].pop(0)
            last_cards_p2 = p2["hand"].pop(0)

            compare_result = compare_cards(last_cards_p1, last_cards_p2)

            winner_pile = upside_down_cards_p1 + upside_down_cards_p2 + [last_cards_p1, last_cards_p2]

            if compare_result == "p1":
                p1["won_pile"].extend(winner_pile)
                tie_over = True
            elif compare_result == "p2":
                p2["won_pile"].extend(winner_pile)
                tie_over = True

#=============================
#   count suite card bonus
#=============================
def count_suite_card(cards, winning_suite):
    """this function will count the amount of a specific suite"""

    counter = 0

    for card in cards:
        if card["suite"] == winning_suite:
            counter += 1

    return counter

#=============================
#   handle tie result (bonus)
#=============================
def handle_game_result_tie(p1,p2):
    """if there was a tie this function will check according to the suite of the card"""

    current_winning_suite = "H"

    p1_winning_suite_count = count_suite_card(p1["won_pile"], current_winning_suite)
    p2_winning_suite_count = count_suite_card(p2["won_pile"], current_winning_suite)

    if p1_winning_suite_count > p2_winning_suite_count:
        print(f"the winning player is : {p1["name"]}")
    elif p2_winning_suite_count < p2_winning_suite_count:
        print(f"the winning player is : {p2["name"]}")










