# Periodic Element Fetcher
# Takes and arguement of atomic number, symbol or element name and outputs details about element

# Globals
PSQL="psql -X --username=freecodecamp --dbname=periodic_table --tuples-only -c"

# Functions
# Output Renderer
RENDER_OUTPUT(){
  if [[ -z $1 ]]
  then
    echo Nothing to render. Add database query result.
  else
    # While loop to loop over db result and print outro statement
    echo "$1" | while read ATOMIC_NUMBER BAR SYMBOL BAR NAME BAR TYPE BAR ATOMIC_MASS BAR MELTING_POINT BAR BOILING_POINT
    do
      echo "The element with atomic number $ATOMIC_NUMBER is $NAME ($SYMBOL). It's a $TYPE, with a mass of $ATOMIC_MASS amu. $NAME has a melting point of $MELTING_POINT celsius and a boiling point of $BOILING_POINT celsius."
    done
  fi
}

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
  # Atomic number case
  # Fetch element detais (as the atomic num is primary key)
  ELEMENT_DETAILS=$($PSQL "SELECT elements.atomic_number, elements.symbol, elements.name, types.type, properties.atomic_mass, properties.melting_point_celsius, properties.boiling_point_celsius FROM elements JOIN properties ON elements.atomic_number = properties.atomic_number JOIN types ON properties.type_id = types.type_id WHERE elements.atomic_number=$1")
  if [[ -z $ELEMENT_DETAILS ]]
  then
    echo I could not find that element in the database.
    exit
  else
    RENDER_OUTPUT "$ELEMENT_DETAILS"
  fi
elif [[ $1 =~ ^[a-zA-Z]{1,2}$ ]]
then
  # Symbol case (if arg is a two letter word)
  ELEMENT_DETAILS=$($PSQL "SELECT elements.atomic_number, elements.symbol, elements.name, types.type, properties.atomic_mass, properties.melting_point_celsius, properties.boiling_point_celsius FROM elements JOIN properties ON elements.atomic_number = properties.atomic_number JOIN types ON properties.type_id = types.type_id WHERE LOWER(elements.symbol)=LOWER('$1')")
  if [[ -z $ELEMENT_DETAILS ]]
  then
    echo I could not find that element in the database.
    exit
  else
    RENDER_OUTPUT "$ELEMENT_DETAILS"
  fi
else
  # Name case
  ELEMENT_DETAILS=$($PSQL "SELECT elements.atomic_number, elements.symbol, elements.name, types.type, properties.atomic_mass, properties.melting_point_celsius, properties.boiling_point_celsius FROM elements JOIN properties ON elements.atomic_number = properties.atomic_number JOIN types ON properties.type_id = types.type_id WHERE LOWER(elements.name)=LOWER('$1')")
  if [[ -z $ELEMENT_DETAILS ]]
  then
    echo I could not find that element in the database.
    exit
  else
    RENDER_OUTPUT "$ELEMENT_DETAILS"
  fi
fi
