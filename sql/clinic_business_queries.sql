-- Total appointments

SELECT
    COUNT(*) AS total_appointments
FROM appointments;

-- Completed appointments

SELECT
    COUNT(*) AS completed_appointments
FROM appointments
WHERE status = 'Completed';

-- No-show appointments

SELECT
    COUNT(*) AS no_show_count
FROM appointments
WHERE status = 'No Show';

-- No-show rate

SELECT
    ROUND (100.0 * SUM(
        CASE
            WHEN status = 'No Show'
            THEN 1
            ELSE 0
        END
    ) / COUNT(*), 2) AS no_show_rate_percent
FROM appointments;

-- Average wait time

SELECT
    ROUND(
        AVG(wait_time_minutes)::numeric, 2
        ) AS avg_wait_time
FROM appointments
WHERE status ='Completed';

-- Average visit duration

SELECT
    ROUND(
        AVG(visit_duration_minutes)::numeric, 2
        ) AS avg_visit_duration
FROM appointments
WHERE status ='Completed';

-- Appointment status breakdown

SELECT
    status,
    COUNT(*) AS total
FROM appointments
GROUP BY status
ORDER BY total DESC;

-- Appointments by specialty

SELECT
    p.specialty,
    COUNT(*) AS total_appointments
FROM appointments a
JOIN providers p
ON a.provider_id = p.provider_id
GROUP BY p.specialty
ORDER BY total_appointments DESC;

-- Revenue summary

SELECT
    SUM(amount) AS total_billed,
    SUM(paid_amount) AS total_paid,
    SUM(outstanding_balance) AS total_outstanding
FROM billing;

-- Top providers by revenue

SELECT
    p.provider_name,
    SUM(b.amount) AS total_revenue
FROM billing b 
JOIN appointments a
ON b.appointment_id = a.appointment_id
JOIN providers p
ON a.provider_id = p.provider_id
GROUP BY p.provider_name
ORDER BY total_revenue DESC
LIMIT 10;

-- Patient demographics by gender

SELECT
    gender,
    COUNT(*) AS total_patients
FROM patients
GROUP BY gender;

-- Patients by insurance type

SELECT
    insurance_type,
    COUNT(*) AS total_patients
FROM patients
GROUP BY insurance_type
ORDER BY total_patients DESC;

-- No show rate by age group

SELECT
    CASE
        WHEN p.age < 18 THEN 'Under 18'
        WHEN p.age BETWEEN 18 AND 40 THEN '18-40'
        WHEN p.age BETWEEN 41 AND 65 THEN '41-65'
        ELSE '65+'
    END AS age_group,

    COUNT(*) FILTER(
        WHERE a.status = 'No Show'
    ) AS no_show_count,

    COUNT(*) AS total_appointments,

    ROUND( 100.0 * COUNT(*) FILTER(
        WHERE a.status = 'No Show'
    ) / COUNT(*), 2) AS no_show_rate
FROM appointments a
JOIN patients p
ON a.patient_id = p.patient_id
GROUP BY age_group
ORDER BY no_show_rate DESC;

-- Monthly appoinment trend

SELECT
    DATE_TRUNC(
        'month', appointment_date) AS appoinment_month,
    COUNT(*) AS total_appointments
FROM appointments
GROUP BY appoinment_month
ORDER BY appoinment_month;

-- Busiest weekdays

SELECT
    TO_CHAR(appointment_date, 'Day') AS weekday,
    COUNT(*) AS total_appointments
FROM appointments
GROUP BY weekday
ORDER BY total_appointments DESC;
