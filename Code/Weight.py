class Weight:
    weights = [0,0,0,0]
    score = 0



    def __lt__ (self, other):
        return self.score < other.score

    def __eq__ (self, other):
        return self.score == other.score
        
    def __gt__ (self, other):
        return self.score > other.score

    