from game_logic.game import init_game, play_round


if __name__ == "__main__":
   game_data = init_game()
   p1, p2 = game_data["player_1"], game_data["player_2"]
   play_round(p1, p2)



