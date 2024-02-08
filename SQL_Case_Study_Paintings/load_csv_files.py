import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Establish connection to postgresql database
conn_string = 'postgresql://postgres:Bhadwasur@localhost/painting'
db = create_engine(conn_string)
conn = db.connect()

# Reads csv file and puts it into dataframe df then exports data from dataframe into sql table
files = ['artist','canvas_size','image_link','museum','museum_hours','product_size','subject','work']

for file in files:
    df= pd.read_csv(f'D:/Coding/Project/SQL_Case_Study/archive/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)







