#esercizio 14 e 15
import random
from typing import Any

class LotteryMachine:
    
    def __init__(self, list_n: list[Any] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]):
        
        self.list_n = list_n
        
    def ticket(self) -> list[Any]:
        
        x: list[Any] = random.choices(self.list_n, k = 4)
        
        return x
    
    def display(self) -> None:
        
        print(f"\nThe 4 winning items are: {', '.join(map(str, self.ticket()))}\n")
        #print("Congratulations you have won the awards.\n")
        
    def simulate_until_win(self) -> tuple[int, list[Any], list[Any]]:
        
        my_ticket: list[Any] = []
        win_lottery: list[Any] = self.ticket()
        count: int = 0
        
        while win_lottery[:] != my_ticket[:]:
            
            my_ticket: list[Any] = self.ticket()
            count += 1
            
        return count, win_lottery, my_ticket
    
lottery_machine: LotteryMachine = LotteryMachine()
count, winning_ticket, my_ticket = (lottery_machine.simulate_until_win())
print(count, winning_ticket, my_ticket)