# Periodic Element Fetcher
# Takes and arguement of atomic number, symbol or element name and outputs details about element

# Globals
PSQL="psql --username=freecodecamp --dbname=<database_name> -t --no-align -c"

# Functions
# Element ID Fetcher
# I

# Main Logic
# Check if argument is passed
if [[ ! $1 ]]
then
  echo Please provide an element as an argument.
  exit
fi

# If argument is passed, check what kind of argument
# If arg is a number (atomic num case)
if [[ $1 =~ ^[0-9]+$ ]]
then
  echo Is number
elif [[ $1 =~ ^[a-zA-Z]{1,2}$ ]]
then
  # If arg os a two letter word (symbol case)
  echo Is symbol
else
  # Else (name case)
  echo Name case
fi
