from abstract import Game

class CasinoGame(Game):
    def __init__(self):
        print("es")
    def play(self):
        print("now playing")
    
    def bet(self):
        print("placing a bet")

game =CasinoGame()
game.play()
game.bet()



