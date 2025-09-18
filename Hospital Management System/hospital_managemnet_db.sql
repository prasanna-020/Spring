CREATE DATABASE hospital_management_db;
USE hospital_management_db;

CREATE TABLE patients(
patient_id INT auto_increment PRIMARY KEY,
name VARCHAR(100),
age INT,
gender VARCHAR(10),
diagnosis VARCHAR(255));

CREATE TABLE appointments(
appointment_id INT auto_increment PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
notes VARCHAR(255),
foreign key (patient_id) references patients(patient_id),
foreign key (doctor_id) references doctors(doctor_id)
);

CREATE TABLE doctors(
doctor_id INT auto_increment primary KEY,
name VARCHAR(100),
speciality VARCHAR(100),
phone VARCHAR(15));

