import pandas as pd

# Clean appointments data
appointments = pd.read_csv(
    "../data/raw/appointments.csv"
)

print(appointments.head())

print("\nMissing values:")
print(appointments.isnull().sum())

appointments.drop_duplicates(inplace=True)

# Convert datetime columns

datetime_columns = [
    "appointment_date",
    "scheduled_time",
    "check_in_time",
    "visit_start_time",
    "visit_end_time"
]

for col in datetime_columns:
    appointments[col] = pd.to_datetime(appointments[col])


# Create wait_time_minutes

appointments["wait_time_minutes"] = ( appointments["visit_start_time"] - appointments["check_in_time"] ).dt.total_seconds() / 60

# Create visit_duration_minutes

appointments["visit_duration_minutes"] = ( appointments["visit_end_time"] - appointments["visit_start_time"]).dt.total_seconds() / 60

# Handle negative values

appointments = appointments[
    (appointments["wait_time_minutes"] >= 0) & 
    (appointments["visit_duration_minutes"] >= 0)
]

appointments.to_csv(
    "../data/cleaned/appointments_cleaned.csv",
    index=False
)

print("\nappointments_cleaned.csv saved")


# Clean patients data
patients = pd.read_csv(
    "../data/raw/patients.csv"
)

print("\nMissing values:")
print(patients.isnull().sum())

patients.drop_duplicates(inplace=True)

# Data normalization
patients["gender"] = patients["gender"].str.strip().str.title()
patients["city"] = patients["city"].str.strip().str.title()
patients["insurance_type"] = patients["insurance_type"].str.strip().str.title()

patients.to_csv("../data/cleaned/patients_cleaned.csv", index=False)
# Saves cleaned version to a new file
print("\npatients_cleaned.csv saved")


# Clean providers data
providers = pd.read_csv(
    "../data/raw/providers.csv"
)

print("\nMissing values:")
print(providers.isnull().sum())
providers.drop_duplicates(inplace=True)

providers.to_csv(
    "../data/cleaned/providers_cleaned.csv",
    index=False
)

print("\nproviders_cleaned.csv saved")


# Clean billing data
billing = pd.read_csv(
    "../data/raw/billing.csv"   
)

print("\nMissing values:")
print(billing.isnull().sum())

billing.drop_duplicates(inplace=True)

billing["outstanding_balance"] = ( billing["amount"] - billing["paid_amount"] )

billing.to_csv(
    "../data/cleaned/billing_cleaned.csv",
    index=False
)

print("\nbilling_cleaned.csv saved")
