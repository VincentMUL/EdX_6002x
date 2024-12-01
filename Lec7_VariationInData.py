import random
from Lec7_InferentialStatistics import playRoulette, FairRoulette

class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
        
    def __str__(self):
        return 'European Roulette'