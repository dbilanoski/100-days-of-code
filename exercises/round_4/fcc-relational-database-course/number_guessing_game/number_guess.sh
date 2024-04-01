#!/bin/bash

# GLOBALS
PSQL="psql --username=freecodecamp --dbname=number_guess --tuples-only -c"

# HANDLE USERNAME

# Will save user's id here later
USER_ID=""

# Ask user for a name
while [[ -z $USER_NAME_INPUT ]]
do
  echo Enter your username:
  read USER_NAME_INPUT
done

# Fetch database data
USER_DATA=$($PSQL "SELECT users.user_id, COUNT(games.game_id), MIN(games.game_guesses) FROM users JOIN games ON users.user_id=games.user_id WHERE users.name='$USER_NAME_INPUT' GROUP BY users.user_id;")
if [[ -z $USER_DATA ]]
then
  # Greet new user
  echo "Welcome, $USER_NAME_INPUT! It looks like this is your first time here."
  # Add him to the db
  ADD_USER_RESULT=$($PSQL "INSERT INTO users(name) VALUES('$USER_NAME_INPUT')")
  # If something went wrong, exit gracefully
  if [[ $ADD_USER_RESULT != "INSERT 0 1" ]]
  then
    echo Something went wrong. Try again later.
    exit
  fi
  # Fetch user's ID and save it
  USER_ID=$($($PSQL "SELECT user_id FROM users WHERE name='$USER_NAME_INPUT'") | sed 's/\s //g')

else
  # Pipe retrieved data to a while loop to get rid of the "|" and format data
    # NOTE - cannot use classic pipe here and cannot update variables outside of while loop as it creates a sub shell (not aware of current shell)
    # SOLUTION - to use "here" statement to force while loop executing in the current shell session
    # Sintax of while loop changes from pipe to feed the data to the "Done" statement using a here statament
    # This means that the data is the only thing running in the subshell which we are feeding to the current shell I guess?
    # https://stackoverflow.com/questions/16854280/a-variable-modified-inside-a-while-loop-is-not-remembered

  while read USR_ID BAR GAMES_PLAYED BAR BEST_GAME
  do
    # Greet user
    echo "Welcome back, $USER_NAME_INPUT. You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
    # Update USER_ID variable
    USER_ID=$USR_ID
    echo "$USER_ID, $USR_ID"
  done <<< "$USER_DATA"
fi

echo "User $USER_NAME_INPUT got and id: $USER_ID."
# GAME LOGIC
