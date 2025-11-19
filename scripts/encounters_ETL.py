import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.dialects.mssql.information_schema import columns
from sqlalchemy.testing.suite import PrecisionIntervalTest

SERVER_NAME = 'Emi_Bamboo'
DB_NAME = 'HospitalM'
SCHEMA_NAME = 'dbo'
TABLE_NAME = 'Encounters'
FILE_NAME = r'C:\EMI_\GitHub_repos\Hospital-Patient-Records\data\encounters.csv'


data_types = {
            'Id': 'object',
            'PATIENT': 'object',
            'ORGANIZATION': 'object',
            'PAYER': 'object',
            'ENCOUNTERCLASS': 'object',
            'CODE': 'object',
            'DESCRIPTION': 'object',
            'BASE_ENCOUNTER_COST': 'float64',
            'TOTAL_CLAIM_COST': 'float64',
            'PAYER_COVERAGE': 'float64',
            'REASONCODE': 'object',

}

df = pd.read_csv(FILE_NAME, sep = ',', dtype=data_types)

df.rename(columns={
                    "Id":"EncounterID",
                    "PATIENT":"PatientID",
                    "PAYER":"PayerID",
                    "ORGANIZATION":"ProviderID",
                    "ENCOUNTERCLASS":"EncounterType",
                    "CODE": "ProcedureCode",
                    "DESCRIPTION": "Notes",
                    "REASONCODE": "DiagnosisCode",
                    "TOTAL_CLAIM_COST": "TotalCost",
                    "BASE_ENCOUNTER_COST": "EcounterCost",
                    "PAYER_COVERAGE": "PayerCoverage",
                    },
          inplace=True)
df.drop(columns = ["START", "STOP", "REASONDESCRIPTION"], inplace = True)

sql_connection_string = (f'mssql+pyodbc://@{SERVER_NAME}/{DB_NAME}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
engine = create_engine(sql_connection_string)

with engine.connect() as connection:
    connection.execute(text(f"TRUNCATE TABLE [{TABLE_NAME}]"))
    connection.commit()


df.to_sql(name = TABLE_NAME, con = engine, if_exists = 'replace',  index=False)
