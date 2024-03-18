#! /bin/bash

# Database access variable
PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"
echo -e "\n~~~~~ Salon Appointment Scheduler ~~~~~\n"


# Get services from database
SERVICES=$($PSQL "SELECT service_id, name FROM services")
  
# If blank, exit
if [[ -z $SERVICES ]]
  then
    # Notify user and send him to main menu
    echo -e "\nSorry, no available services to schedule at this time. Come again later."
    exit
  else
    # Greet user and offer services
    echo -e "Welcome to appointment scheduler. What can we do for you?\n"

    # Make function to list services. I'll need to repeat it for validaton
    LIST_SERVICES() {
      # If argument is passed, means it's being repeated so I need additional message
      if [[ $1 ]]
      then
        echo -e "\nPlease select a valid service number."
      fi

      # Will pipe servies to a while loop
       # Using read put them into seperate variables so I can customize the output
       # Bar is needed to eliminate the | from the database output
      echo "$SERVICES" | while read SERVICE_ID BAR NAME
      do
       echo "$SERVICE_ID) $NAME"
      done
      # Get input from user
      read SERVICE_ID_SELECTED

      # If input is not a number, repeat the function
      if [[ $SERVICE_ID_SELECTED =~ ^[0-9]+$ ]]
      then 
        # Check if service exists. If not, repeat the function
        SERVICE_VALIDATION=$($PSQL "SELECT service_id FROM services WHERE service_id=$SERVICE_ID_SELECTED")
        if [[ -z $SERVICE_VALIDATION ]]
        then
          LIST_SERVICES repeat
        fi
      else
        LIST_SERVICES repeat
      fi
    }   

    # List services
    LIST_SERVICES
    
    # Get users's phone
    echo -e "What is your phone number?"
    read CUSTOMER_PHONE
    # Check database if user already exist and pipe it to sed to remove spaces from retrieved database data
    CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone='$CUSTOMER_PHONE'")

    # If phone does not exists, I'll need to create new user
    if [[ -z $CUSTOMER_NAME ]]
    then
      # Get user name
      while [[ -z $CUSTOMER_NAME ]]
      do
        echo -e "\nLooks like we dont have you in our records. What is your name?"
        read CUSTOMER_NAME
      done
      # Update database
      INSERT_NEW_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(name, phone) VALUES('$CUSTOMER_NAME','$CUSTOMER_PHONE')")
      # Check for issues and alert user in case something went wrong during saving into database
      if [[ ! $INSERT_NEW_CUSTOMER_RESULT == "INSERT 0 1" ]]
      then
        echo -e "\nSomething went wrong $CUSTOMER_NAME, please come again later."
        exit
      fi
    fi
    # Get customer's id
    CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$CUSTOMER_PHONE'")
    # Get chosen service name and pipe it to sed to remove spaces from retrieved database data
    SERVICE_NAME=$($PSQL "SELECT name FROM services WHERE service_id='$SERVICE_ID_SELECTED'")

    # Ask for time
    while [[ -z $SERVICE_TIME ]]
    do
      echo -e "\nWhat time would you like to schedule for $SERVICE_NAME, $CUSTOMER_NAME?"
      read SERVICE_TIME
    done

    # Update database
    INSERT_NEW_APPOINTMENT_RESULT=$($PSQL "INSERT INTO appointments(customer_id,service_id,time) VALUES('$CUSTOMER_ID','$SERVICE_ID_SELECTED','$SERVICE_TIME')")
      # Check for issues and alert user in case something went wrong during saving into database
    if [[ ! $INSERT_NEW_APPOINTMENT_RESULT == "INSERT 0 1" ]]
    then
      echo -e "\nSomething went wrong $CUSTOMER_NAME, please come again later."
      exit
    fi
    # Inform user with message from the test
    echo -e "\nI have put you down for a $SERVICE_NAME at $SERVICE_TIME, $CUSTOMER_NAME."
  fi