# //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# TicTacToe game written as a Python functions practice while exploring Python during 100DaysOfCode challenge. #
# 02/2022, Danilo Bilanoski.
# //////////////////////////////////////////////////////////////////////////////////////////////////////////// #


###  Variables

## Game state

current_player = " " # needs reset after every turn
game_started = False # needs update on first run
another_round = True # Updates to false when users wants to stop playing
win = False # needs reset after every round
round_count = 1

# Current state of the game board
current_board = {
  "A": [" "," ", " "],
  "B": [" "," ", " "],
  "C": [" "," ", " "]
}

# Winning patterns
winning_patterns = [("A0","A1","A2"),("B0","B1","B2"),("C0","C1","C2"),("A0","B0","C0"),("A1","B1","C1"),("A2","B2","C2"),("A0","B1","C2"),("A2","B1","C0")]

# User objects
player_1 = {
  "name": " ",
  "symbol": " ",
  "input_count": 0, # needs reset after each round
  "input_fields": [], # needs reset after each round
  "times_won":0
}

player_2 = {
  "name": " ",
  "symbol": " ",
  "input_count": 0, # needs reset after each round
  "input_fields": [], # needs reset after each round
  "times_won":0
}


### Utility & Service Functions

# Board functions 
def clear_board():
  '''
  This clears the board after every round.
  '''
  for key in current_board.keys():
    current_board[key] = [" ", " ", " "]


def print_board():
  '''
  This prints the board taking into account current status of inputs tracked in the current_board dictionary.
  '''
  c = current_board
  print("               ")
  print("     0   1   2	")
  print("               ")
  print(f"A    {c['A'][0]} | {c['A'][1]} | {c['A'][2]} ")
  print("    --- --- ---")
  print(f"B    {c['B'][0]} | {c['B'][1]} | {c['B'][2]} ")
  print("    --- --- ---")
  print(f"C    {c['C'][0]} | {c['C'][1]} | {c['C'][2]} ")
  print("               ")


def get_available_slots():
  '''
  This returns empty slots from current game board.
  '''
  slots = []
  for item in current_board.items():
    for a,b in enumerate(item[1]):
      if b == " ":
        slots.append(f"{item[0]}{a}")
      else:
        pass
  return slots

# User functions
def clear_users():
  '''
  This clears the user objects after every round.
  '''
  players = ["player_1", "player_2"]
  
  for player in players:
    globals()[player]['input_count'] = 0
    globals()[player]['input_fields'] = []


def configure_player(str):
  '''
  This one takes the player object name and prompts user for inputs to configure it.
  Intention is to use it first for player one, then player 2.
  '''
  if str == "player_1":
    print(" ")
    print(f"Hi there, {str}.")
  
    # Pick user name
    player_1["name"] = input("Enter your name: ")

    # Pick player symbol
    while player_1["symbol"] != "X" and player_1["symbol"] != "O":
      player_1["symbol"] = input("Chose your symbol [X or O]: ")
    
    print(f"You are ready, {player_1['name']}.")
  
  elif str == "player_2":
    print(" ")
    print(f"Welcome {str}.")
  
    # Pick user name
    player_2["name"] = input("Enter your name: ")

    # Pick player symbol
    if player_1["symbol"] == "X":
      player_2["symbol"] = "O"
      print("Your symbol is O.")
    
    elif player_1["symbol"] == "O":
      player_2["symbol"] = "X"
      print("Your symbol is X.")
    
    else:
      print("Something went wrong, check player config sequence as player 1 is not configured.")
      return
    
    print(f"You are ready, {player_2['name']}.")


def user_input():
  '''
  Gets and returns valid user input for the current move on the board.
  To be used before update_board()
  '''
  print(f"Your turn, {globals()[current_player]['name']}.")
  answer = ""
  available_board_slots = get_available_slots()

  while answer not in available_board_slots:
    answer = input("Choose your next move [A0 to A2; B0 to B2; C0 to C2]: ").upper()

  return answer


def update_board(str):
  '''
  This updates the current game board with the passed user input.
  Passed string should be result of user_input().
  '''
  current_board[str[0]][int(str[1])] = str
  if current_player == "player_1":
    current_board[str[0]][int(str[1])] = player_1["symbol"]
    return
  
  elif current_player == "player_2":
    current_board[str[0]][int(str[1])] = player_2["symbol"]
    return

  else:
    print("Something went wrong, see update_board() function.")
    return 
    
def update_user(str):
  '''
  This updates the current player.
  Passed string should be result of user_input().
  '''  
  if current_player == "player_1":
    player_1["input_fields"].append(str)
    player_1["input_count"] += 1
    return
  
  elif current_player == "player_2":
    player_2["input_fields"].append(str)
    player_2["input_count"] += 1
    return

  else:
    print("Something went wrong, see update_user() function.")
    return 


## Game state functions

# Winner check (user object based)
def is_winner(str):
  '''
  This checks whether user is a winner at the given moment based on recored user inputs and updates the win variable.
  '''
  current_inputs = globals()[str]["input_fields"]

  if len(current_inputs) >= 3:

    for pattern in winning_patterns:

      if set(pattern).issubset(set(current_inputs)):
        print("Winner")
        globals()[str]["times_won"] += 1
        return True
    
    else:
      if len(player_1["input_fields"] + player_2["input_fields"]) == 9:
        print("Tie - no winners in this round.")
        return None

  else:
    pass

  return False
   
# Game round
def game_round():
  '''
  This one runs the game round procedure.
  '''
  # Set player game state
  if globals()["current_player"] == " " or globals()["current_player"] == "player_2":
    globals()["current_player"] = "player_1"
  else:
    globals()["current_player"] = "player_2"
  print(f"Get ready, {globals()[current_player]['name']}.")
  print_board()
  
  # Get user input
  current_player_input = user_input()

  # Update game board
  update_board(current_player_input)

  # Update user object
  update_user(current_player_input)

  # Check if somebody is a winner
  globals()["win"] = is_winner(globals()["current_player"])


# Print statistics
def print_stats(str):
  player = globals()[str]
  print("---------------------------------------")
  print(f"Summary for player {player['name']}:")
  print(".  .  .  .  .  .  .  .  .  .  .  .  .  ")
  print(f"  Win after {player['input_count']} moves.")
  print(f"  Total wins: {player['times_won']}.")
  print("---------------------------------------")
  
def game_over():
  print("---------------------------------------")
  print("------------  GAME OVER  --------------")
  print(".  .  .  .  .  .  .  .  .  .  .  .  .  ")
  print(f"Game summary:")
  print(".  .  .  .  .  .  .  .  .  .  .  .  .  ")
  print(f"  Rounds played: {globals()['round_count']}.")
  print(f"  Result:")
  print(f"    {player_1['name']}: {player_1['times_won']} wins.")
  print(f"    {player_2['name']}: {player_2['times_won']} wins.")
  print(".  .  .  .  .  .  .  .  .  .  .  .  .  ")
  print("---------------------------------------")
  

### Main logic

# Handle start of the game and config of users
if game_started == False:
  print("---------------------------------------")
  print("------------  TIC-TAC-TOE -------------")
  print(".  .  .  .  .  .  .  .  .  .  .  .  .  ")
  print("Welcome to the Tic-tac-toe - simple fun\nin Pyhton with overly complicated game\nlogic written by Danilo Bilanoski.")
  print(".  .  .  .  .  .  .  .  .  .  .  .  .  ")
  configure_player("player_1")
  configure_player("player_2") 
  game_started == True
else:
  pass

# While another_round is true, keep spinning rounds
while another_round == True:

  play_another_round = None

  print(".  .  .  .  .  .  .  .  .  .  .  .  .  ")
  print(f"### Round {round_count} ###")
  print(".  .  .  .  .  .  .  .  .  .  .  .  .  ")
  # Keep the round alive while winner emerges or board gets full
  while win == False and (player_1["input_count"]+player_2["input_count"]) < 9:

    game_round()

  # Round completed, print board
  print_board()

  # If there was a tie, reset the win variable else proceed printing the stats for the winner
  if win == None:
    print("No one won the game, better luck next time.")
    win = False
  else:
    print_stats(current_player)
    print(f"Congrats {globals()[current_player]['name']}, you won the game!")

  # Check if player wants to keep playing
  while play_another_round != "y" and play_another_round != "n":
    locals()["play_another_round"] = input("Do you want to play another round [y, n]: ")
  
  # Reset current user so winner starts first
  if current_player == "player_2":
    current_player = "player_1"
  else:
    current_player = "player_2"

  # Clear the board
  clear_board()

  # Clear users
  clear_users()

  # Clear win state
  globals()["win"] = False
  globals()["another_round"] = True

  # Check if we need to continue playing
  if play_another_round == "n":
    globals()["another_round"] = False
  else:
    globals()["another_round"] = True

game_over()