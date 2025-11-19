import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.dialects.mssql.information_schema import columns
from sqlalchemy.testing.suite import PrecisionIntervalTest

SERVER_NAME = 'Emi_Bamboo'
DB_NAME = 'HospitalM'
SCHEMA_NAME = 'dbo'
TABLE_NAME = 'Payers'
FILE_NAME = r'C:\EMI_\GitHub_repos\Hospital-Patient-Records\data\payers.csv'

# df = pd.read_csv(FILE_NAME, sep = ',')
# data_types2 = {col: str(dtype) for col, dtype in df.dtypes.items()}
# print(data_types2)

data_types = {
             'ADDRESS': 'object',
             'CITY': 'object',
             'Id': 'object',
             'NAME': 'object',
             'PHONE': 'object',
             'STATE_HEADQUARTERED': 'object',
             'ZIP': 'float64'

}

df = pd.read_csv(FILE_NAME, sep = ',', dtype=data_types)

sql_connection_string = (f'mssql+pyodbc://@{SERVER_NAME}/{DB_NAME}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
engine = create_engine(sql_connection_string)

with engine.connect() as connection:
    connection.execute(text(f"TRUNCATE TABLE [{TABLE_NAME}]"))
    connection.commit()


df.to_sql(name = TABLE_NAME, con = engine, if_exists = 'replace',  index=False)

