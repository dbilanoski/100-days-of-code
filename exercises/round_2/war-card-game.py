## Goal - practice OOP in Python 

# https://en.wikipedia.org/wiki/War_(card_game)

# Game logic
  # Each player draws a card, bigger one wins
  # Player which looses gets the cards from table
  # First player who looses all cards wins the game
  # In case cards on table are even, war situation starts
    # Each player draws three cards, each pair competes
    # First one to have bigger cards wins, looser gets all cards from table

# We'll have these classes:
  # Card class which will hold a card symbol, rank and value
    # Rank will be a string of the card number which we will match by the value from the values dictionary
    # Symbol is the symbol

  # Deck class
    # On instntiating a new deck we need:
      # create all 52 card objects and hold them as list
    # We need a shuffle cards method (random liobrary shuffle())
    # We need a deal card method which will pop a card from the card list

  # Player class
    # Player needs to have a list of current cards he holds
    # Player needs to be able to add or remove cards from that list
      # When adding, card should go to the bottom of list
        # append() will do
      # When removing, card should go from the top of the list
        # pop(0) will remove first item in the list
      # When adding multiple cards, will use extend()

  # Game class
    # Current game status
      # Is game still on
      # Rounds played
    # Method for checking win status
    # Method for updating players/game on win
    # Method for printing stats
    # Method for clearing stats

import random

symbols = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
card_values = {
    "Two":2, 
    "Three":3, 
    "Four":4, 
    "Five":5, 
    "Six":6, 
    "Seven":7, 
    "Eight":8,  
    "Nine":9,
    "Ten":10,
    "Jack":11,
    "Queen":12,
    "King":13,
    "Ace":14
  }

class Card():
  '''
  Card definitions.
  '''

  def __init__(self,symbol,rank):
    self.symbol = symbol
    self.rank = rank
    self.value = card_values[rank]
  
  def __str__(self):
    return f"{self.rank} of {self.symbol}."

class Deck():
  '''
  Deck definitions.
  '''
  def __init__(self):
    # We need to instantiate 52 cards here and hold them as list
      # What we do is we loop through the symbols and for each we loop through rank creating one card of that rank and symbol and append it to the cards list
    self.all_cards =  []

    for symbol in symbols:
      for rank in ranks:
        # Create the Card Object
        new_card = Card(symbol,rank)
        # Append it to the all_cards list
        self.all_cards.append(new_card)

  def deck_shuffle(self):
    # Shuffle() does not return anything, it modifies the original list
    random.shuffle(self.all_cards)
  
  def deal_card(self):
    # This will return one card with pop() method
    # Pop() always removes last item in a list
    return self.all_cards.pop()

class Player():
  '''
  Player definitions.
  '''
  rounds_won = 0

  def __init__(self,name):
    
    self.name = name
    # This will hold player's card
    self.all_cards = []

  def remove_card(self):
    # This will remove and return first item from the all_cards list
    return self.all_cards.pop()

  def add_cards(self, new_cards):
    # In case we have multiple objects (list), we are using extend()
    # Else, we are using append()

    if type(new_cards) == type([]):
      # List of multiple card objects
      self.all_cards.extend(new_cards)
    else:
      # Single card object
      self.all_cards.append(new_cards)

  def __str__(self):
    return f"Player {self.name} has {len(self.all_cards)} cards."

class Game():
  '''
  Game state checkers and definitions.
  '''
  def __init__(self):
    self.game_on = True
    self.rounds_played = 0

  def check_winner(self,p1, p2):
    '''
    Check for winner.
    '''
    if len(p1.all_cards) > 0 and len(p2.all_cards) > 0:
      return False
    elif len(p1.all_cards) == 0:
      return p1
    else:
      return p2

  def someone_won(self,p):
    '''
    Set stats for winner. 
    Intention is to use self.check_winner() output as p
    '''
    p.rounds_won += 1
    self.rounds_played += 1
    print(f"{p.name} won the game!")

  def print_stats(self):
    '''
    Print game stats on game over.
    '''
    print(f"Rounds played: {self.rounds_played}")
    print(f"{player_one.name} wins: {player_one.rounds_won}.")
    print(f"{player_two.name} wins: {player_two.rounds_won}.")

    if player_one.rounds_won > player_two.rounds_won:
      print(f"{player_one.name} won the game.")
    elif player_one.rounds_won < player_two.rounds_won:
      print(f"{player_two.name} won the game.")
    else:
      print("It's a TIE.")

    print("Game over.")

  def clear_stats(self):
    '''
    Clear players stats after round is finished.
    '''
    # Clear players cards
    player_one.all_cards = []
    player_two.all_cards = []
  
  def __str__(self):
    '''
    Default string output.
    '''
    print(f"Currently {self.rounds_played} rounds played.")

## Main Logic

# Initiate players and the deck
player_one = Player("Lebsons")
player_two = Player("Sebsons")
new_deck = Deck()
new_game = Game()

# Shuffle the deck
new_deck.deck_shuffle()

# Split deck to players
for card in range(26):
  player_one.add_cards(new_deck.deal_card())
  player_two.add_cards(new_deck.deal_card())

# Game on while loop
while new_game.game_on == True:
  # Check for winner
  winner = new_game.check_winner(player_one, player_two)
  
  if winner != False:
    new_game.someone_won(winner)
    print("Game Over.")
    play_again = ""

    # Check if we want another round
    while play_again != "y" and play_again != "n": 
      play_again = input("Do you want to play another round (y, n): ") 
    
    if play_again == "n":
      new_game.game_on = False
      # Print stats
      new_game.print_stats()
      break
    else:
      # Clear players cards
      new_game.clear_stats()
      # Instantiate new deck
      new_deck = Deck()
      # Shuffle the deck
      new_deck.deck_shuffle()
      # Split deck to players
      for card in range(26):
        player_one.add_cards(new_deck.deal_card())
        player_two.add_cards(new_deck.deal_card())
  
  ## Game starts here
  # Current cards on table
  current_cards_on_table = []

  # Player 1 move
  current_cards_on_table.append(player_one.remove_card())
  print(f"Player {player_one.name} draws: {current_cards_on_table[0]}.")

  # Player 2 move
  current_cards_on_table.append(player_two.remove_card())
  print(f"Player {player_two.name} draws: {current_cards_on_table[1]}.")

  # Check cards
  if current_cards_on_table[0].value > current_cards_on_table[1].value:
    player_two.add_cards(current_cards_on_table)
    print("Player one wins, all cards on the table go to player two.\n")

  elif current_cards_on_table[1].value > current_cards_on_table[0].value:
    player_one.add_cards(current_cards_on_table)
    print("Player two wins, all cards on the table go to player one.\n")
  
  else:
    # War situation
    # Each player will place 3 cards, then we check ony by one. In case nobody wins, we repeat
    print("WAR STARTRED!")
    war_cards = []
    war_on = True

    while war_on == True:
      # In case the war situation led to empty deck without winners
      war_winner = new_game.check_winner(player_one,player_two)

      if war_winner == False:
        pass

      elif war_winner == player_one:
        # In case P1 has no cards, we consider him a winner
        # Player two gets the cards, we break out of war loop 
        # Win routine will be handled on begining of game_on loop
         player_two.add_cards(war_cards)
         print("No cards left at Player one!") 
         print(f"Player {player_one.name} wins the war, all cards on the table go to player two.")
         print("WAR ENDED!\n")
         war_on = False
         break
        
      elif war_winner == player_two:
        # In case P2 has no cards, we consider him a winner
        # Player one gets the cards, we break out of war loop 
        # Win routine will be handled on begining of game_on loop
         player_one.add_cards(war_cards)
         print("No cards left at Player two!") 
         print(f"Player {player_two.name} wins the war, all cards on the table go to player one.")
         print("WAR ENDED!\n")
         war_on = False
         break
     
      # We need three cards from each user for the war situation
      # In case one of users has less than three cards, we proceed war with one card from each

      if len(player_one.all_cards) <= 3 or len(player_two.all_cards) <= 3:
        war_cards.append(player_one.remove_card())
        war_cards.append(player_two.remove_card())
      else:
        for card in range(3):
          war_cards.append(player_one.remove_card())
          war_cards.append(player_two.remove_card())
      
       # Check player 1 card vs player 2 card to find winner
       # P1 will always be even, p2 odd - easy peasy
      for a in range(0,len(war_cards),2):

        for b in range(1,len(war_cards),2):

          print(f"Player {player_one.name} draws: {war_cards[a]}.")
          print(f"Player {player_two.name} draws: {war_cards[b]}.")
          # Player one has a better card
          if war_cards[a].value > war_cards[b].value:
            player_two.add_cards(current_cards_on_table)
            player_two.add_cards(war_cards)
            print(f"Player {player_one.name} wins, all cards on the table go to player {player_two.name} .")
            print("WAR ENDED.\n")
            war_on = False
            break
          # Player two has a better card
          elif war_cards[a].value < war_cards[b].value:
            player_one.add_cards(current_cards_on_table)
            player_one.add_cards(war_cards)
            print(f"Player {player_two.name} wins, all cards on the table go to player {player_one.name}.")
            print("WAR ENDED.\n")
            war_on = False
            break
        # No one had better cards (war continues)      
        else:
          continue
        # Someone won the war, we are breaking from the outer loop
        break