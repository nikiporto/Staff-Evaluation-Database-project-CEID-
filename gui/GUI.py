#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import mysql.connector 
from tkinter import *



#administrator interface  
def administrator_screen():
    global administrator_screen
    administrator_screen=Toplevel(root)
    administrator_screen.title("Administrator")
    administrator_screen.geometry("300x250")
    a=Button(administrator_screen,text="Add user", height="2", width="30",command=add_user).pack()
    b=Button(administrator_screen,text="Add company", height="2", width="30",command=add_company).pack()    
    #c=Button(administrator_screen,text="Add item", height="2", width="30",command=add_item).pack()        
    d=Button(administrator_screen,text="Add field", height="2", width="30",command=add_field).pack()   


def field_insert():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    #cursor.execute("INSERT INTO field(ftitle,perigrafi,jobid) VALUES(%s,%s,%s)" ,(title_entry.get(),perigrafi_entry.get(),jobid_entry.get()))
    sql="INSERT INTO field(ftitle,perigrafi,jobid) VALUES(%s,%s,%s)"
    val=(title_entry.get(),perigrafi_entry.get(),jobid_entry.get())
    cursor.execute(sql, val)
    
    db.commit()

def add_field():
    global add_field_screen
    add_field_screen=Toplevel(administrator_screen)
    add_field_screen.title("Add field")
    add_field_screen.geometry("300x400")
    
    global title_entry
    global perigrafi_entry
    global jobid_entry
    
    
    Label(add_field_screen, text="Enter field title ").pack()
    title_entry = Entry(add_field_screen)
    title_entry.pack()
    
    Label(add_field_screen, text="Enter field description ").pack()
    perigrafi_entry = Entry(add_field_screen)
    perigrafi_entry.pack()
    
    Label(add_field_screen, text="Enter jobid for the field  ").pack()
    jobid_entry = Entry(add_field_screen)
    jobid_entry.pack()
     
    Button(add_field_screen,text="Insert", height="2", width="30",command=field_insert).pack()  
    

    
def company_insert():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                    password = "",
                                  db ="StaffEvaluation")
    
    cursor = db.cursor()
    
    sql="INSERT INTO company (companyName,afm,DOY,phonenumber,country,town,street,arithmos) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(cm_entry.get(),afm_entry.get(),dou_entry.get(),phonenumber_entry.get(),country_entry.get(),town_entry.get(),street_entry.get(),arithmos_entry.get())
    cursor.execute(sql, val)
    
    db.commit()
  
    
    
def add_company():
    global add_company_screen
    add_company_screen=Toplevel(administrator_screen)
    add_company_screen.title("Add company")
    add_company_screen.geometry("300x400")
    
    
   
    
    Label(add_company_screen, text="Enter company name ").pack()
    global cm_entry
    cm_entry = Entry(add_company_screen)
    cm_entry.pack()
    
    Label(add_company_screen, text="Enter company afm ").pack()
    global afm_entry
    afm_entry = Entry(add_company_screen)
    afm_entry.pack()
    
    Label(add_company_screen, text="Enter the doy of the company ").pack()
    global dou_entry
    dou_entry = Entry(add_company_screen)
    dou_entry.pack()
    
    Label(add_company_screen, text="Enter company's phone ").pack()
    global phonenumber_entry
    phonenumber_entry = Entry(add_company_screen)
    phonenumber_entry.pack()
    
    Label(add_company_screen, text="Enter company country ").pack()
    global country_entry
    country_entry = Entry(add_company_screen)
    country_entry.pack()
    
    Label(add_company_screen, text="Enter company town").pack()
    global town_entry
    town_entry = Entry(add_company_screen)
    town_entry.pack()
    
    Label(add_company_screen, text="Enter company street  ").pack()
    global street_entry
    street_entry = Entry(add_company_screen)
    street_entry.pack()
    
    Label(add_company_screen, text="Enter arithmos").pack()
    global arithmos_entry
    arithmos_entry = Entry(add_company_screen)
    arithmos_entry.pack()
    
    Button(add_company_screen,text="Insert", height="2", width="30",command=company_insert).pack()

    
def user_insert():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
   
    sql="INSERT INTO user (username,name,surname,email,sign_in_date,password) VALUES(%s,%s,%s,%s,%s,%s)"
    val=(username_entry.get(),name_entry.get(),surname_entry.get(),email_entry.get(),currfdate_entry.get(),passoword_entry.get())
    cursor.execute(sql, val)
    
    db.commit()


def add_user():
    global add_user_screen
    add_user_screen=Toplevel(administrator_screen)
    add_user_screen.title("Add user")
    add_user_screen.geometry("300x400")
    
    
    Label(add_user_screen, text="Enter username ").pack()
    global username_entry
    username_entry= Entry(add_user_screen)
    username_entry.pack()
    
    Label(add_user_screen, text="Enter name").pack()
    global name_entry
    name_entry = Entry(add_user_screen)
    name_entry.pack()
    
    Label(add_user_screen, text="Enter surname").pack()
    global surname_entry
    surname_entry = Entry(add_user_screen)
    surname_entry.pack()
    
    Label(add_user_screen, text="Enter email").pack()
    global email_entry
    email_entry = Entry(add_user_screen)
    email_entry.pack()
    
    Label(add_user_screen, text="Enter current date").pack()
    global currfdate_entry 
    currfdate_entry  = Entry(add_user_screen)
    currfdate_entry .pack()
    
    Label(add_user_screen, text="Enter password ").pack()
    global passoword_entry
    passoword_entry = Entry(add_user_screen)
    passoword_entry.pack()
    Button(add_user_screen,text="Insert", height="2", width="30",command=user_insert).pack()    
    
#-------------------------------------------------------------------------------------------------------------------------------    
#employee interface
def employee_screen():
    global employee_screen
    employee_screen=Toplevel(root)
    employee_screen.title("Employee")
    employee_screen.geometry("300x250")
    Button(employee_screen,text="See file", height="2", width="30",command=see_file).pack()
    Button(employee_screen,text="Update profile", height="2", width="30",command=update_profile).pack()    
    Button(employee_screen,text="Apply for job possition", height="2", width="30",command=applyforjob).pack()        
    Button(employee_screen,text="See applications", height="2", width="30",command=see_applications).pack()   
    Button(employee_screen,text="Delete application", height="2", width="30",command=delete_application).pack()

def see_file():
    global file_screen
    file_screen=Toplevel(employee_screen)
    file_screen.title("Your profile")
    file_screen.geometry("300x250")
    db = mysql.connector.connect(host ="localhost",
                                    user = "root",
                                    password = "",
                                    db ="StaffEvaluation")
 
    cursor = db.cursor()
    sql="SELECT* FROM user WHERE username='%s'"%(Username.get())
    cursor.execute(sql)
    myresult = cursor.fetchall()
    
    
    for i in myresult:
        Label(file_screen, text=i).pack()

    db.close()
    print(myresult)
    
    
def update_passw():
    
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE user SET password=%s WHERE username=%s"
    val=(passw_entry.get(),Username.get())
    cursor.execute(sql, val)
    
    db.commit()
    
def update_bio():
    
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE employe SET cv=%s WHERE em_username=%s"
    val=(bio_entry.get(),Username.get())
    cursor.execute(sql, val)
    
    db.commit()
    
    
def update_profile():
    global ufile_screen
    ufile_screen=Toplevel(employee_screen)
    ufile_screen.title("Update your profile")
    ufile_screen.geometry("300x250")
    
    Label(ufile_screen, text="Enter new password").pack()
    global passw_entry
    passw_entry = Entry(ufile_screen)
    passw_entry.pack()
    Button(ufile_screen,text="Update",height="2",width="30",command=update_passw).pack()
    
    
    Label(ufile_screen, text="Enter new bio").pack()
    global bio_entry
    bio_entry = Entry(ufile_screen)
    bio_entry.pack()
    Button(ufile_screen,text="Update",height="2",width="30",command=update_bio).pack()
    



def insert_requests():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="INSERT INTO requests(em_username,jobid) VALUES(%s,%s)"
    val=(Username.get(),job_entry.get())
    cursor.execute(sql, val)
    
    db.commit()
    
    
    
def applyforjob():
    global applies_screen
    applies_screen=Toplevel(employee_screen)
    applies_screen.title("Application")
    applies_screen.geometry("300x250")
    
    global job_entry
    
    Label(applies_screen, text="Enter the job id you want to apply for ").pack()
    job_entry = Entry(applies_screen)
    job_entry.pack()
    Button(applies_screen,text="Apply",height="2",width="30",command=insert_requests).pack()
    


def see_applications():   
    global seeappl_screen
    seeappl_screen=Toplevel(employee_screen)
    seeappl_screen.title("Your Applications")
    seeappl_screen.geometry("300x250")
        
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
   
    cursor = db.cursor()
    sql="SELECT * FROM requests WHERE em_username = '%s' "%(Username.get())
    cursor.execute(sql)
    myresult = cursor.fetchall()
    
    for i in myresult:
        Label(seeappl_screen, text=i).pack()

    db.close()
    print(myresult)
   
   
    

def delete_a():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="DELETE FROM requests WHERE em_username = %s AND jobid=%s"
    val=(Username.get(),joba_entry.get())
    cursor.execute(sql, val)
    
    db.commit()
    
    
    
    
def delete_application():
    global deleteappli_screen
    deleteappli_screen=Toplevel(employee_screen)
    deleteappli_screen.title("Delete application")
    deleteappli_screen.geometry("300x250")
    
    global joba_entry
    
    
    Label(deleteappli_screen, text="Enter the job id of the application you want to delete").pack()
    joba_entry = Entry(deleteappli_screen)
    joba_entry.pack()
    Button(deleteappli_screen,text="Delete",height="2",width="30",command=delete_a).pack()
#-------------------------------------------------------------------------------------------------------------------------------
#manager
def manager_screen():
    global manager_screen
    manager_screen=Toplevel(root)
    manager_screen.title("Manager")
    manager_screen.geometry("300x500")
    
    Button(manager_screen,text="Update my company", height="2", width="30",command=update_company).pack() 
    Button(manager_screen,text="Update my profile", height="2", width="30",command=update_mprofile).pack()    
    Button(manager_screen,text="Update salary", height="2", width="30",command=update_salary).pack()
    Button(manager_screen,text="See evaluation results", height="2", width="30",command=see_finalresults).pack()
    Button(manager_screen,text="See avarage grade of evaluator", height="2", width="30",command=mesos_evaluator).pack()
    Button(manager_screen,text="Update employee's profile", height="2", width="30",command=update_eprofile).pack()
    Button(manager_screen,text="See evaluation info", height="2", width="30",command=procedure_one).pack()

    
    
def update_mpassw():
    
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE user SET password=%s WHERE username=%s"
    val=(mpassw_entry.get(),Username.get())
    cursor.execute(sql, val)
    
    db.commit()
    
def update_memail():
    
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE user SET email=%s WHERE username=%s"
    val=(memail_entry.get(),Username.get())
    cursor.execute(sql, val)
    
    db.commit()
        
    
def update_mprofile():
    global mfile_screen
    mfile_screen=Toplevel(manager_screen)
    mfile_screen.title("Update your profile")
    mfile_screen.geometry("300x250")
    
    Label(mfile_screen, text="Enter new password").pack()
    global mpassw_entry
    mpassw_entry = Entry(mfile_screen)
    mpassw_entry.pack()
    Button(mfile_screen,text="Update",height="2",width="30",command=update_mpassw).pack()
    
    
    Label(mfile_screen, text="Enter new email").pack()
    global memail_entry
    memail_entry = Entry(mfile_screen)
    memail_entry.pack()
    Button(mfile_screen,text="Update",height="2",width="30",command=update_memail).pack()
    

def update_s():
        
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE job_position SET salary=%s WHERE jobid=%s"
    val=(salary_entry.get(),majobid_entry.get())
    cursor.execute(sql, val)
    
    db.commit()
    
    
def update_salary():
    global salary_screen
    salary_screen=Toplevel(manager_screen)
    salary_screen.title("Update salary ")
    salary_screen.geometry("300x250")
    
    Label(salary_screen, text="Enter the jobid ").pack()
    global majobid_entry
    majobid_entry = Entry(salary_screen)
    majobid_entry.pack()
    
    Label(salary_screen, text="Enter new salary").pack()
    global salary_entry
    salary_entry = Entry(salary_screen)
    salary_entry.pack()
    Button(salary_screen,text="Update",height="2",width="30",command=update_s).pack()
        
def company_update():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE company SET phonenumber=%s,country=%s,town=%s,street=%s,arithmos=%s WHERE m_username='%s'"%(nphonenumber_entry.get(),ncountry_entry.get(),ntown_entry.get(),nstreet_entry.get(),narithmos_entry.get(),Username.get())
    #val=(nphonenumber_entry.get(),ncountry_entry.get(),ntown_entry.get(),nstreet_entry.get(),narithmos_entry.get(),Username.get())
    cursor.execute(sql)
    
    db.commit()
        
def update_company():
    global update_company_screen
    update_company_screen=Toplevel(manager_screen)
    update_company_screen.title("Update company")
    update_company_screen.geometry("300x400")
    
    
    Label(update_company_screen, text="Enter new company's phone ").pack()
    global nphonenumber_entry
    nphonenumber_entry = Entry(update_company_screen)
    nphonenumber_entry.pack()
    
    Label(update_company_screen, text="Enter new company country ").pack()
    global ncountry_entry
    ncountry_entry = Entry(update_company_screen)
    ncountry_entry.pack()
    
    Label(update_company_screen, text="Enter new company town").pack()
    global ntown_entry
    ntown_entry = Entry(update_company_screen)
    ntown_entry.pack()
    
    Label(update_company_screen, text="Enter new company street  ").pack()
    global nstreet_entry
    nstreet_entry = Entry(update_company_screen)
    nstreet_entry.pack()
    
    Label(update_company_screen, text="Enter new arithmos").pack()
    global narithmos_entry
    narithmos_entry = Entry(update_company_screen)
    narithmos_entry.pack()
    
    Button(update_company_screen,text="Update", height="2", width="30",command=company_update).pack()
  
    

def see_finalresults():   
    global results_screen
    results_screen=Toplevel(manager_screen)
    results_screen.title("Evaluotion Results")
    results_screen.geometry("300x250")
        
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="SELECT * FROM evaluationresult"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    
    for i in myresult:
        Label(results_screen, text=i).pack()

    db.close()
    print(myresult)

def procedure_mesos():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    val=eval_user.get() 
    cursor.callproc('mesos',val)
    
    for result in cursor.stored_results():
            i=result.fetchall()
            Label(average_screen, text=i).pack()
    db.close()
    
    
    
    

def mesos_evaluator():  
    global average_screen
    average_screen=Toplevel(manager_screen)
    average_screen.title("Average grade per evaluator")
    average_screen.geometry("300x250")
      
    Label(average_screen, text="Enter Evaluator username").pack()
    global eval_user
    eval_user= Entry(average_screen)
    eval_user.pack()
    
    Button(average_screen,text="Enter", height="2", width="30",command=procedure_mesos).pack()
    

def update_empl():
    
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE employe SET certifications=%s,cv=%s,achievement=%s WHERE em_username=%s"
    val=(ecert_entry.get(),ecv_entry.get(),each_entry.get(),eusern_entry.get())
    cursor.execute(sql,val)
    
    db.commit()
       
    
    
    
def update_eprofile():
    global efile_screen
    efile_screen=Toplevel(manager_screen)
    efile_screen.title("Update employee's profile")
    efile_screen.geometry("300x250")
    
    Label(efile_screen, text="Enter employee username").pack()
    global eusern_entry
    eusern_entry = Entry(efile_screen)
    eusern_entry.pack()
    
    Label(efile_screen, text="Enter new cv").pack()
    global ecv_entry
    ecv_entry = Entry(efile_screen)
    ecv_entry.pack()
    
    Label(efile_screen, text="Enter new achiviement").pack()
    global each_entry
    each_entry = Entry(efile_screen)
    each_entry.pack()
    
    Label(efile_screen, text="Enter new certification").pack()
    global ecert_entry
    ecert_entry = Entry(efile_screen)
    ecert_entry.pack()
    
    
    Button(efile_screen,text="Update", height="2", width="30",command=update_empl).pack() 
    

def call_prone():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    val=(pname_entry.get(),psur_entry.get()) 
    cursor.callproc('employee',val)

    for result in cursor.stored_results():
            i=result.fetchall()
            Label(procedureone_screen, text=i).pack()
    db.close()
    


    
    
    
def procedure_one():
    global procedureone_screen
    procedureone_screen=Toplevel(manager_screen)
    procedureone_screen.title("Evaluotion info")
    procedureone_screen.geometry("300x250")
    
    Label(procedureone_screen,text="Enter employee name").pack()
    global pname_entry
    pname_entry = Entry(procedureone_screen)
    pname_entry.pack()
    
    Label(procedureone_screen, text="Enter employee surname").pack()
    global psur_entry
    psur_entry = Entry(procedureone_screen)
    psur_entry.pack()
    
    Button(procedureone_screen,text="Enter", height="2", width="30",command=call_prone).pack()
    #for i in sv:
     #   Label(procedureone_screen, text=i).pack()
    

    
    
    
    
#-------------------------------------------------------------------------------------------------------------------------------
 #evaluator   

def evaluator_screen():
    global evaluator_screen
    evaluator_screen=Toplevel(root)
    evaluator_screen.title("Evaluator")
    evaluator_screen.geometry("300x500")
    
    Button(evaluator_screen,text="See my profile", height="2", width="30",command=evaluator_profile).pack() 
    Button(evaluator_screen,text="Update my profile", height="2", width="30",command=eval_update).pack()    
    Button(evaluator_screen,text="Update a job possition anouncation", height="2", width="30",command=update_announces).pack()
    Button(evaluator_screen,text="Announce job possition", height="2", width="30",command=announce_job).pack()
    Button(evaluator_screen,text="See my announces", height="2", width="30",command=see_my_announces).pack()
    Button(evaluator_screen,text="Evaluation Results", height="2", width="30",command= pro_two).pack()
    Button(evaluator_screen,text="See status of evaluations", height="2", width="30",command=pro_three).pack()
    Button(evaluator_screen,text="See all job announces", height="2", width="30",command=see_all_anounces).pack()
  

def evaluator_profile():
    global evprofile_screen
    evprofile_screen=Toplevel(evaluator_screen)
    evprofile_screen.title("Your profile")
    evprofile_screen.geometry("300x250")
    db = mysql.connector.connect(host ="localhost",
                                    user = "root",
                                    password = "",
                                    db ="StaffEvaluation")
 
    cursor = db.cursor()
    sql="SELECT* FROM user WHERE username='%s'"%(Username.get())
    cursor.execute(sql)
    myresult = cursor.fetchall()

    
    for i in myresult:
        Label(evprofile_screen, text=i).pack()

    db.close()
    print(myresult)
    
    

def update_eval():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE user SET name=%s,surname=%s,email=%s,password=%s WHERE username=%s"
    val=(eva_name.get(),eva_surname.get(),eva_mail.get(),eva_pass.get(),Username.get())
    cursor.execute(sql, val)
    
    db.commit()
    
    
    
    
def eval_update():   
    global eva_screen
    eva_screen=Toplevel(evaluator_screen)
    eva_screen.title("Update my profile")
    eva_screen.geometry("300x250")
    
    Label(eva_screen, text="Enter new name").pack()
    global eva_name
    eva_name = Entry(eva_screen)
    eva_name.pack()
    
    Label(eva_screen, text="Enter new surname").pack()
    global eva_surname
    eva_surname = Entry(eva_screen)
    eva_surname.pack()
    
    Label(eva_screen, text="Enter new email").pack()
    global eva_mail
    eva_mail = Entry(eva_screen)
    eva_mail.pack()
    
    Label(eva_screen, text="Enter new password").pack()
    global eva_pass
    eva_pass = Entry(eva_screen)
    eva_pass.pack()


    Button(eva_screen,text="Update", height="2", width="30",command=update_eval).pack() 
    
def update_antable():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="UPDATE announces SET closedate=%s WHERE username=%s AND jobid=%s "
    val=(close_date.get(),Username.get(),job_update.get())
    cursor.execute(sql, val)
    
    db.commit()
    
    
 
def update_announces():
    global update_announces
    update_announces=Toplevel(evaluator_screen)
    update_announces.title("Update an announcation")
    update_announces.geometry("300x250")
    
    Label(update_announces, text="Enter the job id you want to update").pack()
    global job_update
    job_update = Entry(update_announces)
    job_update.pack()
   
    Label(update_announces, text="Enter new deadline for application").pack()
    global close_date
    close_date = Entry(update_announces)
    close_date.pack()
   
    Button(update_announces,text="Update", height="2", width="30",command=update_antable).pack() 


def insert_announces():    
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    sql="INSERT INTO announces(username,jobid,opendate,closedate) VALUES(%s,%s,%s,%s)"
    val=(Username.get(),ann_job.get(),ann_open.get(),ann_close.get())
    cursor.execute(sql, val)
    
    db.commit()
    
def announce_job():
    global announce_job
    announce_job=Toplevel(evaluator_screen)
    announce_job.title("Announce job possiton")
    announce_job.geometry("300x250")
    
    Label(announce_job, text="Enter the job possition id").pack()
    global ann_job
    ann_job = Entry(announce_job)
    ann_job.pack()
       
    Label(announce_job, text="Enter start date of requests").pack()
    global ann_open
    ann_open = Entry(announce_job)
    ann_open.pack()
        
    Label(announce_job, text="Enter deadline for the requests").pack()
    global ann_close
    ann_close = Entry(announce_job)
    ann_close.pack()
    
    Button(announce_job,text="Update", height="2", width="30",command=insert_announces).pack()
    
def see_my_announces():
    global seemyannounces_screen
    seemyannounces_screen=Toplevel(evaluator_screen)
    seemyannounces_screen.title("My announces")
    seemyannounces_screen.geometry("300x250")
    db = mysql.connector.connect(host ="localhost",
                                    user = "root",
                                    password = "",
                                    db ="StaffEvaluation")
 
    cursor = db.cursor()
    sql="SELECT* FROM announces WHERE username='%s'"%(Username.get())
    cursor.execute(sql)
    myresult = cursor.fetchall()

    
    for i in myresult:
        Label(seemyannounces_screen, text=i).pack()

    db.close()
    print(myresult)
    
def call_pro_two():
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    val=(pro_two_eval.get(),pro_two_job.get(),)
    cursor.callproc('sumofevaluation',val)

    for result in cursor.stored_results():
            i=result.fetchall()
            Label(pro_two, text=i).pack()
    db.close()
    
    
    
def pro_two():
    global pro_two
    pro_two=Toplevel(evaluator_screen)
    pro_two.title("Evaluation results")
    pro_two.geometry("300x250")
    
    Label(pro_two, text="Enter your id").pack()
    global pro_two_eval
    pro_two_eval = Entry(pro_two)
    pro_two_eval.pack()
    
    Label(pro_two, text="Enter job id").pack()
    global pro_two_job
    pro_two_job = Entry(pro_two)
    pro_two_job.pack()
    
    Button(pro_two,text="Enter", height="2", width="30",command=call_pro_two).pack()
    

    
def call_pr_three():   
    db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
    
    cursor = db.cursor()
    val=(pro_job.get(),)
    cursor.callproc('evaluationStatus',val)

    for result in cursor.stored_results():
            i=result.fetchall()
            Label(pro_three, text=i).pack()
    db.close()
    

def pro_three():    
    global pro_three
    pro_three=Toplevel(evaluator_screen)
    pro_three.title("Evaluation Status")
    pro_three.geometry("300x250")
    
    Label(pro_three, text="Enter the jobid you want to see status for").pack()
    global pro_job
    pro_job = Entry(pro_three)
    pro_job.pack()
    
    Button(pro_three,text="Enter", height="2", width="30",command=call_pr_three).pack()


    
    
    
    
def see_all_anounces():
    global see_all_anounces
    see_all_anounces=Toplevel(evaluator_screen)
    see_all_anounces.title("All job anounces")
    see_all_anounces.geometry("300x250")
    db = mysql.connector.connect(host ="localhost",
                                    user = "root",
                                    password = "",
                                    db ="StaffEvaluation")
 
    cursor = db.cursor()
    sql="SELECT* FROM announces"
    cursor.execute(sql)
    myresult = cursor.fetchall()

    
    for i in myresult:
        Label(see_all_anounces ,text=i).pack()

    db.close()
    print(myresult)
    
    
    
#-------------------------------------------------------------------------------------------------------------------------------    
def submitact():
     
    user = Username.get()
    passw = password.get()
  
    print(f"The name entered by you is {user} {passw}")
  
    logintodb(user, passw)
  
 
def logintodb(user, passw):
  
    # If paswword is enetered by the 
    # user
    if passw:
        db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "",
                                     db ="StaffEvaluation")
        cursor = db.cursor()
       
    #If no password is enetered by the
     #user
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     db ="StaffEvaluation")
        cursor = db.cursor()
    
    
    
    sql="SELECT password FROM user WHERE username='%s'"%(Username.get())
    cursor.execute(sql)
    
    check= cursor.fetchall()
    for row in check:
        check=str((row[0]))
  



    
    if passw==check:
    
    
         if user=="ABernard":
                administrator_screen()
        
         elif user=="AMartin" or user=="RHoward" or user=="TFlenderson" : 
                evaluator_screen()
    
         elif user=="MScott" or user=="JLevinson" or user=="SHudson" :     
                manager_screen()
    
         else:
                employee_screen()

    else:
        wrong=Label(root ,text="WRONG PASSWORD!").pack()
               


root = Tk()
root.geometry("300x300")
root.title("Account Login")

# Definging the first row
lblfrstrow = Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
global Username 
Username = Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
 
submitbtn = Button(root, text ="Login",bg ='purple', command =submitact )
submitbtn.place(x = 150, y = 135, width = 55)
 
root.mainloop()

  


# In[ ]:





# In[ ]:




