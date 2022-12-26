class Unit:
    def __init__(self, move, fight, strength, defense, attacks,
    wounds, courage):
        self.move = move
        self.fight = fight
        self.strength = strength
        self.defense = defense
        self.attacks = attacks
        self.wounds = wounds
        self.courage = courage

    def toString(self):
        return f'''
    Move: {self.move}'',
    Fight: {self.fight}+,
    Strength: {self.strength},
    Defense: {self.defense},
    Attacks: {self.attacks},
    Wounds: {self.wounds},
    Courage: {self.courage}
        '''
    
class HeroUnit(Unit):
    def __init__(self,move, fight, strength, defense, attacks,
    wounds, courage, might, will, fate):
        super().__init__(move, fight, strength, defense, attacks,
        wounds, courage)
        self.might = might
        self.will = will
        self.fate = fate

    def toString(self):
        tmp = f'''
    Might: {self.might},
    Will: {self.will},
    Fate: {self.fate}
        '''
        return super().toString() + tmp
