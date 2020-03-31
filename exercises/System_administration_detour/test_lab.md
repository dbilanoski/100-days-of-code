## Test lab configuration

Simple network to test out Domain Controller, Active Directory and Group .policy.

We will look at a "Hot Rod" car dealership franshise's branch located in Osijek, Croatia. 

### Scenario
A company branch with sales, management and mechancs department. Setup will be added later.

### Lab Design
- Environment: 
  - Microsoft platform 
  - Virtual environment (Virtual Box)

- Devices/Systems:
  1. Microsoft Server 2012 R2
  2. Windows 7 host
  3. Windows 7 host

- Naming convention:
  - Domain
    - Forest domain name: hotrod.test
    - Subdomain prefix: os
  - Devices:
    - Domain controller name: DC1 (domain controller 1)
  - Users
    - Username naming scheme: first-letter-of-firstname-lastname
      - eq. John Doe -> jdoe 
- IP addressing scheme:
  - Network: 172.16.2.0 /24
  - Available hosts: 254
  - IP Reservations:
    - .1 - .10 Networking devices
      - **Default Gateway:** 172.16.2.2
      - **DC01:** 172.16.2.2
    - .10 - .20 Printers
    - .30 - .254 Hosts





