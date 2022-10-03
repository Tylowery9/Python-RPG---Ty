class Character():
    def __init__(self,name,strength,intelligence,wisdom,dexterity,constitution,charisma,race,Class,level,hit_point_max,movement,armor,xp,type,current_weapon,current_armor):
        self.name = "player"
        self.strength = 0
        self.intelligence = 0
        self. wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.race = "no race"
        self.Class = "no class"
        self.level = 0
        self.hit_point_max = 0
        self.movement = 0
        self.armor = 0
        self.xp = 0
        self.type = "no type"
        self.current_weapon = "none"
        self.current_armor = "none"



    def set_current_weapon(self):
        pass

    def roll_to_hit(self):
        pass

    def roll_for_damage(self):
        pass

    def get_ac(self):
        pass

    def get_movement(self):
        pass

    def get_ability_bonuses(self):
        pass
