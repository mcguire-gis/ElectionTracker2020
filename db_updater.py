#!python3

import urllib.request
import psycopg2

senate_download = 'C:\\Users\\amcguire\\Desktop\\Election\\data\\senate.txt'
pres_download = 'C:\\Users\\amcguire\\Desktop\\Election\\data\\president.txt'
house_download = 'C:\\Users\\amcguire\\Desktop\\Election\\data\\house.txt'

urllib.request.urlretrieve('https://electionresultsfiles.sos.state.mn.us/20201103/ussenate.txt',senate_download)
urllib.request.urlretrieve('https://electionresultsfiles.sos.state.mn.us/20201103/uspres.txt',pres_download)
urllib.request.urlretrieve('https://electionresultsfiles.sos.state.mn.us/20201103/ushouse.txt',house_download)

conn = psycopg2.connect(dbname="postgres",user='postgres',password="#$yeBt8wdt6Q", host = "localhost", port='5432')
uc = conn.cursor()  #update_cursor
uc.execute("delete from public.senate where \"OrderCode\" > 0;")
senate_to_table = open(senate_download)
uc.copy_from(senate_to_table,'public.senate',sep=";")
senate_to_table.close()
uc.execute("delete from public.president where \"OrderCode\" > 0;")
pres_to_table = open(pres_download)
uc.copy_from(pres_to_table,'public.president',sep=";")
uc.execute("delete from public.house where \"OrderCode\" > 0;")
pres_to_table.close()
house_to_table = open(house_download)
uc.copy_from(house_to_table,'public.house',sep=";")
house_to_table.close()

conn.commit()

uc.close()
conn.close()
