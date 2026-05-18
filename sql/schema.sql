CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    city VARCHAR(100),
    insurance_type VARCHAR(50)
);

CREATE TABLE providers (
    provider_id INT PRIMARY KEY,
    provider_name VARCHAR(100),
    specialty VARCHAR(100)
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    provider_id INT,
    appointment_date TIMESTAMP,
    scheduled_time TIMESTAMP,
    check_in_time TIMESTAMP,
    visit_start_time TIMESTAMP,
    visit_end_time TIMESTAMP,
    status VARCHAR(50),

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id),

    FOREIGN KEY (provider_id)
    REFERENCES patients(provider_id)
);

CREATE TABLE billing (
    billing_id INT PRIMARY KEY,
    appointment_id INT PRIMARY KEY,
    amount DECIMAL(10,2),
    paid_amount DECIMAL(10,2),
    payment_status VARCHAR(50),

    FOREIGN KEY (appointment_id)
    REFERENCES appointments(appointment_id)
);