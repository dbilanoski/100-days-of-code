Dbname: salon
Three tables:

1. customers
  * customer_id, serial
  * phone, varchar, unique
  * name, varchar(50)

2. appointments
  * appointment_id, serial
  * time, varchar
  * service_id foreign key
  * customer_id foreign key

3. services
  * service_id, serial
  * name, varchar(50)
  * put three services to work with


```sql
psql --username=freecodecamp --dbname=postgres

-- Create database
create database salon;
\c salon

-- Create tables
create table customers(
  customer_id serial primary key not null,
  phone varchar(15) unique not null,
  name varchar(50) not null
);

create table services(
  service_id serial primary key not null,
  name varchar(50)
);

create table appointments(
  appointment_id serial primary key not null,
  time varchar(20),
  service_id int references services(service_id) not null,
  customer_id int references customers(customer_id) not null
);

-- Insert needed values into services table
insert into services(name) values
  ('Service 1'),
  ('Service 2'),
  ('Service 3');

```