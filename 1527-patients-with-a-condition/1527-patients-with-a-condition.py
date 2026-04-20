import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Use str.contains with regex to find 'DIAB1' at the start or after a space
    condition = patients['conditions'].str.contains(r'^DIAB1|\sDIAB1', regex=True)
    return patients[condition]