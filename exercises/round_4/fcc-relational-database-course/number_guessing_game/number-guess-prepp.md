## Tasks
1. Database with users
  * Tables: 
    * users
      * rows: user_id serial
      * name varchar(22) unique not null
    * games
      * game_id serial
      * user_id foreign from users.user_id
      * game_guesses int not null

2. Script logic
    1. Ask for a user name
    * Check the db
    * If user exist, proceed, otherwise register user to the db
    2. Generate random number between 1 and 100
    3. Create outside variable to track count of guesses
    4. Game loop
      
    * Prompt user to guess it
    * While loop until input is correct
    * If bigger or smaller, print assignment hot-cold messages
    5. Print message from assignment
    6. Update the database


## Database

```sql
-- psql --username=freecodecamp --dbname=postgres

-- Create database and connect to it
CREATE DATABASE number_guess;
/c number_guess

-- Create tables
CREATE TABLE users(
  user_id SERIAL PRIMARY KEY NOT NULL,
  name varchar(22) UNIQUE NOT NULL
);


CREATE TABLE games(
  game_id SERIAL PRIMARY KEY NOT NULL,
  user_id INT REFERENCES users(user_id),
  game_guesses INT NOT NULL
);
```