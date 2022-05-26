###Imported files
import sqlite3
import csv
import sys

#print(f"Name of the script          : {sys.argv[0]=}")
#print(f"Arguments of the script     : {sys.argv[1:]=}")

print(sys.argv)
print(len(sys.argv))


###SQLite Database
###Connect to the database
conn = sqlite3.connect('cars.db')

###Create a cursor
c = conn.cursor()

###Create Table for cars ###
#c.execute("""CREATE TABLE cars ( 
#        dim_hgt integer,
#        dim_lnt integer,
#        dim_wdt integer,
#        enginf_drvlin text,
#        enginf_engtyp text,
#        enginf_numfwdgrs integer,
#        enginf_trm text,
#        fulinf_ctympg integer,
#        fulinf_fultyp text,
#        fulinf_hwympg integer,
#        idn_cls text,
#        idn_id text,
#        idn_mke text,
#        idn_mdlyer text,
#        enginf_engstthpw integer,
#        enginf_engstttor integer
#        )""")



###Inserting car data into table ###

with open('cars.csv', newline='') as csvfile:
    carreader = csv.reader(csvfile, delimiter=',', quotechar='|')

#Step over first Line in file - Headers  
    next(carreader)
    
#    print("carreader",carreader)
    for row in carreader:
#        print("row",row)
        for item in row:        
#            print("item",item)
            c.execute:(f"INSERT INTO cars VALUES{row}") 
#        print(f"INSERT INTO cars VALUES {row}")

#        print(', '.join(row)) 


'''
with open('cars.csv', 'r', newline='') as f:
    carreader = csv.reader(f)
    for row in carreader:
        print(row[0])
'''
####with open('cars.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
####    writer.writerows(cars)

#        c.execute(f"INSERT INTO cars VALUES (row)")  
#        print(','.join(row)) 
'''
#Setting the csv mode and importing the data from cars.csv file to cars.db file
# .mode csv 
# .import c:/vzpython_project/cars.csv cars 

###Test Inserting data into table ###
###c.execute("INSERT INTO cars VALUES ('140','143','202','All-wheel drive','Audi 3.2L 6 cyliner 250hp 236ft-lbs','0','6','6 Speed Automatic Select Shift','18','Automatic transmission','2009 Audi A3 3.2','Audi','2009 Audi A3','0','250','236')")

#Test data has been insert into table
#print("Data Added to table")                 
'''    
#def dynamic_data_entry():
#    c.execute("INSERT INTO cars (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, enginf_engstthpw, enginf_engstttor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
#               (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, enginf_engstthpw, enginf_engstttor))
                    


#FetchAll and print the data
c.execute("SELECT * FROM cars")
print(c.fetchall()) 

#items = c.fetchall()
#for item in items:
#    print(item)


###Exception
#try:
#except: 
#print("")

###Commit code
conn.commit()

###Close cursor
c.close()

### Close file
conn.close()

print("Job Complete!")