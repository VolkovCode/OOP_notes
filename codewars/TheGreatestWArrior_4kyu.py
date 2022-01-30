ranks = ["Pushover", "Novice", "Fighter", 
         "Warrior", "Veteran", "Sage", 
         "Elite", "Conqueror", "Champion", 
         "Master", "Greatest"]


class Warrior():
    def __init__(self):
        self.rank = ranks[0]
        self.level = 1
        self.experience = 100
        self.achievements = []
        self.i = 0
                   
    def rank_set(self, level, l=0, h=10, rank=ranks[0]):
        if level >= 100:
            rank = ranks[-1]
            return rank
        elif level in range(l, h):
            self.i = 0
            return rank
        else:
            l +=10
            h +=10
            self.i += 1
            rank = ranks[self.i]
            return self.rank_set(level, l, h, rank)
    
    def training(self, train_data):
        if train_data[2] <= self.level:
            self.experience += train_data[1]
            if self.experience > 10000:
                self.experience = 10000
            self.level = int(self.experience/100)
            self.rank = self.rank_set(self.level)
            self.achievements.append(train_data[0])
            return train_data[0]
        else:
            return 'Not strong enough'
    
    def battle(self, en_lvl):
        if en_lvl not in range(1, 101):
            return "Invalid level"
        elif self.level-en_lvl == 1:
            self.experience += 5
            if self.experience > 10000:
                self.experience = 10000
            self.level = int(self.experience/100)
            self.rank = self.rank_set(self.level)
            return 'A good fight'
        elif self.level-en_lvl >= 2:
            self.experience += 0
            if self.experience > 10000:
                self.experience = 10000
            self.level = int(self.experience/100)
            self.rank = self.rank_set(self.level)
            return "Easy fight"
        elif self.level == en_lvl:
            self.experience += 10
            if self.experience > 10000:
                self.experience = 10000
            self.level = int(self.experience/100)
            self.rank = self.rank_set(self.level)
            return 'A good fight'
        en_rank = self.rank_set(en_lvl)
        rank_dif = ranks.index(en_rank) - ranks.index(self.rank)
        if rank_dif >= 1 and en_lvl-self.level >= 5:
            return "You've been defeated"
        elif en_lvl-self.level >= 1:
            self.experience += 20 * (en_lvl-self.level) ** 2
            if self.experience > 10000:
                self.experience = 10000
            self.level = int(self.experience/100)
            self.rank = self.rank_set(self.level)
            
            return 'An intense fight'
        
    
        
bruce_lee = Warrior()

bruce_lee.training(["Defeated Chuck Norris", 9000, 1])
for i in [
    bruce_lee.experience, 
    bruce_lee.level, 
    bruce_lee.rank,
    bruce_lee.achievements, 
    bruce_lee.battle(100),
    bruce_lee.experience ]:
    print(i)  
 
