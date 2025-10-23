from random import randrange

#=====================================
#  validate_create_card_input_number
#=====================================
def validate_create_card_input_number(rank : str):
    """this function will check if it is a number and if it is in the correct range"""

    try:
        int_rank = int(rank)
        if int_rank not in range(2, 11):
            return False
        return True

    except Exception as e:
        return True

#=====================================
#              create_card
#=====================================
def create_card(rank : str, suite : str) -> dict:
     """will return a card or {} if the input is not correct"""
     match rank:
         case "A" :
             return {"rank" : "A", "suite" : suite, "value" : 14}
         case "K" :
             return {"rank" : "K", "suite" : suite, "value" : 13}
         case "Q" :
             return {"rank" : "Q", "suite" : suite, "value" : 12}
         case "J" :
             return {"rank" : "J", "suite" : suite, "value" : 11}
         case _:

             if not validate_create_card_input_number(rank):
                 return {}

             return {"rank" : rank, "suite" : suite, "value" : int(rank)}


#=====================================
#            compare cards
#=====================================
def compare_cards(p1_card:dict, p2_card:dict) -> str:
    """this function will return the winner - or WAR if it is a tie"""
    if p1_card["value"] > p2_card["value"]:
        return 'p1'
    elif p1_card["value"] < p2_card["value"]:
        return 'p2'

    return "WAR"


#=====================================
#              create deck
#=====================================
def create_deck() -> list[dict]:

    ranks =  ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suites = ["H", "S", "D", "C"]
    cards = []

    for rank in ranks:
        for suite in suites:
            card = create_card(rank, suite)
            cards.append(card)

    return cards


#=====================================
#             handle swap
#=====================================
def handle_swap(index1, index2, deck):

    #this will not swap if the indexes are equal
    if index1 == index2:
        return

    #this will swap between the two indexes
    deck[index1], deck[index2] = deck[index2], deck[index1]


#=====================================
#             shuffle
#=====================================
def shuffle(deck:list[dict]) -> list[dict]:
    """this function manages the card shuffling"""

    for i in range(0, 1000):
        index1 = randrange(0, 52)
        index2 = randrange(0, 52)
        handle_swap(index1, index2, deck)

    return deck










