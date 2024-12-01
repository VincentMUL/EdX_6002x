#Some background in Inferential Statistics, for continuing our Stochastical Programs.
#Sample drawn from Population.
#Population being a set of examples.
#Sample being a proper subset of the population; a few examples.
#GOAL: Statistical knowledge about the population from the sample.
#Only works if the sample is random, containing the same properties as the population.

#Example of the coin flip. Suppose you flipped it once, and it landed on heads. 
#How confident are you about the next flip being heads as well?
#What if you flipped it twice and got heads twice? How confident are you now?
#You might reason for a fair coin the chance was 0.25 to be heads twice in a row.
#What if you flipped it 100 times? And all 100 times it landed on heads?
#Now you might feel very safe in inferring that the coin is biased.
#Your belief is based on the intuation that 100 flips is representative to all flips.
#This belief seems sound for 100 flips being heads. Suppose 52 H and 48 T.
#How confident are you for saying 52/100 is the true probability of heads?
#How confident there are more H then T in the next 100 flips?
#Why is their a difference in confidence?
#Confidence depends on 2 things: Sample Size and Variance (or variability).

#Roulette example. 

import random

#In FairRoulette you win what you bet, because it's fair. Which is why the odds are 1.0 for black and red.
#The pocketOdds is the number of pockets - 1. Why -1? 
#Imagine if you bet 1 dollar and there were only 2 pockets. If you win, you get 1 dollar.
#If you lose, you lose 1 dollar. The odds are 1.0.
#Therefore the odds are the number of pockets - 1. If you win the selected pocket, you get the amount times the odds.


class FairRoulette():
    def __init__(self):
        self.pockets = [] #Pocket numbers
        for i in range(1, 37):
            self.pockets.append(i)#Pocket numbers 1-36
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0 #Odds for black and red
        self.pocketOdds = len(self.pockets) - 1.0 #Odds for pocket
        #Why -1? Because the pocketOdds is the number of pockets - 1.
        
    def spin(self):
        self.ball = random.choice(self.pockets)#Randomly choose a pocket
        
    def isBlack(self): #Check if the ball is black
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10)\
            or (self.ball>18 and self.ball<=28)): #Black pockets
            return self.ball%2 == 0 #Even numbers are black
        else:
            return self.ball%2 == 1 #Odd numbers are red
        
    def isRed(self): #If it's not black, it's red
        return type(self.ball) == int and not self.isBlack()
    
    def betBlack(self, amt):#Bet on black
        if self.isBlack():
            return amt*self.blackOdds #return the amount times the odds
        else: return -amt #return the negative amount
    
    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else: return -amt
    
    def betPocket(self, pocket, amt):#Bet on a pocket
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds #return the amount times the odds
        else: return -amt #return the negative amount
    
    def __str__(self):
        return 'Fair Roulette'

#The simulation itself. Structured with game (because different roulettes)
#and number of spins (which determines iterations of the game).
def playRoulette(game, numSpins, toPrint = True):
    luckyNumber = '2' #The lucky number, played number
    bet = 1 #Bet 1 dollar.
    totReds, totBlacks, totPockets = 0.0, 0.0, 0.0
    for i in range(numSpins):
        game.spin()
        totReds += game.betRed(bet)
        totBlacks += game.betBlack(bet)
        totPockets += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting red =', str(100*totReds/numSpins) + '%')
        print('Expected return betting black =', str(100*totBlacks/numSpins) + '%')
        print('Expected return betting', luckyNumber, '=', str(100*totPockets/numSpins) + '%\n')
    return (totReds/numSpins, totBlacks/numSpins, totPockets/numSpins)

numSpins = 100000
game = FairRoulette()
playRoulette(game, numSpins)
#Notice the variations in the expected returns.
#Small number of spins, large variations.
#Large number of spins, small variations.
#For 10million spins, range of returns is pretty narrow.
#It says something about the expected return of the next spin (ie zero).
#Law of Large Numbers (Bernoulli's law): As the number of trials increases, 
# the average of the trials converges to the expected value.
# In repeated independent trials with the same probability p of success in each trial,
# the chance that the fraction of successes differs from p converges to zero as the number of trials goes to infinity.
# NOTE does not imply if deviations occur, they will be corrected by opposite deviations in the future.
# This is the Gambler's Fallacy.
# Example of case: Monte Carlo Fallacy (August 18, 1913, Casino de Monte Carlo).
# The ball fell on black 26 times in a row. People bet on red, because they thought it was due.
# Probability of 25 times black in row is 1/2^25 = 1/33.5 million.
# Probability of 26 times black in row is 1/2^26 = 1/67 million.
# But the probability of 26 times black in row after 25 times black in row is 1/2.
# Sometimes confusion between gambler's fallacy and regression to the mean.
# Regression to the mean is the tendency of extreme events to be followed by less extreme events.
# Example: If you are very tall, your children will be shorter than you.
# Example: 10 times fair roulette, 10 times black. Likely next 10 times will be less black.
#          Looking at the mean of the 20 spins, it will be closer to 50% black, than the first 10 spins.
#          This is regression to the mean.
# First used by Francis Galton in 1885, in the context of height of children of tall parents:
# 'Regression towards mediocrity in hereditary stature.'
# Paper info: Galton, F. (1886). Regression towards mediocrity in hereditary stature. Journal of the Anthropological Institute, 15, 246-263.
# Regression to the mean is a mathematical phenomenon, not a psychological one.
# It's a consequence of the law of large numbers.
# It's a consequence of the fact that extreme events are rare.

# Casinos are not fair, they have a house edge; pocket of 0 and 00 and both green.

# EXERCISE 1

# A fair two-sided coin is flipped 4 times. It comes up heads all four times. 
# What is the probability that it comes up heads on the fifth flip? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 1/2. The coin is fair, so the probability of heads is 1/2.

# A fair two-sided coin is flipped 1000 times. It comes up heads every time. Which is correct?
# A. Regression to the mean tells us that the next 1000 tosses will be almost all tails.
# B. Regression to the mean tells us that the next few tosses will be not as extreme as the first 1000.
# Answer B. The probability of 1000 heads in a row is 1/2^1000, which is very small.

# Next we toss a huge ball with 1,000 dots on it. 
# Half the dots are red and the other half are blue. 
# We roll the ball and when it stops, we note the color of the dot on the very top of the ball.
# True or False? If we roll it four times, and it comes up red once and blue three times, 
# then we have proved that the ball is biased.
# False. The probability of 3 blues and 1 red is 1/2^4 = 1/16. Not very unlikely.
# Sample size is simply too small.

