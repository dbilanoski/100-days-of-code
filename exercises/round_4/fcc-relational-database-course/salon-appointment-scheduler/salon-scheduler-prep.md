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


