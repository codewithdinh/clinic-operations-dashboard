# Generate patients data: patient_id, age, gender, city, insurance_type

import pandas as pd
import random
from faker import Faker

fake = Faker()

NUM_PATIENTS = 1000

patients = []

for patient_id in range(1, NUM_PATIENTS + 1):
    patients.append({
        "patients_id": patient_id,
        "age": random.randint(1, 90),
        "gender": random.choice(["Male", "Female"]),
        "city": fake.city(),
        "insurance_type": random.choice([
            "Private",
            "Medicare",
            "Medicaid",
            "Self-Pay"
        ])
    })

patients_df = pd.DataFrame(patients)

patients_df.to_csv(
    "../data/raw/patients.csv",
    index = False
)

print("patients.cvs generated")


# Generate providers data: provider_id, provider_name, specialty

NUM_PROVIDERS = 25

specialties = [
    "Cardiology",
    "Dermatology",
    "Pediatrics",
    "Orthopedics",
    "Neurology"
]

providers = []

for provider_id in range(1, NUM_PROVIDERS + 1):
    providers.append({
        "provider_id": provider_id,
        "provider_name": fake.name(),
        "specialty": random.choice(specialties)
    })

providers_df = pd.DataFrame(providers)

providers_df.to_csv(
    "../data/raw/providers.csv",
    index=False
)

print("providers.csv generated")


# Generate appointments data

from datetime import datetime, timedelta

NUM_APPOINTMENTS = 1000

appointments = []

statuses = [
    "Completed",
    "Cancelled",
    "No Show"
]

start_date = datetime(2025, 1, 1)

for appointment_id in range(1, NUM_APPOINTMENTS + 1):
    patient_id = random.randint(1, NUM_PATIENTS)

    provider_id = random.randint(1, NUM_PROVIDERS)

    appointment_date = start_date + timedelta(
        days=random.randint(0, 180))
    
    scheduled_time = appointment_date.replace(
        hour=random.randint(8, 16),
        minute=random.choice([0, 15, 30, 45])
    )

    status = random.choices(
        statuses,
        weights=[75, 10, 15]
    )[0]

    if status == "Completed":

        check_in_time = scheduled_time + timedelta(
            minutes=random.randint(-10, 15)
        )

        visit_start_time = check_in_time + timedelta(
            minutes=random.randint(5, 60)
        )

        visit_end_time = visit_start_time + timedelta(
            minutes=random.randint(15, 90)
        )
    
    else:
        check_in_time = None
        visit_start_time = None
        visit_end_time = None

    appointments.append({
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "provider_id": provider_id,
        "appointment_date": appointment_date,
        "scheduled_time": scheduled_time,
        "check_in_time": check_in_time,
        "visit_start_time": visit_start_time,
        "visit_end_time": visit_end_time,
        "status": status
    })

appointments_df = pd.DataFrame(appointments)

appointments_df.to_csv(
        "../data/raw/appointments.csv",
        index=False
    )

print("appointments.csv generated")


# Generate billing data: billing_id, appointment_id, amount, paid_amount, payment_status

NUM_BILLING = NUM_APPOINTMENTS

billing = []

for billing_id in range(1, NUM_BILLING):

    amount = random.randint(50, 1000)

    payment_status = random.choices(
        ["Paid", "Partial", "Unpaid"],
        weights=[75, 15, 10]
        )[0]

    if payment_status == "Paid":
        paid_amount = amount

    elif payment_status == "Partial":
        paid_amount = random.randint(1, amount - 50)

    else:
        paid_amount = 0

    billing.append({
        "billing_id": billing_id,
        "appointment_id": billing_id,
        "amount": amount,
        "paid_amount": paid_amount,
        "payment_status": payment_status
    })

billing_df = pd.DataFrame(billing)

billing_df.to_csv(
    "../data/raw/billing.csv",
    index=False
)

print("billing.csv generated")

