# Periodic Table Database


```sql

-- Enter db
psql --username=freecodecamp --dbname=periodic_table

-- Rename cols
ALTER TABLE properties RENAME COLUMN weight TO atomic_mass;
ALTER TABLE properties RENAME COLUMN melting_point TO melting_point_celsius;


-- Add contstraints
ALTER TABLE properties ALTER COLUMN melting_point_celsius SET NOT NULL;
ALTER TABLE properties ALTER COLUMN boiling_point_celsius SET NOT NULL;
ALTER TABLE elements ADD UNIQUE(symbol);
ALTER TABLE elements ADD UNIQUE(name);
ALTER TABLE elements ALTER COLUMN symbol SET NOT NULL;
ALTER TABLE elements ALTER COLUMN name SET NOT NULL;


-- Create additional tables
CREATE TABLE types(
  type_id serial primary key,
  type varchar(30) not null
);

-- Add additional cols (will add NOT NULL once data is populated)
ALTER TABLE properties ADD COLUMN type_id INT REFERENCES types(type_id);

-- Set foreign keys
ALTER TABLE properties ADD FOREIGN KEY(atomic_number) REFERENCES elements(atomic_number);
ALTER TABLE properties ADD FOREIGN KEY(type_id) REFERENCES types(type_id);

-- Insert data to new types table
INSERT INTO types(type) VALUES
  ('nonmetal'),
  ('metal'),
  ('metalloid');

INSERT INTO elements(atomic_number, symbol, name) VALUES
  ('9','F','Fluorine'),
  ('10','Ne','Neon');

INSERT INTO properties(atomic_number,type,atomic_mass,melting_point_celsius,boiling_point_celsius) VALUES
  ('9','nonmetal','18.998','-220','-188.1'),
  ('10','nonmetal','20.18','-248.6','-246.1');

-- Add type id's to existing property entries
UPDATE properties SET type_id=(
  SELECT type_id FROM types WHERE properties.type = types.type
);

-- Set constraint of not null ti type_id
ALTER TABLE properties ALTER COLUMN type_id SET NOT NULL;

-- EDITS
-- Capitalize first letter but leave rest as is
UPDATE elements SET symbol = CONCAT(UPPER(LEFT(symbol,1)), substring(symbol,2,LENGTH(symbol)));
-- Remove trailing zeroes from decimal numbers (changing data type as per assigment but not setting scale and precision will fix adding uneccessary zeroes)
ALTER TABLE properties ALTER COLUMN atomic_mass TYPE DECIMAL;
-- Then trimming existing values to get rid of the zeroes in existing data
-- RTRIM to remove zeroes from string, second cast to convert decimal to string so RTRIM could work and first cast to rever it back to decimal for final update
UPDATE properties SET atomic_mass=CAST(RTRIM(CAST(atomic_mass AS TEXT),'0') AS DECIMAL);

```