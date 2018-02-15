

import random
class WordSearch():
    def __init__(self, searchWords, maxX = 20, maxY = 20):
        self.maxX = maxX
        self.maxY = maxY
        self.grid = [] # grid is a list of list of strings (characters)
        testWords = ['superhero', 'gugu','gaga','blah','vodka']
        searchWords = searchWords.split(",")
        if searchWords == ['']:
            searchWords = testWords
        self.searchWords = searchWords 
        for row in range(0, self.maxY):
            self.grid.append([])
            for column in range(0, self.maxX):
                self.grid[row].append('*')
        for word in searchWords:
            DIR = random.randint(0, 7)
        while not self.engrave(word, self.DONTCARE , self.DONTCARE , DIR):
            pass
        self.obfusticate()
                   
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL = 2
    REVHORIZONTAL = 3
    REVVERTICAL = 4
    REVDIAGONAL = 5
    REVFLIPDIAGONA = 6
    FLIPDIAGONAL = 7
    DONTCARE = -100
    def engrave(self,word, x, y, direction):
        if len(word) == 0:
            return True
        # word has length > 0
        # check if we need to choose random pos
        if x == self.DONTCARE or y == self.DONTCARE: # cannot have one random, one fixed
            while True:
                y = random.randint(0, self.maxY - 1)
                x = random.randint(0, self.maxX - 1)
                if self.grid[y][x] == '*':
                    break
        # check if x & y are valid            
        if x == self.maxX or x < 0:
            return False
        if y == self.maxY or y < 0:
            return False
        if not (self.grid[y][x] == "*" or self.grid[y][x] == word[0]):
            return False
        undovalue = self.grid[y][x]  
        undox = x
        undoy = y 
        self.grid[y][x] = word[0]
        # now need to write rest of the word
        if direction == self.HORIZONTAL:
            x += 1
        elif direction == self.VERTICAL:
            y += 1
        elif direction == self.DIAGONAL:
            y += 1
            x += 1
        elif direction == self.REVHORIZONTAL:
            x -= 1
        elif direction == self.REVVERTICAL:
            y -= 1
        elif direction == self.REVDIAGONAL:
            y -= 1
            x -= 1
        elif direction == self.FLIPDIAGONAL:
            x += 1
            y -= 1 
        elif direction == self.REVFLIPDIAGONA:
            x -= 1
            y += 1             
        else:
            print("This direction not implemented yet")
        if self.engrave(word[1:], x, y, direction):
            # we could do the rest, we are happy and done
            return True
        else:
            # grrh: something didn’t work, we need to undo now
            y = undoy
            x = undox
            self.grid[y][x] = undovalue
            return False
        
    def obfusticate(self):
        for row in self.grid:
            for i in range(len(row)):
                if row[i] == '*':
                    row[i] = 'abcdefghijklmnopqrstuvwxyz0123456789'[random.randint(0,25)]
                


    def letter(self,x,y):
        return self.grid[x][y]
    
