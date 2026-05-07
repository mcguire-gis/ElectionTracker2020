import pandas as pd
from sqlalchemy import create_engine
import psycopg2

dbname = 'postgres'
user = 'postgres'
password = 'bulldogs'


df_init = pd.read_csv('/home/andrew/Documents/data/initialize.txt', sep=';', index_col=False)
#df_senate = pd.read_csv('/home/andrew/Documents/data/senate.txt', sep=';')
#df_house = pd.read_csv('/home/andrew/Documents/data/house.txt', sep=';')
races = ['president','senate','house']

engine = create_engine(f'postgresql://{user}:{password}@127.0.0.1:5432/{dbname}')
conn = psycopg2.connect(dbname=dbname,user=user,password=password, host = "localhost", port='5432')
uc = conn.cursor()  #update_cursor

for r in races:
	print("Drop table",r,"if exists")
	uc.execute("""DROP TABLE IF EXISTS """+r+""";""")
	conn.commit()
	print("Creating public."+r)
	df_init.to_sql(r,engine,index=False)
	print("Table created")
	
uc.close()
conn.close()
print("Tables initialized, finished")
