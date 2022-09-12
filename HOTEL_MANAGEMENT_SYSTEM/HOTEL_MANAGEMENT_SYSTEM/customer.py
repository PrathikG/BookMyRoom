from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Cust_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


     #variables------------------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()   
        self.var_mother=StringVar()   
        self.var_gender=StringVar()   
        self.var_post=StringVar()   
        self.var_mobile=StringVar()   
        self.var_email=StringVar()   
        self.var_nationality=StringVar()   
        self.var_address=StringVar()   
        self.var_id_proof=StringVar()   
        self.var_id_number=StringVar()   


    #title
        lbl_title=Label(self.root, text="ADD CUSTOMER DETAILS", font= ("times new roman", 18, "bold"),bg="#66A2BA",fg="#243A47",bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

    #logo

        img2=Image.open (r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\logo.jpeg")
        img2=img2.resize((100,40), Image. ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

    #label_frame

        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",font= ("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5,y=50,width=425, height=490)

    #label and entries

    #custRef

        lbl_cust_ref=Label(labelframeleft, text="Customer Ref:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font= ("arial", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

    #cust name

        cname=Label(labelframeleft, text="Customer Name:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        cname.grid(row=1, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable =self.var_cust_name, width=29, font= ("arial", 13, "bold"))
        entry_ref.grid(row=1, column=1)

    #mother name

        lblmname=Label(labelframeleft, text="Mother Name:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblmname.grid(row=2, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_mother, width=29, font= ("arial", 13, "bold"))
        entry_ref.grid(row=2, column=1)

    #gender combobox

        lbl_gender=Label(labelframeleft, text="Gender:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lbl_gender.grid(row=3, column=0, sticky=W)
        
        combo_gender=ttk.Combobox(labelframeleft, textvariable= self.var_gender, font= ("arial", 12, "bold"), width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")  
        combo_gender.current(0)            
        combo_gender.grid(row=3, column=1)
      

    #postcode

        lblPostCode=Label(labelframeleft, text="Post Code:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblPostCode.grid(row=4, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_post, width=29, font= ("arial", 13, "bold"))
        entry_ref.grid(row=4, column=1)

    #mobileNumber

        lblMobile=Label(labelframeleft, text="Mobile Number:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblMobile.grid(row=5, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font= ("arial", 13, "bold"))
        entry_ref.grid(row=5, column=1)


    #email

        lblEmail=Label(labelframeleft, text="Email:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblEmail.grid(row=6, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font= ("arial", 13, "bold"))
        entry_ref.grid(row=6, column=1)

    #nationality

        lblNationality=Label(labelframeleft, text="Nationality:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font= ("arial", 12, "bold"), width=27,state="readonly")
        combo_Nationality["value"]=("India","United Kingdom","Canada","America","Germany","Sri Lanka","Antartica")  
        combo_Nationality.current(0)            
        combo_Nationality.grid(row=7, column=1)



    #idproof type combobox

        lblIdProof=Label(labelframeleft, text="Id Proof Type:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_gender=ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font= ("arial", 12, "bold"), width=27,state="readonly")
        combo_gender["value"]=("Aadhar Card","Pan Card","Driving License")  
        combo_gender.current(0)            
        combo_gender.grid(row=8, column=1)
                                   


    #id number

        lblIdNumber=Label(labelframeleft, text="Id Number:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblIdNumber.grid(row=9, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=29, font= ("arial", 13, "bold"))
        entry_ref.grid(row=9, column=1)



    #Address

        lblAddress=Label(labelframeleft, text="Address:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblAddress.grid(row=10, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font= ("arial", 13, "bold"))
        entry_ref.grid(row=10, column=1)      

    #buttons------------------------------------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412, height=40)

        btnAdd=Button(btn_frame,text="Add", command=self.add_data, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnAdd.grid(row=0, column=0, padx=1)


        btnUpdate=Button(btn_frame,text="Update",command=self.update, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)


        btnDelete=Button(btn_frame,text="Delete",command=self.delete1, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnDelete.grid(row=0, column=2, padx=1)


        btnReset=Button(btn_frame,text="Reset",command=self.reset, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnReset.grid(row=0, column=3, padx=1)       


        #tableFrame and search system

        Table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Or Search Details",font= ("arial", 12, "bold"), padx=2)
        Table_frame.place(x=435,y=50,width=860, height=490)


        lblSearchBy=Label(Table_frame, text="Search:", font= ("arial", 12, "bold"), bg="red", fg="white" )        
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2) 

        self.search_var=StringVar()

        combo_search=ttk.Combobox(Table_frame, textvariable=self.search_var, font= ("arial", 12, "bold"), width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")  
        combo_search.current(0)            
        combo_search.grid(row=0, column=1, padx=2)
        
        self.txt_search=StringVar()
        entry_search=ttk.Entry(Table_frame, textvariable=self.txt_search, width=24, font= ("arial", 13, "bold"))
        entry_search.grid(row=0, column=2, padx=2)

        btnSearch=Button(Table_frame,text="Search", command=self.search, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnSearch.grid(row=0, column=3, padx=1)


        btnShowAll=Button(Table_frame,text="Show All", command=self.fetch_data, font=("arial",11,"bold"),bg="#66A2BA", fg="#243A47", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)
       

#show data table
        detail_table=Frame(Table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=860, height=350)


        scroll_x=ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.Cust_Details= ttk.Treeview(detail_table, column=("ref","name", "mother", "gender", "post", "mobile", "email","nationality","id proof", "id number", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
          
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details.xview)
        scroll_y.config(command=self.Cust_Details.yview)

        self.Cust_Details.heading("ref",text="Refer No")
        self.Cust_Details.heading("name",text="Name")
        self.Cust_Details.heading("mother",text="Mother Name")
        self.Cust_Details.heading("gender",text="Gender")
        self.Cust_Details.heading("post",text="Post Code")
        self.Cust_Details.heading("mobile",text="Mobile Number")
        self.Cust_Details.heading("email",text="Email")
        self.Cust_Details.heading("nationality",text="Nationlaity")
        self.Cust_Details.heading("id proof",text="Id Proof")
        self.Cust_Details.heading("id number",text="Id Number")
        self.Cust_Details.heading("address",text="Address")

        self.Cust_Details["show"]="headings"

        self.Cust_Details.column("ref",width=100)
        self.Cust_Details.column("name",width=100)
        self.Cust_Details.column("mother",width=100)
        self.Cust_Details.column("gender",width=100)
        self.Cust_Details.column("post",width=100)
        self.Cust_Details.column("mobile",width=100)
        self.Cust_Details.column("email",width=100)
        self.Cust_Details.column("nationality",width=100)
        self.Cust_Details.column("id proof",width=100)
        self.Cust_Details.column("id number",width=100)
        self.Cust_Details.column("address",width=100)

        self.Cust_Details.pack(fill=BOTH, expand=1)
        self.Cust_Details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
          if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
          else:
            try:
                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                     self.var_ref.get(),
                                                                                     self.var_cust_name.get(),
                                                                                     self.var_mother.get(),
                                                                                     self.var_gender.get(),
                                                                                     self.var_post.get(),
                                                                                     self.var_mobile.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_nationality.get(),
                                                                                     self.var_id_proof.get(),
                                                                                     self.var_id_number.get(),
                                                                                     self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                

                messagebox.showinfo("Success","customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)


    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from customer")
                rows= my_cursor.fetchall()
                if len(rows)!=0:
                    self.Cust_Details.delete(*self.Cust_Details.get_children())
                    for i in rows:
                        self.Cust_Details.insert("",END, values=i)

                    conn.commit()
                conn.close() 



    def get_cursor(self, events=""):
        cursor_row= self.Cust_Details.focus()
        content=self.Cust_Details.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Please Enter Your Mobile Number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
            my_cursor=conn.cursor()  
            my_cursor.execute("update customer set Name=%s, Mother=%s, Gender=%s, PostCode=%s,Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s where Ref=%s",(
                                                                                     
                                                                                     self.var_cust_name.get(),
                                                                                     self.var_mother.get(),
                                                                                     self.var_gender.get(),
                                                                                     self.var_post.get(),
                                                                                     self.var_mobile.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_nationality.get(),
                                                                                     self.var_id_proof.get(),
                                                                                     self.var_id_number.get(),
                                                                                     self.var_address.get() ,
                                                                                     self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()    
            messagebox.showinfo("Update","Customer details have been updated successfully",parent=self.root)
            


        
    def delete1(self):
        delete1=messagebox.askyesno("Hotel Management System", "Do you to delete this customer", parent=self.root)
        if delete1>0:
            conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
            my_cursor=conn.cursor() 
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete1:
                return
        conn.commit()
        self.fetch_data()
        conn.close()  


    def reset(self):

        

        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
         conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
         my_cursor=conn.cursor()
         
         my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.Cust_Details.delete(*self.Cust_Details.get_children())
             for i in rows:
                 self.Cust_Details.insert("",END, values=i)
         conn.commit()

         conn.close()    


if __name__ == "__main__":
    root=Tk()
    obj=Cust_window(root)
    root.mainloop()