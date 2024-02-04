-- Plan
/*
Five tables
  - galaxy, star, solar_system, planet, moon
  - primary keys: table-name_id, serial, unique, not null
  - foreign keys: 
    - galaxy: star, solar system
    - solar_sytem: galaxy, star
    - star: galaxy, solar_system
    - planet: solar_system, star
    - moon: planet
  - columns
    - galaxy: galaxy_id, name, age, size_in_ly, type, has_black_holes
    - solar_system: solar_system_id, galaxy_id, name, age, size_in_km
    - star: star_id, solar_system_id, name, age, diameter_in_km, type
    - planet: planet_id, star_id, name, age, diameter_in_km, has_water, has_life
    - moon: moon_id, planet_id, name, age, diameter_in_km, has_atmosphere
  
  - rows requirements
    - galaxy, solar system, star: 6
    - planet: 12
    - moon: 20
*/

-- Steps

create database universe;
\c universe

-- Create tables and columns
create table galaxy(
  galaxy_id serial not null
  name varchar(30) not null unique
  age int
  size_in_ly numeric(15,2) not null
  type varchar(30) not null
  has_black_holes boolean
);

create table solar_system(
  solar_system_id serial not null
  galaxy_id int not null
  name varchar(30) not null unique
  age int
  size_in_km numeric(15,2) not null
);

create table star(
  star_id serial not null
  solar_system_id int not null
  name varchar(30) not null unique
  age int
  diameter_in_km numeric(15,2) not null
  type varchar(30) not null
);

create table planet(
  planet_id serial not null
  star_id int not null
  name varchar(30) not null unique
  age int
  diameter_in_km numeric(15,2) not null
  has_water boolean
  has_life boolean
);

create table moon(
  moon_id serial not null
  planet_id int not null
  name varchar(30) not null unique
  age int
  diameter_in_km numeric(15,2) not null
  has_atmosphere boolean
);

-- Set primary and foregin keys
alter table galaxy add primary key(galaxy_id);

alter table solar_system add primary key(solar_system_id);
alter table solar_system add foregin key(galaxy_id) references solar_system(solar_system_id);

alter table star add primary key(star_id);
alter table star add foregin key(solar_system_id) references galaxy(galaxy_id);

alter table planet add primary key(planet_id);
alter table planet add foregin key(star_id) references star(star_id);


alter table moon add primary key(moon_id);
alter table moon add foregin key(planet_id) references planet(planet_id);


-- Add data
-- Those with requirement of six rows
insert into galaxy(galaxy_id,name,age,size_in_ly,type,has_black_holes)
  values(1,'Galaxy 001',5056000,6866585.29,'Spiral',true),
  values(2,'Galaxy 002',6500200,5766585.12,'Elliptical',true),
  values(3,'Galaxy 003',10005501,4566585.80,'Spiral',false),
  values(4,'Galaxy 004',205600,5566585.99,'Irregular',false),
  values(5,'Galaxy 005',99022006,3566585.25,'Barred',false),
  values(6,'Galaxy 006',5040068,4565585.36,'Spiral',true);

insert into solar_system(solar_system_id,galaxy_id,name,age,size_in_km)
  values(1,1,'Solar System 001',100050,12123385.29),
  values(2,2.'Solar System 002',2500300,1226585.12),
  values(3,3,'Solar System 003',300501,6321585.80),
  values(4,4,'Solar System 004',203600,658544.99),
  values(5,5,'Solar System 005',11020002,5855455.25),
  values(6,6,'Solar System 006',3040012,52323585.36);

insert into star(star_id,solar_system_id,name,age,diameter_in_km,type)
  values(1,1,'Star 001',5056000,6866585.29,'Spiral',true),
  values(2,2,'Star 002',6500200,5766585.12,'Elliptical',true),
  values(3,3,'Star 003',10005501,4566585.80,'Spiral',false),
  values(4,4,'Star 004',205600,5566585.99,'Irregular',false),
  values(5,5,'Star 005',99022006,3566585.25,'Barred',false),
  values(6,6,'Star 006',5040068,4565585.36,'Spiral',true);

  -- Those with requirement of six rows