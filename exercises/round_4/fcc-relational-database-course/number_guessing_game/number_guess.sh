#!/bin/bash

# GLOBALS
PSQL="psql --username=freecodecamp --dbname=number_guess --tuples-only -c"

# HANDLE USERNAME
while [[ -z $USER_NAME_INPUT ]]
do
  echo Enter your username:
  read USER_NAME_INPUT
done

# Fetch user id from the db
USER_ID=$($PSQL "SELECT user_id FROM users WHERE name='$USER_NAME_INPUT'")

if [[ -z $USER_ID ]]
then
  # NEW USER CASE
  # Greet new user
  echo "Welcome, $USER_NAME_INPUT! It looks like this is your first time here."

  # Add user to the db
  ADD_USER_RESULT=$($PSQL "INSERT INTO users(name) VALUES('$USER_NAME_INPUT')")
  # If something went wrong, exit gracefully
  if [[ $ADD_USER_RESULT != "INSERT 0 1" ]]
  then
    echo Something went wrong. Try again later.
    exit
  fi

  # Update user id
  USER_ID=$($PSQL "SELECT user_id FROM users WHERE name='$USER_NAME_INPUT'")
else
  # EXISTING USER CASE
  # Fetch user's database data
  USER_DATA=$($PSQL "SELECT users.name, COUNT(games.game_id), MIN(games.game_guesses) FROM users JOIN games ON users.user_id=games.user_id WHERE users.user_id='$USER_ID' GROUP BY users.user_id;")
  
  # Loop over user's data and store them to variables for formatting
  echo "$USER_DATA" | while read USERNAME BAR GAMES_PLAYED BAR BEST_GAME
  do
    # Greet user
    echo "Welcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
  done
fi

# GAME LOGIC
# Create random number between 1 and 1000
SECRET_NUMBER=$(( RANDOM % 1000 + 1 ))

# Counter for how many guesses it took
NUMBER_OF_GUESSES=0

# Ask user to guess
echo "Guess the secret number between 1 and 1000:"

# Loop it until user guessess 
until [[ $USER_GUESS == $SECRET_NUMBER ]]
do
  # Get the input from the user
  read USER_GUESS

  # Check if input is an integer 
  if [[ $USER_GUESS =~ ^[0-9]+$ ]]
  then
    # Lower than secret number case
    if [[ $USER_GUESS -gt $SECRET_NUMBER ]]
    then
      echo "It's lower than that, guess again:"
    # Higher than secret number case
    elif [[ $USER_GUESS -lt $SECRET_NUMBER ]]
    then
      echo "It's higher than that, guess again:"
    fi
  # Not an integer case
  else
    echo "That is not an integer, guess again:"
  fi

  # Increment the counter
  ((NUMBER_OF_GUESSES+=1))
done

# Winner case
echo "You guessed it in $NUMBER_OF_GUESSES tries. The secret number was $SECRET_NUMBER. Nice job!"

# Update the database
DATABASE_UPDATE_RESULT=$($PSQL "INSERT INTO games(user_id,game_guesses) VALUES($USER_ID,$NUMBER_OF_GUESSES)")