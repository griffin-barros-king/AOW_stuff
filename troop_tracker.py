

class troop:

    def __init__(self, name, troops_list, num_needed):
        self.name = name 
        troops_list.sort()
        self.troops_list = troops_list
        self.size = len(troops_list)
        self.num_needed = num_needed
        if self.size < num_needed:
            self.min_level = 0
            return
        self.min_level = troops_list[-(self.num_needed - 1)]
        return
    
    def upgradable(self):
        if self.min_level == 0:
            return f'{self.name} is not upgradable'
        temp_min_level = self.min_level
        possible = list(self.troops_list)
        i = 0
        while i < len(possible) - 1:
            if (possible[i] == possible[i+1]) and (len(possible) > self.num_needed) and (possible[i] < temp_min_level):
                possible[i+1] = possible[i] + 1
                possible = possible[:i] + possible[i+1:]
                possible.sort()
            else:
                i += 1
            if possible.count(temp_min_level) >= self.num_needed: 
                if possible[-1] == self.min_level:
                    if possible.count(self.min_level) >= self.num_needed + 1:
                        possible[-2] = self.min_level + 1
                        possible = possible[:-1]
                    continue
                temp_min_level += 1
                i = 0
        
        return f'{self.name} is upgradable to {possible}'
    
    def combine(self):
        if self.min_level == 0:
            print('failed to combine, not enough troops below min level')
            return
        
        possible = list(self.troops_list)
        i = 0
        while i < len(possible) - 1:
            if (possible[i] == possible[i+1]) and (len(possible) > self.num_needed) and (possible[i] < self.min_level):
                possible[i+1] = possible[i] + 1
                possible = possible[:i] + possible[i+1:]
                possible.sort()
            else:
                i += 1
            if possible.count(self.min_level) >= self.num_needed: 
                if possible[-1] == self.min_level:
                    if possible.count(self.min_level) >= self.num_needed + 1:
                        possible[-2] = self.min_level + 1
                        possible = possible[:-1]
                    continue
                self.min_level += 1
                i = 0
        
        self.troops_list = possible
        return
    
    def UpdateTroop(self, troops_list):
        troops_list.sort()
        self.troops_list = troops_list
        self.size = len(troops_list)
        if self.size < self.num_needed:
            self.min_level = 0
            return
        self.min_level = troops_list[-(self.num_needed - 1)]
        return
    
    def addTroop(self, lvl):
        self.troops_list.append(lvl)
        self.UpdateTroop(self.troops_list)
    
    def __str__(self):
        return f'{self.name}: {self.troops_list} # needed is: {self.num_needed}, min_level: {self.min_level}'



def to_csv(all_troops, filename):
    with open(filename, 'w') as f:
        for troop in all_troops:
            f.write(f'{troop.name},{troop.troops_list},{troop.num_needed}\n')
        f.close()
    return



thing = [1,1,1,2,3,4,5, 5, 5, 5,5,6,6,7, 7]
test = troop('infantry', thing, 3)
print(test)
test.addTroop(3)
print(test)
print(test.upgradable())
test.combine()
print(test)

all_troops = []
