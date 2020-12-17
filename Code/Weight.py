class Weight:

    def __init__(self, weights, score):
        self.weights = weights
        self.score = score



    def __lt__ (self, other):
        return self.score > other.score

    def __eq__ (self, other):
        return self.score == other.score
        
    def __gt__ (self, other):
        return self.score < other.score

    