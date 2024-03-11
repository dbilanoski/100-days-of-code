## Plan


Two tables:
  1. teams
    * team_id serial primary key not null
    * name unique not null
   
  2. games
    * game_id serial primary key not null
    * year int not null
    * round varchar not null
    * winner_goals int not null
    * opponent_goals int not null
    * winner_id foreign key referencing team_id from teams not null
    * opponent_id foreign key referencing team_id from teams not null


## STEPS

```sql

-- Create Database
CREATE DATABASE worldcup;
-- \c worldcup

-- Create tables
CREATE TABLE teams(
  team_id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(50) NOT NULL UNIQUE
)

CREATE TABLE games(
  game_id SERIAL PRIMARY KEY NOT NULL,
  year INT NOT NULL,
  round VARCHAR(50) NOT NULL,
  winner_goals INT NOT NULL,
  opponent_goals INT NOT NULL,
  winner_id INT REFERENCES teams(team_id) NOT NULL,
  opponent_id INT REFERENCES teams(team_id) NOT NULL
)

```