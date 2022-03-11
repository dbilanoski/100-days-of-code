## Goal - practice OOP in Python 

# Game logic
  # Dealer will be computer, player will be human
  # We'll have Hit and Stay
    # Hit - player recieves another card
    # Stay - stop recienivng cards
  # Goal - get closer to 21 than the dealer does
  # Turn based - player either hits or stay - once stayed, computer dealer turn is on
  # Computer then hits until it either beats the player or it busts
  # If sum of cards is more than 21, player is bust and round finishes
  # If player gets an ace and a face card (21), it's called blackjack
  # Bet is placed before the round
    # Winer gets the invested bet of opponent
    # Blackjack win gets 1.5 * invested bet

### Globals
import random

symbols = {
  "Hearts":"♡", 
  "Diamonds":"♢", 
  "Spades":"♤", 
  "Clubs":"♧"
  }

card_values = {
    "Two":[2, "2 "], 
    "Three":[3, "3 "], 
    "Four":[4, "4 "],  
    "Five":[5, "5 "],  
    "Six":[6, "6 "],  
    "Seven":[7, "7 "],  
    "Eight":[8, "8 "],   
    "Nine":[9, "9 "], 
    "Ten":[10, "10 "], 
    "Jack":[10, "J "], 
    "Queen":[10, "Q "],
    "King":[10, "K "],
    "Ace":[11, "A "]
  }

### Classes
class Card():
  '''
  Card definitions.
  '''

  def __init__(self,symbol,rank):
    self.symbol = symbol
    self.rank = rank
    self.value = card_values[rank][0]
    self.print_value = card_values[rank][1]
  
  def print_card(self, card="Blank"):
    '''
    Card printing method. When called with "Blank", it will show card "faced down".
    '''
    if type(card) == type([]):
      for c in card:
        print(f"...........\n: {c.print_value}      :\n:         :\n:         :\n:         :\n:         :\n:       {symbols[c.symbol]} :\n...........")
  
    else:
      print("...........")
      if card == "Blank":
        print(f": ?       :")
      else:
        print(f": {card.print_value}      :")
      print(":         :")
      print(":         :")
      print(":         :")
      print(":         :")
      if card == "Blank":
        print(f":       ? :")
      else:
        print(f":       {symbols[card.symbol]} :")
      print("...........")
    
  def __str__(self):
    print("...........")
    print(f": {self.print_value}      :")
    print(":         :")
    print(":         :")
    print(":         :")
    print(":         :")
    print(f":       {symbols[self.symbol]} :")
    print("...........")
    return f"{self.rank} of {self.symbol}"
  
class Deck():
  '''
  Deck definitions.
  '''
  def __init__(self):
    self.deck_cards = []

    for symbol in list(symbols.keys()):
      for value in list(card_values.keys()):
        self.deck_cards.append(Card(symbol, value))

  def shuffle_deck(self):
    '''
    Shuffles the deck in place.
    '''
    random.shuffle(self.deck_cards)
  
  def deal_card(self, hit=False, current_player=None):
    '''
    Returns one card from the deck. 
    In case "hit" is used, ask user for the Jack value.
    In case "hit" is used and user is the dealer, assign value based on whether dealer cards sum is greater or less than 17 (soft 17).
    '''
    if hit == False:
      return self.deck_cards.pop()

    else:
      current_card = self.deck_cards.pop()

      if current_card.rank == "Ace":
        if current_player.role == "human":
          while True:
            try:
              current_card.value = int(input("Do you want your Ace to be valued as 1 or 11 (1, 11): "))
            except:
              print("We need 1 or 11 here.")
            else:
              break
        else:
          if current_player.print_current_sum("blind") < 17:
            current_card.value = 11
          else:
            current_card.value = 1 

      return current_card

class Player():
  '''
  Player definitions.
  '''
  rounds_won = 0
  money_won = 0
  money_lost = 0 
  role = "human"

  def __init__(self, name=" "):
    self.name = name
    self.wallet = 0
    self.current_cards = []

    if self.name == "Dealer":
      self.role = "dealer"
  
  def __str__(self):
    return f"Player {self.name} won {self.rounds_won} rounds, {self.money_won}$ and lost {self.money_lost}$. Current wallet: {self.wallet}$"
   
  def configure_player(self):
    '''
    Initial configuration of the human player.
    '''
    print(f"Welcome to the game of BlackJack, player.")
    print(f"Let's take a moment to configure you.\b")
    self.name = input("Your name: ")
    while type(self.wallet) != type(3) or self.wallet == 0:
      try:
        self.wallet = int(input("Your current gambling budget: "))
      except:
        print("Please enter a number greater than 0.")
    print(f"You are ready {self.name}.\n")

  def print_current_sum(self,blind=False):
    '''
    This handles printing the sum of current cards. If "blind" is used, method just returns the num.
    '''
    if blind != "blind":
      if len(self.current_cards) > 0:
        print(f"Current SUM is: {sum(card.value for card in self.current_cards)}\n")
      else:
        print("No cards on the table at the moment.\n")
    else:
      return sum(card.value for card in self.current_cards)

  def update_on_win(self, game, blackjack=False):
    self.game = game
    self.rounds_won += 1
    self.money_won += game.players_bet

    if blackjack != False:
      self.wallet += game.players_bet * 1.5
    else:
      self.wallet += game.players_bet
    
class Game():
  '''
  Game stats & definitions.
  '''
  def __init__(self):
    self.current_round = 0
    self.current_player = "human"
    self.game_on = True
    self.players_bet = 0
  
  def place_bet(self, player):
    '''
    This handles the betting routine.
    '''
    self.player = player

    while True:
      try:
        bet = int(input("Place your bet ($): "))
      
      except:
        print(f"We need numbers bigger than 0 here, {self.player.name}.")

      else:
        if bet == 0:
          print(f"We need numbers bigger than 0 here, {self.player.name}.")
        elif bet <= self.player.wallet:
          self.players_bet = bet
          self.player.wallet -= bet
          break
        else: 
         print(f"Not enough money in your wallet, {self.player.name}. Amount left: {self.player.wallet}$")

    print(f"Bet of {self.players_bet} placed, good luck {self.player.name}!")

  def play_again(self):
    '''
    This handles the new round prompt routine.
    '''
    while True:
      answer = input("Wanna play again (y, n): ")

      if answer == "n":
        self.game_on = False
        break
      elif answer == "y":
        self.game_on = True
        self.current_player = "human"
        break
      else:
        print("Please use y or n for answer.")
     
### Main logic

# Initiate needed components
human = Player()
dealer = Player("Dealer")
new_game = Game()

# Configure the player
human.configure_player()

## Start of the round
while new_game.game_on == True:
  new_deck = Deck()
  new_game.current_round += 1
  
  # Reset stats
  new_game.players_bet = 0
  human.current_cards = []
  dealer.current_cards = []

  # Check user wallet
  if human.wallet == 0:
    print(f"Sorry {human.name}, you have no money left.")
    break

  # Place the bet
  new_game.place_bet(human)

  # Shuffle the deck
  new_deck.shuffle_deck()

  # Deal 2 cards to each player
  for card in range(2):
    human.current_cards.append(new_deck.deal_card())
    dealer.current_cards.append(new_deck.deal_card())

  # Show dealer cards
    # Dealer gets one opened, one closed
  print("\nDEALER CARDS")
  dealer.current_cards[0].print_card("Blank")
  dealer.current_cards[1].print_card(dealer.current_cards[1])
    # Human gets two opened
  print("\nYOUR CARDS")
  human.current_cards[0].print_card(human.current_cards)
  human.print_current_sum()

  while True:
     # Player / Dealer turns
    current_player = globals()[new_game.current_player]
    print(f"Your turn {current_player.name}")

    # In case player's cards are already over 21
    if current_player.print_current_sum("blind") > 21:
      print("You lose!")

      if current_player.role == "human":
        human.money_lost += new_game.players_bet
        new_game.play_again()
        break
      elif current_player.role == "dealer":
        print(f"Player {human.name} has won.\n")
        human.rounds_won += 1
        human.money_won += new_game.players_bet
        human.wallet += new_game.players_bet
        new_game.play_again()
        break
    
    # Current player is human
    if new_game.current_player == "human":
      # Collect answer
      answer = 0
      while type(answer) != type(2) or answer > 2 or answer < 1:
        try:
          answer = int(input("[1] Hit or [2] Stay? (1 or 2): "))
        except:
          print("Please use 1 for 'Hit' or 2 for 'Stay'!")
        
      # Player's choice
      # If total sum > 21, bust (end of game_on, that case is handled at the begining of the loop)
      # If stay, check for winner, if true win, if not other player turn
      # If hit, draw another card, ask again 
      if answer == 2:
        # Check for winner
        if current_player.print_current_sum("blind") == 21:
          print("You win!")
          current_player.update_on_win(new_game,"blackjack")
          new_game.play_again()
          break

        else:
          # Set dealer's turn
          new_game.current_player = "dealer"

      else:
        # This is Hit, player pulls another card, loop repeats
        current_player.current_cards.append(new_deck.deal_card("hit",current_player))
        current_player.current_cards[-1].print_card(current_player.current_cards)
        current_player.print_current_sum()

    else:
      # Current player is the dealer
      current_player.print_current_sum()
      
      # Here we repeat drawing cards until
        # 1. > 21, bust, human wins, handled on beggining of the loop
        # 2. = 21, dealer wins
        # 3. > human sum and less than 21, dealer wins    
        # 4. Keep drawing

      if current_player.print_current_sum("blind") == 21:
        print("You win!")
        current_player.update_on_win(new_game, "blackjack")

        money_lost = new_game.players_bet * 0.5
        # Remove excess money from wallet human needed to pay
        human.wallet -= money_lost
        # Update "money lost" for human
        human.money_lost += money_lost

        new_game.play_again()
        break
 
      elif current_player.print_current_sum("blind") > human.print_current_sum("blind") and current_player.print_current_sum("blind") < 21:
        print("You win!")
        current_player.update_on_win(new_game)

        # Update "money lost" for human
        human.money_lost += new_game.players_bet
        new_game.play_again()
        break

      else:
        current_player.current_cards.append(new_deck.deal_card("hit",current_player))
        current_player.current_cards[-1].print_card(current_player.current_cards)
        current_player.print_current_sum()
  
print("Game over.")
print(f"Rounds played: {new_game.current_round}")
print(human)