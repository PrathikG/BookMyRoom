from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #================var================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofday=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        

        
    #title
        lbl_title=Label(self.root, text="ROOM BOOKING", font= ("times new roman", 18, "bold"),bg="#66A2BA",fg="#243A47",bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

    #logo

        img2=Image.open (r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\logo.jpeg")
        img2=img2.resize((100,40), Image. ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        #label_frame

        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking",font= ("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5,y=50,width=425, height=490)


         #label and entries

    #custContact

        lbl_cust_contact=Label(labelframeleft, text="Customer Contact:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact=ttk.Entry(labelframeleft, width=20, textvariable=self.var_contact, font= ("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

      #Fetch button

        btnAdd=Button(labelframeleft,text="Get Data", command= self.Fetch_contact, font=("arial",9,"bold"),bg="#66A2BA", fg="#243A47", width=8)
        btnAdd.place(x=345, y=4)
  

     #check in date

        check_in_date=Label(labelframeleft, text="Check_In Date", font= ("arial", 12, "bold"), padx=2, pady=6)        
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft, textvariable=self.var_checkin, width=29, font= ("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)


     #check out date

        check_out_date=Label(labelframeleft, text="Check_Out Date", font= ("arial", 12, "bold"), padx=2, pady=6)        
        check_out_date.grid(row=2, column=0, sticky=W)

        txtcheck_out_date=ttk.Entry(labelframeleft, textvariable=self.var_checkout, width=29, font= ("arial", 13, "bold"))
        txtcheck_out_date.grid(row=2, column=1)   


     #Room Type

        lbl_RoomType=Label(labelframeleft, text="Room Type:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lbl_RoomType.grid(row=3, column=0, sticky=W)

        conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        rows1= my_cursor.fetchall()

        
        combo_RoomType=ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font= ("arial", 12, "bold"), width=27,state="readonly")
        combo_RoomType["value"]=rows1
        combo_RoomType.current(0)            
        combo_RoomType.grid(row=3, column=1)   
   
   #Available Rooms

        lblRoomsAvailable=Label(labelframeleft, text="Available Rooms:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblRoomsAvailable.grid(row=4, column=0, sticky=W)

        # txtRoomsAvailable=ttk.Entry(labelframeleft, textvariable= self.var_roomavailable, width=29, font= ("arial", 13, "bold"))
        # txtRoomsAvailable.grid(row=4, column=1)

        conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows= my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font= ("arial", 12, "bold"), width=27,state="readonly")
        combo_RoomNo["value"]=rows 
        combo_RoomNo.current(0)            
        combo_RoomNo.grid(row=4, column=1)   

   #Meal

        lblMeal=Label(labelframeleft, text="Meal:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblMeal.grid(row=5, column=0, sticky=W)

        combo_Meal=ttk.Combobox(labelframeleft, textvariable=self.var_meal, font= ("arial", 12, "bold"), width=27,state="readonly")
        combo_Meal["value"]=("breakfast","lunch","dinner")  
        combo_Meal.current(0)            
        combo_Meal.grid(row=5, column=1)  


   #No of days

        lblNoOfDays=Label(labelframeleft, text="No Of Days:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays=ttk.Entry(labelframeleft, textvariable= self.var_noofday,  width=29, font= ("arial", 13, "bold"))
        txtNoOfDays.grid(row=6, column=1)    

       #Paid Tax

        lblNoOfDays=Label(labelframeleft, text="Paid Tax:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblNoOfDays.grid(row=7, column=0, sticky=W)

        txtNoOfDays=ttk.Entry(labelframeleft, textvariable = self.var_paidtax, width=29, font= ("arial", 13, "bold"))
        txtNoOfDays.grid(row=7, column=1) 

         #Sub total

        lblSubTotal=Label(labelframeleft, text="Sub Total:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal=ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, width=29, font= ("arial", 13, "bold"))
        txtSubTotal.grid(row=8, column=1)               


        #Total Cost

        lblIDNumber=Label(labelframeleft, text="Total Cost:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblIDNumber.grid(row=9, column=0, sticky=W)

        txtIDNumber=ttk.Entry(labelframeleft, textvariable=self.var_total,  width=29, font= ("arial", 13, "bold"))
        txtIDNumber.grid(row=9, column=1)  

        #======================bill btn===============================
        btnAdd=Button(labelframeleft,text="Total", command=self.total, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnAdd.grid(row=10, column=0, padx=1, sticky=W)  

        btnBill=Button(labelframeleft,text="Bill", command=self.bill1, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnBill.grid(row=10, column=1, padx=1, sticky=W)  

                   


        #button values

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412, height=40)

        btnAdd=Button(btn_frame,text="Add", command=self.add_data, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnAdd.grid(row=0, column=0, padx=1)


        btnUpdate=Button(btn_frame,text="Update", command=self.update, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)


        btnDelete=Button(btn_frame,text="Delete", command=self.delete1, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset=Button(btn_frame,text="Reset", command=self.reset, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnReset.grid(row=0, column=3, padx=1) 

        #Right side img====================================

        img3=Image.open (r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\bedd.jpg")
        img3=img3.resize((730,230), Image. ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling3=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling3.place(x=760,y=55,width=530,height=230)


        #search System===============================

        Table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Or Search Details",font= ("arial", 12, "bold"), padx=2)
        Table_frame.place(x=435,y=280,width=860, height=250)


        lblSearchBy=Label(Table_frame, text="Search:", font= ("arial", 12, "bold"), bg="red", fg="white" )        
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2) 

        self.search_var=StringVar()

        combo_search=ttk.Combobox(Table_frame, textvariable=self.search_var, font= ("arial", 12, "bold"), width=24,state="readonly")
        combo_search["value"]=("Contact","Room")  
        combo_search.current(0)            
        combo_search.grid(row=0, column=1, padx=2)
        
        self.txt_search=StringVar()
        entry_search=ttk.Entry(Table_frame, textvariable=self.txt_search, width=24, font= ("arial", 13, "bold"))
        entry_search.grid(row=0, column=2, padx=2)



        btnSearch=Button(Table_frame,text="Search", command=self.search, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnSearch.grid(row=0, column=3, padx=1)


        btnShowAll=Button(Table_frame,text="Show All", command=self.fetch_data, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)



        #show data table=-============================================
        detail_table=Frame(Table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=860, height=180)


        scroll_x=ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.room_table= ttk.Treeview(detail_table, column=("contact","checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
          
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")
     

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

#------------------------Add--------------------------------------------------------

    def add_data(self):
          if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
          else:
            try:
                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                       self.var_contact.get(),
                                                                       self.var_checkin.get(),
                                                                       self.var_checkout.get(),
                                                                       self.var_roomtype.get(),
                                                                       self.var_roomavailable.get(),
                                                                       self.var_meal.get(),
                                                                       self.var_noofday.get(),


                     
                ))    
                                                                                     
                                
                conn.commit()
                self.fetch_data()
                conn.close()
                

                messagebox.showinfo("Success","room successfully booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)



 #-----------------------fetch_data----------------------------------               


    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from room")
                rows= my_cursor.fetchall()
                if len(rows)!=0:
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert("",END, values=i)

                    conn.commit()
                conn.close() 

 #-------------------get_cursor-----------------------------------------------------------------------------               


    def get_cursor(self, events=""):
        cursor_row= self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofday.set(row[6])



#================update_data----------------------------------------------------------


    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Please Enter Your Mobile Number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
            my_cursor=conn.cursor()  
            my_cursor.execute("update room set check_in=%s, check_out=%s, roomtype=%s, room=%s, meal=%s, noOfdays=%s where Contact=%s",(
                                                                                     
                                                                       
                                                                       self.var_checkin.get(),
                                                                       self.var_checkout.get(),
                                                                       self.var_roomtype.get(),
                                                                       self.var_roomavailable.get(),
                                                                       self.var_meal.get(),
                                                                       self.var_noofday.get(),
                                                                       self.var_contact.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()    
            messagebox.showinfo("Update","room details have been updated successfully",parent=self.root)


#==============================Delete=================================================

    def delete1(self):
        delete1=messagebox.askyesno("Hotel Management System", "Do you to delete this room", parent=self.root)
        if delete1>0:
            conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
            my_cursor=conn.cursor() 
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete1:
                return
        conn.commit() 
        self.fetch_data()
        conn.close()  

#====================================================reset=============================

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofday.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
       


            
            


#==================All Data Fetched===================================================

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter the Contact number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
            my_cursor=conn.cursor()    
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()    

                     
                showDataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=445, y=55, width=300, height=180)

                lblname=Label(showDataframe, text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0, y=0)

                lbl=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl.place(x=90,y=0)

                #==========Gender================================

                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()    
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0, y=30)

                lbl2=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl2.place(x=90,y=30)

                #==========email================================

                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()    
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0, y=60)

                lbl2=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl2.place(x=90,y=60)

                #==========Nationality================================

                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()    
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Nationality:",font=("arial",12,"bold"))
                lblGender.place(x=0, y=90)

                lbl2=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl2.place(x=90,y=90)


                #==========Address================================

                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()    
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Address:",font=("arial",12,"bold"))
                lblGender.place(x=0, y=120)

                lbl2=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl2.place(x=90,y=120)

#=====================search system========================================================

    def search(self):
         conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
         my_cursor=conn.cursor()
         
         my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.room_table.delete(*self.room_table.get_children())
             for i in rows:
                 self.room_table.insert("",END, values=i)
             conn.commit()

         conn.close()    



#------------------bill total------------------------------------------------------------------                

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate, "%d/%m/%Y")
        outDate=datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofday.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="dinner" and self.var_roomtype.get()=="double"):
            q1=(300)
            q2=(1500)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="double"):
            q1=(300)
            q2=(1500)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)    

        elif (self.var_meal.get()=="lunch" and self.var_roomtype.get()=="double"):
            q1=(300)
            q2=(1500)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="single"):
            q1=(300)
            q2=(1000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 

        elif(self.var_meal.get()=="dinner" and self.var_roomtype.get()=="single"):
            q1=(300)
            q2=(1000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="lunch" and self.var_roomtype.get()=="single"):
            q1=(300)
            q2=(1000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)           

        elif(self.var_meal.get()=="lunch" and self.var_roomtype.get()=="luxury"):
            q1=(300)
            q2=(2000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  

        elif(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="luxury"):
            q1=(300)
            q2=(2000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 

        elif(self.var_meal.get()=="dinner" and self.var_roomtype.get()=="luxury"):
            q1=(300)
            q2=(2000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." + str("%.2f"%((q5)*0.1))
            ST="Rs." + str("%.2f"%((q5)))
            TT="Rs." + str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  
     


    def bill1(self):
        if self.var_total.get()=="":
            messagebox.showerror("Error","Bill not generated")  

        else:

            conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into bill values(%s,%s,%s,%s,%s)",(
                                                                                     self.var_contact.get(),
                                                                                     self.var_roomavailable.get(),
                                                                                     self.var_paidtax.get(),
                                                                                     self.var_actualtotal.get(),
                                                                                     self.var_total.get(),
                                                                                    
                ))
            conn.commit()
            # self.fetch_data()
            conn.close()  
            messagebox.showinfo("Success","Bill Successfully Generated")   

            

        


if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()