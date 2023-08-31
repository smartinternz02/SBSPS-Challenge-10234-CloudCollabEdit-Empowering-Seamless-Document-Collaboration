# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
def showall():
    sql= "SELECT * from CLOUD"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The FIRST NAME is : ",  dictionary["FIRST NAME"])
        print("The LAST NAME is : ", dictionary["LAST NAME"])
        print("The MOBILE NO is : ",  dictionary["MOBILE NO"])
        print("The EMAIL is : ",  dictionary["EMAIL"])
        print("The PASSWORD is : ",  dictionary["PASSWORD"])  
        print("The ADDRESS is : ",  dictionary["ADDRESS"])

        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from CLOUD where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The FIRST NAME is : ",  dictionary["FIRST NAME"])
        print("The LAST NAME is : ", dictionary["LAST NAME"])
        print("The MOBILE NO is : ", dictionary["MOBILE NO"])
        print("The EMAIL is : ", dictionary["EMAIL"])
        print("The PASSWORD is : ", dictionary["PASSWORD"])
        print("The ADDRESS is : ", dictionary["ADDRESS"])
        dictionary = ibm_db.fetch_both(stmt)
        
        
def insertdb(conn,FIRSTNAME,LASTNAME,MOBILENO,EMAIL,PASSWORD,ADDRESS):
    sql= "INSERT into CLOUD VALUES('{}','{}','{}','{}','{}','{}')".format(FIRSTNAME,LASTNAME,MOBILENO,EMAIL,PASSWORD,ADDRESS )
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=vxw40712;PWD=ClTnvmBtjLhJia8n",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"Hari","Hari@gmail.com",'1234567890','Adarsh nagar','Faculty','Civil','1234567')
    getdetails("Hari@gmail.com",'1234567')
    #showall()

except:
    print("Error connecting to the database")
