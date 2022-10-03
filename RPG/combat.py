class combat():
    def __init__(self,player_characters,NPCs,interactive_mode,party_xp,party_success,ordered_combatants,player_ply_function,endgame_function):
        self.player_characters = "none"
        self.NPCs = "none"
        self.interactive_mode = False
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = "none"
        self.player_ply_function = "none"
        self.endgame_function = "none"

    def are_all_players_dead(self):
        pass

    def is_combat_over(self):
        pass

    def end_combat(self):
        pass

    def ply(self):
        pass

    def print_stats(self):
        pass

    def turn(self):
        pass

    def start(self):
        pass
    