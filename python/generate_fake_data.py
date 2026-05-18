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