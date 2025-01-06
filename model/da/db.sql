-- creating database
create database insurance_project;

-- a table for saving insurances
create table insurance_project.insurances
(
    insurance_id int primary key auto_increment,
    service nvarchar(30) not null ,
    number_of_duration int not null ,
    duration_period varchar(6) not null ,
    cost int not null
);

