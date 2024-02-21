#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

# Clear tables
echo $($PSQL "TRUNCATE games, teams")

# Cat the csv then pipe it to while loop to variables matching csv headers
cat games.csv | while IFS="," read YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  # Skip printing csv headers by checking if the variable name matches the csv header
  if [[ $YEAR != 'year' ]]
  then
    # Get winner ID. In not there, add winner name to the database
    WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
    if [[ -z $WINNER_ID ]]
    then
      # Insert winner team name
      INSERT_TEAMS=$($PSQL "INSERT INTO teams(name) VALUES('$WINNER')" 2>&1)
      # Get ID from the database
      WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
    fi
    
    # Do same for the opponent
    OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")
    if [[ -z $OPPONENT_ID ]]
    then
      # Insert opponent team name
      INSERT_TEAMS=$($PSQL "INSERT INTO teams(name) VALUES('$OPPONENT')")
      # Get ID from the database
      OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")
    fi
    
    # Add data to the games table
    INSERT_GAMES=$($PSQL "INSERT INTO games(year, round, winner_goals, opponent_goals, winner_id, opponent_id) VALUES($YEAR,'$ROUND',$WINNER_GOALS,$OPPONENT_GOALS,$WINNER_ID,$OPPONENT_ID)")
    # Print final confirmation
    if [[ $INSERT_GAMES == "INSERT 0 1" ]]
    then
      echo All went well: $YEAR, $ROUND, $WINNER_GOALS, $OPPONENT_GOALS, $WINNER_ID, $OPPONENT_ID
    fi
  fi

done