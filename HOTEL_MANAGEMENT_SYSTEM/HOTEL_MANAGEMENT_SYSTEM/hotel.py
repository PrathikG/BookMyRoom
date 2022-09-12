from tkinter import*
from PIL import Image, ImageTk
from customer import Cust_window
from room import Roombooking
from details import Details
from bill import Bill
from login import login_window


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        img1= Image.open(r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\hotel3.jpg")
        img1=img1.resize((1550,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=200)
    #logo

        img2=Image.open (r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\logo.jpeg")
        img2=img2.resize((235,175), Image. ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=230,height=140)

    #title
        lbl_title=Label(self.root, text="BOOK MY ROOM", font= ("times new roman", 40, "bold"),bg="#66A2BA",fg="yellow")
        lbl_title.place(x=0,y=140,width=1550,height=50)

    #frame
        main_frame=Frame(self.root)
        main_frame.place(x=0,y=190,width=1550,height=620)

    #menu
        
        lbl_menu=Label(main_frame, text="MENU", font= ("times new roman", 20, "bold"),bg="#B6B6B6",fg="#243A47",bd=4, relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230) 

    #btn Frame
        btn_frame=Frame(main_frame,bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=35,width=258,height=210)    

        cust_btn= Button(btn_frame,text="CUSTOMER", command=self.cust_details, width=22, font= ("times new roman", 14, "bold"),bg="#66A2BA",fg="#243A47", bd=0, cursor="hand1")    
        cust_btn.grid(row=0,column=0, pady=1)    
        
        cust_btn= Button(btn_frame,text="ROOM", command= self.room_details, width=22, font= ("times new roman", 14, "bold"),bg="#66A2BA",fg="#243A47", bd=0, cursor="hand1")    
        cust_btn.grid(row=1,column=0, pady=1) 
        
        cust_btn= Button(btn_frame,text="DETAILS", command=self.details, width=22, font= ("times new roman", 14, "bold"),bg="#66A2BA",fg="#243A47", bd=0, cursor="hand1")    
        cust_btn.grid(row=2,column=0, pady=1) 
        
        cust_btn= Button(btn_frame,text="BILLING", command=self.bill, width=22, font= ("times new roman", 14, "bold"),bg="#66A2BA",fg="#243A47", bd=0, cursor="hand1")    
        cust_btn.grid(row=3,column=0, pady=1) 
        #
        cust_btn= Button(btn_frame,text="LOGIN", command=self.login, width=22, font= ("times new roman", 14, "bold"),bg="#66A2BA",fg="#243A47", bd=0, cursor="hand1")    
        cust_btn.grid(row=4,column=0, pady=1) 

        cust_btn= Button(btn_frame,text="LOGOUT", command=self.logout, width=22, font= ("times new roman", 14, "bold"),bg="#66A2BA",fg="#243A47", bd=0, cursor="hand1")    
        cust_btn.grid(row=5,column=0, pady=1)   



    #right side image

        img3=Image.open (r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\hotel.jpg")
        img3=img3.resize((1310,590), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling1=Label(main_frame,image=self.photoimg3)
        lbling1.place(x=225,y=0,width=1310,height=590)

    #down side image

        img4=Image.open (r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\building.jpg")
        img4=img4.resize((230,210), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0, y=225,width=230,height=200)

       
        img5=Image.open (r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\food.jpg")
        img5=img5.resize((230,190), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbling1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=420,width=230,height=170)
            

    


    def cust_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Cust_window(self.new_window)


    def room_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Roombooking(self.new_window)  

    def details(self):
      self.new_window=Toplevel(self.root)
      self.app=Details(self.new_window)  
   
    def bill(self):
      self.new_window=Toplevel(self.root)
      self.app=Bill(self.new_window) 

    def login(self):
      self.new_window=Toplevel(self.root)
      self.app=login_window(self.new_window)  

    def logout(self):
        self.root.destroy()   


if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()     