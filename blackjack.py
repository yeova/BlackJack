from operator import truediv
import random, os

clear = lambda: os.system('cls') 

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

print('Welcome to the Black Jack Game!')
   
# the function asking player to start a game
def new_game():
    ng = ''
    while ng not in ['yes','no']:
        ng = input("Do you want to start a new game?\nAnswer 'Yes' or 'No' ").lower()
        if ng =='yes':
            return True
        elif ng =='no':
            return False
        else:
            clear() 
            print ('Invalid aswer. Please try again.')

# the function for making a bet
def bet_action(amount):
    print(f"Your current balance is {amount}.")
    bet = 'wrong'
    while not bet.isdigit():
        bet = input(f'Make your bet: ')
        if bet.isdigit() == False:
            print('Invalid input. Please try again.')
        elif int(bet) > amount:
            print('Your bet cannot exceed your balance. Please try again.')
            bet = 'wrong'
    clear()
    bet = int(bet)
    amount -= bet            
    print(f'Your bet is accepted. Your current bet: {bet}.')
    print(f'Your balance: {amount}.')
    return (bet, amount)

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name, amount = 100):

        self.name = name
        self.all_cards = []
        self.amount = amount

    def add_cards(self, new_card):

            self.all_cards.append(new_card)
    
    def sum (self):

        k = 0
        sum = 0

        for i in self.all_cards:
            sum += i.value

            if i.value == 11:
                k += 1

        while sum > 21 and k > 0:
            sum -= 10
            k -= 1
        
        return sum 
 
# the function showing table
def table(dealer, player, players_turn):

    print(f"\n{player.name}'s cards:")
    for i in player.all_cards:
        print ('|', i, end=' |   ')
    print(f"\n{player.name}'s sum is {player.sum()}")

    print("\nDealer's cards:")
    sum = 0

    if players_turn:
        print ('|', dealer.all_cards[0], end=' |   |      x       |')
        sum = dealer.all_cards[0].value

    else:
        for i in dealer.all_cards:
            print ('|', i, end=' |   ') 
        sum = dealer.sum()
    print(f"\nDealer's sum is {sum}\n")


# the function asking about next action
def game_choice(cont_turn):
    choice = ''
    while choice not in ['hit','stay'] and cont_turn:
        choice = input("HIT or STAY? ").lower()

        if choice =='hit':
            clear()
            player.add_cards(new_deck.deal_one())

        elif choice =='stay':
            clear()
            cont_turn = False
            
        else:
            print ('Invalid aswer. Please try again. Choose between hit and stay.')

    return cont_turn
        
    


# GAME SETUP
dealer = Player('Dealer')
player = Player(input('Enter your name: '))
clear()

# the variable to keep game playing
game_on = True

while game_on:

    player.all_cards = []
    dealer.all_cards = []
    players_turn = True
    
    new_deck = Deck()
    new_deck.shuffle()

    for x in range(2):
        dealer.add_cards(new_deck.deal_one())
        player.add_cards(new_deck.deal_one())
    
    bet, player.amount = bet_action(player.amount)

    while players_turn:

        table(dealer, player, players_turn)
        players_turn = game_choice(players_turn)

        if player.sum() > 21:

            table(dealer, player, not players_turn)
            print("IT'S A BUST. YOU LOST!")
            players_turn = False
                
    while dealer.sum() < 17 and player.sum() <= 21:
        dealer.add_cards(new_deck.deal_one())

    if player.sum() <= 21:

        if dealer.sum() > 21 or player.sum() > dealer.sum():
            player.amount +=  bet * 2
            print("YOU WON !")

        elif player.sum() == dealer.sum():
            player.amount +=  bet
            print("IT'S A DRAW .")

        else:
            print("YOU LOST !")
            
        table(dealer, player, players_turn)


    if player.amount == 0:
        print(f'Your balance is empty.')
        game_on = new_game()
        player.amount = 100

print ("Okay. See you next time!")

