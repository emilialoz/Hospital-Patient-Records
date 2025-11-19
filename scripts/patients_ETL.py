import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.dialects.mssql.information_schema import columns
from sqlalchemy.testing.suite import PrecisionIntervalTest

SERVER_NAME = 'Emi_Bamboo'
DB_NAME = 'HospitalM'
SCHEMA_NAME = 'dbo'
TABLE_NAME = 'Patients'
FILE_NAME = r'C:\EMI_\GitHub_repos\Hospital-Patient-Records\data\patients.csv'


#data_types = {col: str(dtype) for col, dtype in df.dtypes.items()}
#print(data_types)

data_types = {
    'ADDRESS': 'object',
     'BIRTHDATE': 'object',
     'BIRTHPLACE': 'object',
     'CITY': 'object',
     'COUNTY': 'object',
     'DEATHDATE': 'object',
     'ETHNICITY': 'object',
     'FIRST': 'object',
     'GENDER': 'object',
     'Id': 'object',
     'LAST': 'object',
     'LAT': 'float64',
     'LON': 'float64',
     'MAIDEN': 'object',
     'MARITAL': 'object',
     'PREFIX': 'object',
     'RACE': 'object',
     'STATE': 'object',
     'SUFFIX': 'object',
     'ZIP': 'float64'

}

df = pd.read_csv(FILE_NAME, sep = ',', dtype=data_types)

df.rename(columns={"COUNTY":"COUNTRY","Id": "ID"}, inplace=True)

sql_connection_string = (f'mssql+pyodbc://@{SERVER_NAME}/{DB_NAME}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
engine = create_engine(sql_connection_string)

with engine.connect() as connection:
    connection.execute(text(f"TRUNCATE TABLE [{TABLE_NAME}]"))
    connection.commit()


df.to_sql(name = TABLE_NAME, con = engine, if_exists = 'append',  index=False)

