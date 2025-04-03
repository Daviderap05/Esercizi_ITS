#esercizio 14 e 15
import random

class LotteryMachine:
    
    def __init__(self, list_n: list[str, int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]):
        
        self.list_n = list_n
        
    def ticket(self):
        
        x: list[str, int] = random.choices(self.list_n, k = 4)
        
        return x
    
    def display(self):
        
        print(f"\nThe 4 winning items are: {', '.join(map(str, self.ticket()))}\n")
        #print("Congratulations you have won the awards.\n")
        
    def simulate_until_win(self, my_ticket: list= []):
        
        win_lottery: list[str, int] = self.ticket()
        count: int = 0
        
        while win_lottery[:] != my_ticket[:]:
            
            my_ticket: list[str, int] = self.ticket()
            count += 1
            
        return count, win_lottery, my_ticket
    
win_lottery: LotteryMachine = LotteryMachine()
count, win_lottery, my_ticket = (win_lottery.simulate_until_win())
print(count, win_lottery, my_ticket)