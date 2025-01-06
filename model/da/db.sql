-- creating database
create
database insurance_project;

-- table for saving insurances
create table insurance_project.insurances
(
    insurance_id       int primary key auto_increment,
    service            nvarchar(30) not null,
    number_of_duration int        not null,
    duration_period    varchar(6) not null,
    cost               int        not null
);

-- table for saving employees information
create table insurance_project.employees
(
    person_id     int primary key auto_increment,
    name          nvarchar(30) not null,
    family        nvarchar(30) not null,
    national_code varchar(10) unique not null,
    birth_date    date               not null,
    username      nvarchar(30) unique not null,
    password      nvarchar(30) not null,
    status        tinyint,
    role          nvarchar(20),
    salary        int

);

-- table for saving admins
create table insurance_project.admins
(
    admin_id int primary key auto_increment,
    name     nvarchar(30) not null,
    family   nvarchar(30) not null,
    username nvarchar(30) not null unique,
    password nvarchar(30) not null
);

-- table for saving customers
create table insurance_project.customers
(
    person_id     int primary key auto_increment,
    name          nvarchar(30) not null,
    family        nvarchar(30) not null,
    father_name   nvarchar(30) not null,
    national_code varchar(10) unique not null,
    birth_date    date        not null,
    phone         varchar(12),
    username      nvarchar(30) unique not null,
    password      nvarchar(30) not null,
    status        tinyint
);
