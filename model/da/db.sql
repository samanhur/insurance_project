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
    birth_date    date               not null,
    phone         varchar(12),
    username      nvarchar(30) unique not null,
    password      nvarchar(30) not null,
    status        tinyint
);

-- table for active customer's insurances
create table insurance_project.active_insurance
(
    active_insurance_id int primary key auto_increment,
    service            nvarchar(30) not null,
    number_of_duration int        not null,
    duration_period    varchar(7) not null,
    cost               int        not null,
    expire_date        date       not null,

    customer_id        int,
    insurance_id       int,

    foreign key (customer_id) references customers (person_id),
    foreign key (insurance_id) references insurances (insurance_id)
);

-- view for active insurances for customers
create view insurance_project.insurance_list as
select *
from insurance_project.active_insurance
         join insurance_project.customers
              on insurance_project.active_insurance.customer_id = insurance_project.customers.person_id;
