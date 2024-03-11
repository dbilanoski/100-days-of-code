#!/bin/bash
# From the FCC's Relatonal Databases course "Learn SQL by Building a Student Database: Part 1" module
# Script to insert data from courses.csv and students.csv into students database

# This will be used to access database
PSQL="psql -X --username=<username> --dbname=students --no-align --tuples-only -c"
# Clear tables from the students database
echo $($PSQL "TRUNCATE students, majors, courses, majors_courses")

# Cat the csv then pipe it to a while loop to MAJOR and COURSE variables while setting comma as a delimiter
cat courses.csv | while IFS="," read MAJOR COURSE
do
  # To avoid adding csv headers to the db, we test if the entry is equal to the header name
  if [[ $MAJOR != "major" ]]
  then
    # Get major_id by quering the database with major name from the csv
    MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")

    # if not found, insert major, id will be created in the database
    if [[ -z $MAJOR_ID ]]
    then
      # Insert major
      INSERT_MAJOR_RESULT=$($PSQL "INSERT INTO majors(major) VALUES('$MAJOR')")
      # If insertion was successful, alert user
      if [[ $INSERT_MAJOR_RESULT == "INSERT 0 1" ]]
      then
        echo Inserted into majors, $MAJOR
      fi

      # Now get new major_id
      MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")
    fi

    # Get course_id from the db
    COURSE_ID=$($PSQL "SELECT course_id FROM courses WHERE course='$COURSE'")

    # if not found, insert course to the db
    if [[ -z $COURSE_ID ]]
    then
      # Insert course
      INSERT_COURSE_RESULT=$($PSQL "INSERT INTO courses(course) VALUES('$COURSE')")
      # If insertion was successful, alert user
      if [[ $INSERT_COURSE_RESULT == "INSERT 0 1" ]]
      then
        echo Inserted into courses, $COURSE
      fi

      # Get new course_id
      COURSE_ID=$($PSQL "SELECT course_id FROM courses WHERE course='$COURSE'")
    fi

    # Insert into majors_courses
    INSERT_MAJORS_COURSES_RESULT=$($PSQL "INSERT INTO majors_courses(major_id, course_id) VALUES($MAJOR_ID, $COURSE_ID)")
    if [[ $INSERT_MAJORS_COURSES_RESULT == "INSERT 0 1" ]]
    then
      echo Inserted into majors_courses, $MAJOR : $COURSE
    fi
  fi
done

# Cat the students.csv then pipe it to a while loop to FIRST, LAST, MAJOR and GPA variables while setting comma as a delimiter
cat students.csv | while IFS="," read FIRST LAST MAJOR GPA
do
  # To avoid adding csv headers to the db, we test if the entry is equal to the header 
if [[ $FIRST != "first_name" ]]
then
  # Get major_id
  MAJOR_ID=$($PSQL "SELECT major_id FROM majors WHERE major='$MAJOR'")

  # if not found, set id to null
  if  [[ -z $MAJOR_ID ]]
  then
    # Set to null
    MAJOR_ID=null
  fi
  # Insert student  
  INSERT_STUDENT_RESULT=$($PSQL "INSERT INTO students(first_name,last_name,major_id,gpa) VALUES ('$FIRST','$LAST',$MAJOR_ID,$GPA)")
  # If insertion was sucessfull, alert user
  if [[ $INSERT_STUDENT_RESULT == "INSERT 0 1" ]]
  then
    echo Inserted into students, $FIRST $LAST
  fi
fi
done