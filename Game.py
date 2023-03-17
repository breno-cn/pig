import random

class Game:
    def __init__(self) -> None:
        self.current_turn = 0
        self.players = [0, 0]
        self.score_acc = 0

    def reset(self) -> None:
        self.current_turn = 0
        self.players = [0, 0]
        self.score_acc = 0

    def flip_turn(self) -> None:
        self.current_turn = 1 if self.current_turn == 0 else 0

    def roll(self) -> None:
        dice = random.randint(1, 6)
        
        if dice == 1:
            self.flip_turn()
            self.score_acc = 0
            return

        self.score_acc += dice

    def hold(self) -> None:
        self.players[self.current_turn] += self.score_acc
        self.flip_turn()
        self.score_acc = 0

    def play_random(self) -> None:
        chance = random.randint(1, 2)

        if chance == 1:
            self.roll()
        else:
            self.hold() 

    def player1_win(self) -> None:
        if self.current_turn == 1:
            self.play_random()
            return

        target = 10
        if self.score_acc <= target:
            self.roll()
        else:
            self.hold()

    def player2_win(self) -> None:
        if self.current_turn == 0:
            self.play_random()
            return

        target = 10
        if self.score_acc <= target:
            self.roll()
        else:
            self.hold()

    def tough_victory(self) -> None:
        target = 9 if self.current_turn == 1 else 12
        if self.score_acc <= target:
            self.roll()
        else:
            self.hold() 
    
    def should_stop(self) -> bool:
        return self.players[0] >= 100 or self.players[1] >= 100

    def winner(self) -> int:
        if self.players[0] >= 100:
            return 0
        
        return 1
