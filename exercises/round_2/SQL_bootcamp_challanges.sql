-- Here will be solutions to milestone challenges from https://www.udemy.com/course/the-complete-sql-bootcamp/


-- ##############################
-- ASSESSMENT TEST 1           #
-- ############################

-- 1. Return the customer IDs of customers who have spent at least $110 with the staff member who has an ID of 2.
SELECT customer_id, SUM(amount)
FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) >= 110;
-- The answer should be customers 187 and 148. # YES


-- 2. How many films begin with the letter J?
SELECT COUNT(title) FROM film
WHERE title LIKE 'J%'
-- The answer should be 20. # YES


-- 3. What customer has the highest customer ID number whose name starts with an 'E' and has an address ID lower than 500?
SELECT first_name, last_name, customer_id, address_id
FROM customer
WHERE first_name LIKE 'E%' AND address_id < 500
ORDER BY customer_id DESC
LIMIT 1;
-- The answer is Eddie Tomlin # YES

-- ##############################
-- ASSESSMENT TEST 2           #
-- ############################

-- 1. How can you retrieve all the information from the cd.facilities table?
SELECT * FROM cd.facilities;

-- 2. You want to print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs?

SELECT name, membercost FROM cd.facilities;

-- 3. How can you produce a list of facilities that charge a fee to members?
SELECT name, membercost FROM cd.facilities
WHERE membercost != 0;
    
-- 4. How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.
SELECT facid, 
	name, 
	membercost, 
	monthlymaintenance
FROM cd.facilities
WHERE membercost > 0 AND (membercost < monthlymaintenance * 0.02)
ORDER BY monthlymaintenance DESC;

    
-- 5. How can you produce a list of all facilities with the word 'Tennis' in their name?
SELECT name FROM cd.facilities 
WHERE name LIKE '%Tennis%';
    
-- 6. How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.
SELECT * FROM cd.facilities WHERE facid IN (1,5);
    
-- 7. How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question.
SELECT memid,
	surname,
	firstname,
	joindate
FROM cd.members
WHERE joindate >= '2012-9-1'
    
-- 8. How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
SELECT DISTINCT surname FROM cd.members
ORDER BY surname
LIMIT 10;

-- 8.1. Without guests:
SELECT DISTINCT surname FROM cd.members
WHERE LOWER(surname) != 'guest'
ORDER BY surname
LIMIT 10;
    
-- 9. You'd like to get the signup date of your last member. How can you retrieve this information?
SELECT joindate FROM cd.members
ORDER BY joindate DESC
LIMIT 1
    
-- 10. Produce a count of the number of facilities that have a cost to guests of 10 or more.
SELECT count(*) FROM cd.facilities
WHERE guestcost >= 10;

-- 11. Produce a list of the total number of slots booked per facility in the month of September 2012. Produce an output table consisting of facility id and slots, sorted by the number of slots.
SELECT facid, sum(slots) AS slots_total FROM cd.bookings
WHERE starttime >= '2012-9-01' AND starttime <= '2012-9-30'
GROUP BY facid
ORDER BY slots_total DESC;

-- 12. Produce a list of facilities with more than 1000 slots booked. Produce an output table consisting of facility id and total slots, sorted by facility id.
SELECT facid, sum(slots) AS slots_total FROM cd.bookings
GROUP BY facid HAVING sum(slots) > 1000
ORDER BY facid DESC;
    
-- 13. How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.
SELECT cd.bookings.starttime, cd.facilities.name 
FROM cd.facilities 
INNER JOIN cd.bookings ON cd.facilities.facid = cd.bookings.facid
WHERE lower(cd.facilities.name) LIKE '%tennis court%' 
	AND cd.bookings.starttime >= '2012-09-21'
	AND cd.bookings.starttime <= '2012-09-22'
ORDER BY cd.bookings.starttime;

-- 14. How can you produce a list of the start times for bookings by members named 'David Farrell'?
SELECT cd.bookings.starttime,
	cd.members.firstname || ' ' || cd.members.surname AS full_name
FROM cd.bookings
INNER JOIN cd.members ON cd.bookings.memid = cd.members.memid
WHERE cd.members.firstname = 'David' AND cd.members.surname = 'Farrell';


-- ##############################
-- ASSESSMENT TEST 3           #
-- ############################

-- Welcome to your final assessment test! This will test your knowledge of the previous section, focused on creating databases and table operations. This test will actually consist of a more open-ended assignment below:

-- Complete the following task:

-- 1. Create a new database called "School" this database should have two tables: teachers and students.

  -- The students table should have columns for student_id, first_name,last_name, homeroom_number, phone,email, and graduation year.

  -- The teachers table should have columns for teacher_id, first_name, last_name,

  -- homeroom_number, department, email, and phone.

  -- The constraints are mostly up to you, but your table constraints do have to consider the following:

    -- We must have a phone number to contact students in case of an emergency.
    -- We must have ids as the primary key of the tables
    -- Phone numbers and emails must be unique to the individual.

CREATE DATABASE "School"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;


CREATE TABLE students (
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	homeroom_number VARCHAR(50),
	phone VARCHAR(50) NOT NULL UNIQUE,
	email VARCHAR(150) UNIQUE,
	graduation_year INT CHECK(graduation_year > '1900')
);

CREATE TABLE teachers (
	teacher_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	homeroom_number VARCHAR(50),
	department VARCHAR(150) NOT NULL,
	phone VARCHAR(50) NOT NULL UNIQUE,
	email VARCHAR(150) UNIQUE
);

-- 2. Once you've made the tables, insert a student named Mark Watney (student_id=1) who has a phone number of 777-555-1234 and doesn't have an email. He graduates in 2035 and has 5 as a homeroom number.

INSERT INTO students (first_name,last_name,phone,email,homeroom_number,graduation_year)
VALUES (
	'Mark','Watney','777-555-1234','','5','2035'
);


-- 3. Then insert a teacher names Jonas Salk (teacher_id = 1) who as a homeroom number of 5 and is from the Biology department. His contact info is: jsalk@school.org and a phone number of 777-555-4321.

INSERT INTO teachers (first_name,last_name,phone,email,homeroom_number,department)
VALUES (
	'Jonas','Salk','777-555-4321','jsalk@school.org','5','Biology'
);