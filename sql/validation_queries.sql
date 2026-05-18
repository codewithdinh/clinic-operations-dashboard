SELECT *
FROM patients
LIMIT 5;

SELECT *
FROM appointments
LIMIT 5;

SELECT COUNT(*) FROM patients;

SELECT COUNT(*) FROM providers;

SELECT COUNT(*) FROM appointments;

SELECT COUNT(*) FROM billing;

SELECT
    wait_time_minutes
FROM appointments
LIMIT 10;

SELECT
    amount,
    paid_amount,
    outstanding_balance
FROM billing
LIMIT 10;