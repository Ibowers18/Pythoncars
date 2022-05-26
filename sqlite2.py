###Imported files
import sqlite3
import csv
import sys

###Command Line Arguments
print(sys.argv)
print(len(sys.argv))

###SQLite Database
###Connect to the database
conn = sqlite3.connect('cars2.db')

###Create a cursor
c = conn.cursor()
'''
###Create Table for cars2 ###
c.execute("""CREATE TABLE IF NOT EXISTS cars2 ( 
        dim_hgt integer,
        dim_lnt integer,
        dim_wdt integer,
        enginf_drvlin text,
        enginf_engtyp text,
        enginf_hyb integer,
        enginf_numfwdgrs integer,   
        enginf_trm text,
        fulinf_ctympg integer,   
        fulinf_fultyp text,
        fulinf_hwympg integer,
        idn_cls text,  
        idn_id text,
        idn_mke text,
        idn_mdlyer text,
        idn_yer integer,
        enginf_engstthpw integer,
        enginf_engstttor integer
        )""")
'''

#def dynamic_data_entry():
#       c.execute("INSERT INTO cars2 (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_hyb, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, idn_yer, enginf_engstthpw, enginf_engstttor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)",
####            (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_hyb, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, idn_yer, enginf_engstthpw, enginf_engstttor))   

def dynamic_data_entry(row_values):
    c.execute("INSERT INTO cars2 (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_hyb, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, idn_yer, enginf_engstthpw, enginf_engstttor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)", row_values)



with open('cars2.csv', 'r+', newline='') as csvfile:
    carreader2 = csv.reader(csvfile, delimiter=',', quotechar='|') 

#Step over first Line in file - Headers 
    cars2 = iter(carreader2)
    next(cars2)


    for row in cars2:   
        dynamic_data_entry(row)

        
'''
#DELETE Columns "enginf_hyb integer" and "idn_yer integer" 
#from cars2 table

ALTER TABLE cars2
DROP COLUMNS enginf_hyb;idn_yer; 
'''
##    
#        print("carreader2",carreader2)
#        for row in carreader2:
#            print("row",row)
#            for item in row:        
#                print("item",item)
##   

###Inserting car data into table ###
#
#               def dynamic_data_entry(row_values):
#                       c.execute("INSERT INTO cars2 (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_hyb, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, idn_yer, enginf_engstthpw, enginf_engstttor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)", row_values)
#                   
#                #    (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_hyb, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, idn_yer, enginf_engstthpw, enginf_engstttor)) 
##


 


##
#                c.execute:(f"INSERT INTO cars2 VALUES{row}") 
#                print(f"INSERT INTO cars2 VALUES {row}")
#                print(', '.join(row)) 
##

###Test Inserting data into table 
#c.execute("INSERT INTO cars2 VALUES ('140','143','202','All-wheel drive','Audi 3.2L 6 cyliner 250hp 236ft-lbs','True','6','6 Speed Automatic Select Shift','18','Gasoline','25','Automatic transmission','2009 Audi A3 3.2','Audi','2009 Audi A3','2009','250','236')")

###Test data has been insert into table
#print("Data Added to table") 
    

    
###def dynamic_data_entry():
###    c.execute("INSERT INTO cars2 (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_hyb, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, idn_yer, enginf_engstthpw, enginf_engstttor) VALUES, (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)",
###               (dim_hgt, dim_lnt, dim_wdt, enginf_drvlin, enginf_engtyp, enginf_hyb, enginf_numfwdgrs, enginf_trm, fulinf_ctympg, fulinf_fultyp, fulinf_hwympg, idn_cls, idn_id, idn_mke, idn_mdlyer, idn_yer, enginf_engstthpw, enginf_engstttor))
                   


#FetchAll and print the data
#                c.execute("SELECT * FROM cars2")
#                print(c.fetchall()) 



#items = c.fetchall()
#for item in items:
#    print(item)


###Exceptions###
#try:
#    f = open('corrupt_file.txt')
   
#except FileNotFoundError as e:
#except Exception as e:
#print(e)

###Commit code
conn.commit()

###Close cursor
c.close()

### Close file
conn.close()

print("Job Complete!")