from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Bill:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


   #title
        lbl_title=Label(self.root, text="BILLING", font= ("times new roman", 18, "bold"),bg="#66A2BA",fg="#243A47",bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

    #logo

        img2=Image.open (r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\logo.jpeg")
        img2=img2.resize((100,40), Image. ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)


        
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Generate Bill",font= ("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5,y=50,width=425, height=80)


       #-----------------image------------------


        img1= Image.open(r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\hotel3.jpg")
        img1=img1.resize((1550,600),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=300,width=1550,height=350)


 
     
    #---variables-------------

        self.var_contact=StringVar()  
        self.var_room1=StringVar()  

   
    #RoomNo

        lblAddress=Label(labelframeleft, text="Room No:", font= ("arial", 12, "bold"), padx=2, pady=6)        
        lblAddress.grid(row=0, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_room1, width=24, font= ("arial", 13, "bold"))
        entry_ref.grid(row=0, column=1)      


      #Fetch button

        btnAdd=Button(labelframeleft,text="Reciept", command= self.Fetch_contact, font=("arial",9,"bold"),bg="#66A2BA", fg="#243A47", width=8)
        btnAdd.place(x=345, y=4)


    #==================All Data Fetched===================================================

    def Fetch_contact(self):
        if self.var_room1.get()=="":
            messagebox.showerror("Error","Please enter the Room number", parent=self.root)
            
        else:
            
            conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
            my_cursor=conn.cursor()    
            query=("select Contact from bill where RoomNo=%s")
            value=(self.var_room1.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()    

                     
                showDataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=445, y=55, width=300, height=180)

                lblname=Label(showDataframe, text="Contact:",font=("arial",12,"bold"))
                lblname.place(x=0, y=0)

                lbl=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl.place(x=90,y=0)

                #==========RoomNo================================

                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()    
                query=("select RoomNo from bill where RoomNo=%s")
                value=(self.var_room1.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Room No:",font=("arial",12,"bold"))
                lblGender.place(x=0, y=30)

                lbl2=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl2.place(x=90,y=30)

                #==========tax================================

                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()    
                query=("select Tax from bill where RoomNo=%s")
                value=(self.var_room1.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Tax:",font=("arial",12,"bold"))
                lblGender.place(x=0, y=60)

                lbl2=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl2.place(x=90,y=60)

                #==========Nationality================================

                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()    
                query=("select SubTotal from bill where RoomNo=%s")
                value=(self.var_room1.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Sub Total:",font=("arial",12,"bold"))
                lblGender.place(x=0, y=90)

                lbl2=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl2.place(x=90,y=90)


                #==========Total================================

                conn=mysql.connector.connect(host="localhost", user="root", passwd="root", database="management")
                my_cursor=conn.cursor()    
                query=("select Total from bill where RoomNo=%s")
                value=(self.var_room1.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Total:",font=("arial",12,"bold"))
                lblGender.place(x=0, y=120)

                lbl2=Label(showDataframe, text=row, font=("arial",12,"bold") )
                lbl2.place(x=90,y=120)

   
    
        

        
             

    
    

if __name__ == "__main__":
    root=Tk()
    obj=Bill(root)
    root.mainloop()