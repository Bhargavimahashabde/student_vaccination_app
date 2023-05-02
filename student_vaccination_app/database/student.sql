CREATE DATABASE vaccination;
use vaccination_status ;
GRANT ALL on first to root@localhost;
CREATE TABLE student (
 RegNo INT PRIMARY KEY,
 Name VARCHAR(255) NOT NULL,
 Vaccination_Status ENUM('Yes', 'No') NOT NULL
);
insert into student (RegNo, Name, Vaccination_Status) VALUES
((1, 'Jay Desai', 'Yes'),
(2, 'Jyoti Shingade', 'Yes'),
(3, 'Bhargav Jagtap', 'No'),
(4, 'Sarita Lele', 'Yes'),
(5, 'Dhanu Kale', 'No'));