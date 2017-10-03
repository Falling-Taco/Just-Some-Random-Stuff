import random
class TossSimulator():
    heads = 0
    tails = 0
    def doFlip(self):
        x = random.randint(0,1)
        if x:
            self.heads+=1
            print('heads!')
        else:
            self.tails+=1
            print('tails!')
 
    def getScore(self):
        print('heads : %d' %self.heads)
        print('tails : %d' %self.tails)
 
coin = TossSimulator()

while True:

    x = input('Do you want Toss the coin ? Yes or No?\n').lower()

    if(x == 'yes' or x == 'y'):
       coin.doFlip()
       coin.getScore()

    elif(x == 'no' or x == 'n'):
        break    

