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
    - star: star_id, solar_system_id, galaxy_id, name, age, diameter_in_km, type
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
  galaxy_id serial not null,
  name varchar(30) not null unique,
  age int,
  size_in_ly numeric(15,2) not null,
  type text not null,
  has_black_holes boolean
);

create table solar_system(
  solar_system_id serial not null,
  galaxy_id int not null,
  name varchar(30) not null unique,
  age int,
  size_in_km numeric(15,2) not null
);

create table star(
  star_id serial not null,
  solar_system_id int not null,
  galaxy_id int not null,
  name varchar(30) not null unique,
  age int,
  diameter_in_km numeric(15,2) not null,
  type varchar(30) not null
);

create table planet(
  planet_id serial not null,
  star_id int not null,
  name varchar(30) not null unique,
  age int,
  diameter_in_km numeric(15,2) not null,
  has_water boolean,
  has_life boolean
);

create table moon(
  moon_id serial not null,
  planet_id int not null,
  name varchar(30) not null unique,
  age int,
  diameter_in_km numeric(15,2) not null,
  has_atmosphere boolean
);

-- Set primary and foregin keys
alter table galaxy add primary key(galaxy_id);

alter table solar_system add primary key(solar_system_id);
alter table solar_system add foreign key(galaxy_id) references galaxy(galaxy_id);

alter table star add primary key(star_id);
alter table star add foreign key(galaxy_id) references galaxy(galaxy_id);
alter table star add foreign key(solar_system_id) references solar_system(solar_system_id);

alter table planet add primary key(planet_id);
alter table planet add foreign key(star_id) references star(star_id);


alter table moon add primary key(moon_id);
alter table moon add foreign key(planet_id) references planet(planet_id);


-- Add data
-- Those with requirement of six rows
insert into galaxy(galaxy_id,name,age,size_in_ly,type,has_black_holes) values
  (1,'Galaxy 001',5056000,6866585.29,'Spiral',true),
  (2,'Galaxy 002',6500200,5766585.12,'Elliptical',true),
  (3,'Galaxy 003',10005501,4566585.80,'Spiral',false),
  (4,'Galaxy 004',205600,5566585.99,'Irregular',false),
  (5,'Galaxy 005',99022006,3566585.25,'Barred',false),
  (6,'Galaxy 006',5040068,4565585.36,'Spiral',true);

insert into solar_system(solar_system_id,galaxy_id,name,age,size_in_km) values
  (1,1,'Solar System 001',100050,12123385.29),
  (2,2,'Solar System 002',2500300,1226585.12),
  (3,3,'Solar System 003',300501,6321585.80),
  (4,4,'Solar System 004',203600,658544.99),
  (5,5,'Solar System 005',11020002,5855455.25),
  (6,6,'Solar System 006',3040012,52323585.36);

insert into star(star_id,solar_system_id,name,age,diameter_in_km,type) values
  (1,1,'Star 001',5056000,6866585.29,'Spiral'),
  (2,2,'Star 002',6500200,5766585.12,'Elliptical'),
  (3,3,'Star 003',10005501,4566585.80,'Spiral'),
  (4,4,'Star 004',205600,5566585.99,'Irregular'),
  (5,5,'Star 005',99022006,3566585.25,'Barred'),
  (6,6,'Star 006',5040068,4565585.36,'Spiral');

-- Those with requirement of 12 rows and 20 rows
insert into planet(planet_id,star_id,name,age,diameter_in_km,has_water,has_life) values
  (1,1,'Planet 001',205000,6865.29,false,false),
  (2,2,'Planet 002',3105500,66365.27,false,false),
  (3,3,'Planet 003',650500,55565.31,true,true),
  (4,4,'Planet 004',30600,23245.41,true,false),
  (5,5,'Planet 005',120500,7965.55,false,false),
  (6,6,'Planet 006',325000,66965.66,false,false),
  (7,1,'Planet 007',665000,683265.00,true,true),
  (8,2,'Planet 008',8000,6988.77,false,false),
  (9,3,'Planet 009',105000,5565.46,false,false),
  (10,4,'Planet 010',523000,1225.69,false,false),
  (11,5,'Planet 011',206600,3165.99,false,false),
  (12,6,'Planet 012',2056800,56865.12,true,false);

insert into moon(moon_id,planet_id,name,age,diameter_in_km,has_atmosphere) values
  (1,1,'Moon 001',16000,65.29,false),
  (2,2,'Moon 002',2600,123.19,false),
  (3,3,'Moon 003',3500,321.21,true),
  (4,4,'Moon 004',456000,11.22,false),
  (5,5,'Moon 005',5600,55.23,false),
  (6,6,'Moon 006',6600,569.24,false),
  (7,6,'Moon 007',1600,1232.26,true),
  (8,7,'Moon 008',288000,22.49,false),
  (9,7,'Moon 009',36000,116.59,false),
  (10,8,'Moon 010',46000,1998.69,false),
  (11,9,'Moon 011',16200,556.25,false),
  (12,10,'Moon 012',26020,332.24,false),
  (13,11,'Moon 013',36001,123.23,false),
  (14,11,'Moon 014',96002,622.22,false),
  (15,11,'Moon 015',86003,699.29,false),
  (16,12,'Moon 016',7630,652.11,true),
  (17,1,'Moon 017',66004,989.32,false),
  (18,1,'Moon 018',560005,695.65,false),
  (19,12,'Moon 019',36060,165.55,false),
  (20,3,'Moon 020',36070,3365.99,false);

-- Export database to a file
--- pg_dump -cC --inserts -U freecodecamp universe > universe.sql 