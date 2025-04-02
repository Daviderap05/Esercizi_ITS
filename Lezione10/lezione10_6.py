'''
    Add a method called simulate_until_win(self, my_ticket) that:

        Accepts a ticket (a list of 4 items).
        Repeatedly draws random tickets using the draw_ticket() method.
        Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
        Returns the number of attempts and the winning ticket.
        
    2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

    3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

    4. Print a message showing:

        a) Your ticket
        b) The winning ticket
        c) How many attempts it took to win

'''
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