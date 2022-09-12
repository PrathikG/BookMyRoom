from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  #pip install pillow
from tkinter import messagebox
import random
from customer import Cust_window
from room import Roombooking
# from hotel import HotelManagementSystem
import mysql.connector


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()






class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("login")
        self.root.geometry("1550x800+0+0")
         
        
 
   
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\background.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        self.root2=Frame(self.root,bg="#0174AF")
        self.root2.place(x=610,y=170,width=340,height=450)

        
        img1=Image.open(r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\user1.png")
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimage1,bd=4,relief=RIDGE)
        lblimg1.place(x=730,y=175,width=120,height=100)


        get_str=Label(self.root2,text="Get started",font=("arial",20,"bold"),fg="white",bg="#0174AF")
        get_str.place(x=110,y=100)

        # label
        username=lbl=Label(self.root2,text="username",font=("times new roman",15,"bold"),fg="white",bg="#0174AF")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(self.root2,text="password",font=("times new roman",15,"bold"),fg="white",bg="#0174AF")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        # icon images
        img2=Image.open(r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(self.root,image=self.photoimage2,bd=4,relief=RIDGE)
        lblimg2.place(x=650,y=323,width=25,height=25)


        img3=Image.open(r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\pass.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(self.root,image=self.photoimage3,bd=4,relief=RIDGE)
        lblimg3.place(x=650,y=395,width=25,height=25)


        # login button
        loginbtn=Button(self.root2,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#FF851A",activeforeground='white',activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register button
        registerbtn=Button(self.root2,text="New user register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="#0174AF",activeforeground='white',activebackground="#0174AF")
        registerbtn.place(x=14,y=350,width=160)


        # forgot passwd
        forgotbtn=Button(self.root2,text="forgot Password",command=self.forgot_password_window, font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="#0174AF",activeforeground='white',activebackground="#0174AF")
        forgotbtn.place(x=9,y=370,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)   

    def login(self):
            if self.txtuser.get() == "" or self.txtpass.get() == "":
             messagebox.showerror("Error", "Enter valid username and password")
            elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
                messagebox.showinfo("success", "welcome")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                                        ))
#///////---------------------------------------  2 : 14 : 39
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid username and password")
                else:
                    open_main=messagebox.askyesno("yes No","Access only admin")
                    if open_main>0:
                        self.new_window=Toplevel(self.new_window)
                        self.app=Cust_window(self.new_window)
                    else:
                            if not open_main:
                                    return
                conn.commit()
                conn.close()  

#===============================================reset password=====================================================

    def reset_pass(self):
            if self.combo_security_Q.get()=="Select":
                    messagebox.showerror("Error","Select the Security question")

            elif self.txt_security.get()=="":
                    messagebox.showerror("Error","Please Enter the answer")

            elif self.txt_password.get()=="":
                    messagebox.showerror("Error","Please enter the new password")

            else:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                    my_cursor=conn.cursor() 
                    query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                    value=(self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
                    my_cursor.execute(query,  value)
                    row= my_cursor.fetchone()
                    
                    if row==None:
                            messagebox.showerror("Error","Please enter the correct answer", parent=self.root2)
                    else:
                            query=("update register set password=%s where email=%s")
                            value=(self.txt_password.get(), self.txtuser.get())
                            my_cursor.execute(query, value)

                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Info", "Your password has been reset, please login with new password")
                      


#=================================================forgot password==================================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
           messagebox.showerror("Error","Please enter the Email to reset password")
        else:
             conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
             my_cursor=conn.cursor() 

             query=("select * from register where email=%s")
             value=(self.txtuser.get(),)
             my_cursor.execute(query, value)

             row=my_cursor.fetchone()
             
             if row=="":
                messagebox.showerror("Error","Username doesn't exit")
             else:
                 conn.close()
                 self.root2=Toplevel()
                 self.root2.title("Forgot Password")
                 self.root2.geometry("340x450+610+170")

                 #background image
                 self.bg1="#0174AF"
                 bg_lbl1=Label(self.root2,bg=self.bg1)
                 bg_lbl1.place(x=0,y=0,relwidth=1,relheight=1)


                 l=Label(self.root2, text="Forgot Password", font= ("arial", 20, "bold"),bg="#0174AF",fg="white") 
                 l.place(x=0, y=10, relwidth=1)

                                                                       

                 security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
                 security_Q.place(x=50,y=80)

                 self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                 self.combo_security_Q["values"]=("select","Your birth place","your gf name","your pet name")
                 self.combo_security_Q.place(x=50,y=110,width=250)
                 self.combo_security_Q.current(0)

                 security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
                 security_A.place(x=50,y=150)

                 self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                 self.txt_security.place(x=50,y=180,width=250)

                 new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
                 new_password.place(x=50,y=220)

                 self.txt_password=ttk.Entry(self.root2,font=("times new roman",15))
                 self.txt_password.place(x=50,y=250,width=250)

                 btn=Button(self.root2,command= self.reset_pass, text="Reset", font=('times new roman', 15, 'bold'), fg= "white", bg="#FF851A")
                 btn.place(x=130, y=290, width=90)



       
       #-------------------------   REGISTER ----------------------------
       
class register:
    def __init__(self,root) :
        self.root=root
        self.root.title("register")
        self.root.geometry("1550x800+0+0")
#text variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()






#background image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\background.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

#left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\left.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=200,y=100,width=470,height=550)

#main self.root2
        self.root2 =Frame(self.root,bg="#0174AF")
        self.root2.place(x=670,y=100,width=700,height=550)

        register_lbl=Label(self.root2,text="REGISTER HERE",font=("arial",20,"bold"),fg="white",bg="#0174AF")
        register_lbl.place(x=20,y=20)        

#--------------label and entry
        #------row 1
        fname=Label(self.root2,text="First Name",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(self.root2,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(self.root2,text="Last Name",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(self.root2,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

       #-------------row 2 
        contact=Label(self.root2,text="Contact No",font=("times new roman",15,"bold"),bg="#0174AF", fg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(self.root2,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        #--email

        email=Label(self.root2,text="Email",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(self.root2,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #------------row 3
        security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(self.root2,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","Your birth place","your gf name","your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(self.root2,textvariable=self.var_securityA,text="security answer",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(self.root2,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #---------row 4
        pswd=Label(self.root2,text="Password",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(self.root2,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(self.root2,text="Confirm Password",font=("times new roman",15,"bold"),bg="#0174AF",fg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(self.root2,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #-------check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(self.root2,variable=self.var_check,text="I Agree to terms",font=("times new roman",11,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #----------buttons
        img=Image.open(r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\register.png")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)

        b1=Button(self.root2,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",11,"bold"), bg="#0174AF")
        b1.place(x=40,y=420,width=200)

        #
        img1=Image.open(r"C:\Users\asus\Desktop\HOTEL_MANAGEMENT_SYSTEM\HOTEL_MANAGEMENT_SYSTEM\images\login1.png")
        img1=img1.resize((200,75),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        b1=Button(self.root2,image=self.photoimage1, command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",11,"bold"), bg="#0174AF")
        b1.place(x=370,y=408,width=200)


   #---- function declaration
    
    
    def register_data(self):
                if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
                        messagebox.showerror("error","all fields are required", parent=self.root2)

                elif self.var_pass.get()!=self.var_confpass.get():
                        messagebox.showerror("error","passwords don't match", parent=self.root2)  
                elif self.var_check.get()==0:
                        messagebox.showerror("error","Agree to terms and condition", parent=self.root2)
                else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                        my_cursor=conn.cursor()
                        query=("select *from register where email=%s")
                        value=(self.var_email.get(),)
                        my_cursor.execute(query,value)   
                        row=my_cursor.fetchone()
                        if row!=None:
                                messagebox.showerror("Error","user already exists,please try another email", parent=self.root2)
                                return
                        else:
                                my_cursor.execute("insert into register value(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_fname.get(),
                                                                                                        self.var_lname.get(),
                                                                                                        self.var_contact.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_securityQ.get(),
                                                                                                        self.var_securityA.get(),
                                                                                                        self.var_pass.get()

                                                                                                                ))                         
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("SUCCESS","register successfull")  


    def return_login(self):
            self.root.destroy()                   
    
    def cust_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Cust_window(self.new_window) 

    def room_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Roombooking(self.new_window)   

         



if __name__=="__main__":
    main()
