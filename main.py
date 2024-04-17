from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk  #pip install pillow for import image
import random,os
from tkinter import messagebox
import tempfile
from time import strftime


class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Bill Generating System")


        #Variable Declaration
        self.C_name = StringVar()
        self.C_phone = StringVar()
        self.Bill_no = StringVar()
        z=random.randint(10000,99999)
        self.Bill_no.set(z)
        self.C_email = StringVar()
        self.Search_bill = StringVar()
        self.Product  = StringVar()
        self.Prices = IntVar()
        self.Qty = IntVar()
        self.Sub_total = StringVar()
        self.Tax_input = StringVar()
        self.Total = StringVar()



        #Product Categories List
        self.Category = ["Select Option","Clothing","LifeStyle","Mobiles"]
       #SubCatClothing
        self.SubCatClothing = ["Pant","T-Shirt","Shirt"]
        self.pant=["Levis", "Nike", "Adidas"] 
        self.price_Levis=899
        self.price_Nike=1399
        self.price_Adidas=1299

        self.T_Shirt=["Polo","Roadster","Jack&Jones"]
        self.price_polo=1500
        self.price_Roadster=1000
        self.price_JackJones=1399

        self.Shirt=["Peter England","Louis Phillipe","Park Avenue"]
        self.price_Peter=999
        self.price_Louis=1999
        self.price_Park=1299

        #SubCatLifStyle
        self.SubCatLifSytle=["Bath-Soap","Face Cream","Hair Oil"]
        self.Bath_soap=["LifeBouy","Lux","Santoor","Pearl"]
        self.price_life=float(20)
        self.price_lux=20
        self.price_santoor=20
        self.price_pearl=25

        self.Face_Cream=["Fair&Lovely","Ponds","Olay","Ganier"]
        self.price_fair=79
        self.price_ponds=49
        self.price_olay=89
        self.price_garnier=109

        self.Hair_oil=["Parachute","Jashmin","Bajaj"]
        self.price_para=129
        self.price_jashmin=299
        self.price_bajaj=230
        


       
        self.SubCatMobiles=["Iphone","Samsung","Vivo"]
        self.Iphone=["Iphone-13ProMax","Iphone-14ProMax","Iphone-15ProMax"]
        self.price_13pm=123000
        self.price_14pm=135000
        self.price_15pm=149000

        self.Samsung=["Samsung-Flip4","Samsung-Flip5","Samsung-S24"]
        self.price_f4=99000
        self.price_f5=119999
        self.price_s24=89000

        self.vivo=["Vivo-v26","Vivo-v28","Vivo-v30"]
        self.price_v26=45999
        self.price_v28=55999
        self.price_v30=79999





        


        #Image1
        img = Image.open("Image/mall.jpg")
        img = img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        #Image2
        img_1 = Image.open("Image/girls.jpg")
        img_1 = img_1.resize((500,130))
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)



        #Image3
        img_2 = Image.open("Image/apple.jpg")
        img_2 = img_2.resize((500,130))
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=520,height=130)

       



        #Label Title
        lbl_title = Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="White",fg="Red")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            String = strftime("%H:%M:%S %p")
            lbl.config(text = String)
            lbl.after(1000,time)

        lbl = Label(lbl_title,font=('times new roman',16,"bold"),background="WHITE",fg="BLUE")
        lbl.place(x=0,y=(-4),width=120,height=45)
        time()



        #Main Frame
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="WHITE")
        Main_Frame.place(x=0,y=175,width=1530,height=610)




        # Customer LabelFrame

        Cust_Frame = LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="White",fg="Red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob = Label(Cust_Frame,text="Mobile No. ",font=("times new roman",12,"bold"),bg="White",fg="Black")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob =ttk.Entry(Cust_Frame,textvariable=self.C_phone,font=("arial",11,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        
        self.lblCustName = Label(Cust_Frame,text="Customer Name  ",font=("times new roman",12,"bold"),bg="White",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName =ttk.Entry(Cust_Frame,textvariable=self.C_name,font=("arial",11,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)



        
        self.lblEmail = Label(Cust_Frame,text="Email ",font=("arial",12,"bold"),bg="White",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail =ttk.Entry(Cust_Frame,textvariable=self.C_email,font=("arial",11,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)





        
        # Product LabelFrame

        Product_Frame = LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="White",fg="Red")
        Product_Frame.place(x=370,y=5,width=650,height=140)


         #Category
        self.lblCategory= Label(Product_Frame,text="Select Categories",font=("arial",11,"bold"),bg="White",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)


        self.Combo_Category = ttk.Combobox(Product_Frame,values=self.Category,font=("arial",11,"bold"),width=24,state='readonly')
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #SubCategory
        self.lblSubCategory= Label(Product_Frame,text="Select SubCategory",font=("arial",11,"bold"),bg="White",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)


        self.ComboSubCategory = ttk.Combobox(Product_Frame,values=[""],font=("arial",11,"bold"),width=24,state='readonly')
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
 
        #Product Name
        self.lblproduct= Label(Product_Frame,text="Select Product Name",font=("arial",11,"bold"),bg="White",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)


        self.ComboProduct = ttk.Combobox(Product_Frame,textvariable=self.Product,font=("arial",11,"bold"),width=24,state='readonly')
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
       
        #Price
        self.lblPrice= Label(Product_Frame,text="Price",font=("arial",10,"bold"),bg="White",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)


        self.ComboPrice = ttk.Combobox(Product_Frame,textvariable=self.Prices,font=("arial",11,"bold"),width=18,state='readonly')
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty= Label(Product_Frame,text="Qty",font=("arial",11,"bold"),bg="White",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)


        self.ComboQty = ttk.Entry(Product_Frame,textvariable=self.Qty,font=("arial",11,"bold"),width=20)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)





        #Image Frame

        MiddleFrame = Frame(Main_Frame,bd=2,bg="White")
        MiddleFrame.place(x=10,y=150,width=980,height=340)


        #Image1
        img_12 = Image.open("Image/good.jpg")
        img_12 = img_12.resize((490,340))
        self.photoimg_12=ImageTk.PhotoImage(img_12)

        lbl_img_12=Label(MiddleFrame,image=self.photoimg_12)
        lbl_img_12.place(x=0,y=0,width=490,height=340)


        img_22 = Image.open("Image/mall.jpg")
        img_22 = img_22.resize((490,340))
        self.photoimg_22=ImageTk.PhotoImage(img_22)

        lbl_img_22=Label(MiddleFrame,image=self.photoimg_22)
        lbl_img_22.place(x=490,y=0,width=490,height=340)








        #Search
        Search_Frame = Frame(Main_Frame,bd=2,bg="White")
        Search_Frame.place(x=1030,y=15,width=500,height=40)


        self.lblBill= Label(Search_Frame,text="Bill Number ",font=("arial",10,"bold"),bg="RED",fg="WHITE")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame,textvariable=self.Search_bill,font=("arial",11,"bold"),width=18)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=1)

        self.BtnSearch = Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2,sticky=W,padx=2)






        









        #Right Frame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="White",fg="Red")
        RightLabelFrame.place(x=1030,y=45,width=480,height=440)


        #text Field
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea = Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="WHITE",fg="BLUE",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)




         # BillCounter LabelFrame

        Bottom_Frame = LabelFrame(Main_Frame,text="Bill Counter ",font=("times new roman",12,"bold"),bg="White",fg="Red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=119)

        #SubTotal
        self.lblSubTotal= Label(Bottom_Frame,text="Sub Total",font=("arial",10,"bold"),bg="White",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)


        self.EntrySubTotal = ttk.Entry(Bottom_Frame,textvariable=self.Sub_total,font=("arial",11,"bold"),width=18,state='readonly')
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
    

         #Tax
        self.lbl_tax= Label(Bottom_Frame,text=" Gov Tax ",font=("arial",10,"bold"),bg="White",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)


        self.txt_tax = ttk.Entry(Bottom_Frame,textvariable=self.Tax_input,font=("arial",11,"bold"),width=18,state='readonly')
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
         #Amount
        self.lblAmountTotal= Label(Bottom_Frame,text=" Total",font=("arial",10,"bold"),bg="White",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)


        self.txtAmountTotal = ttk.Entry(Bottom_Frame,textvariable=self.Total,font=("arial",11,"bold"),width=18,state='readonly')
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)



        # Button Frame

        Btn_Frame = Frame(Bottom_Frame,bd=2,bg="White")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart = Button(Btn_Frame,command=self.AddToCart,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill = Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)


        self.BtnSave = Button(Btn_Frame,command=self.save_bill,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint = Button(Btn_Frame,command=self.Bprint,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear = Button(Btn_Frame,command=self.clear,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit = Button(Btn_Frame,command=self.root.destroy,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)

        self.welcome()

        self.l=[]

    def AddToCart(self):
        Tax=1
        self.nP = self.Prices.get()
        self.PQ = self.Qty.get() * self.nP
        self.l.append(self.PQ)
        if self.Product.get == "":
            messagebox.showerror("Error","PLEASE SELECT PRODUCT NAME")

        else:
            self.textarea.insert(END,f"\n {self.Product.get()}\t\t{self.Qty.get()}\t\t{self.PQ}")
            self.Sub_total.set(str("Rs.%.2f"%(sum(self.l))))
            self.Tax_input.set(str('Rs.%.2f'%((((sum(self.l))- (self.Prices.get()))*Tax)/100)))
            self.Total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.Prices.get()))*Tax)/100)))))



    def gen_bill(self):
        if self.Product.get()=="":
              messagebox.showerror("Error","PLEASE ADD TO CART PRODUCT")
        
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,"\n")
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n***************************************************")
            self.textarea.insert(END,f"\n SUB AMOUNT : \t\t\t{self.Sub_total.get()}")
            self.textarea.insert(END,f"\n TAX AMOUNT : \t\t\t{self.Tax_input.get()}")
            self.textarea.insert(END,f"\n TOTAL AMOUNT : \t\t\t{self.Total.get()}")
            self.textarea.insert(END,"\n***************************************************")


    def save_bill(self):
        op= messagebox.askyesno("Save Bill","Do you want to Save the Bill")
        if op>0:
            self.Bill_data = self.textarea.get(1.0,END)
            f1 = open('Bills/'+str(self.Bill_no.get())+".text",'w')
            f1.write(self.Bill_data)
            op = messagebox.showinfo("Saved Bill",f"Bill No : {self.Bill_no.get()} Saved Successfully!!!")
            f1.close()


    def Bprint(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mkdtemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.Search_bill.get():
                f1=open(f"Bills/{i}",'r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found = "yes"

        if found == "no":
             messagebox.showerror("Error","Invalid Bill No. ")



    def clear(self):
        self.textarea.delete(1.0,END)
        self.C_name.set("")
        self.C_email.set("")
        self.C_phone.set("")
        x=random.randint(10000,99999)
        self.Bill_no.set(str(x))
        self.Search_bill.set("")
        self.Product.set("")
        self.Prices.set(0)
        self.Qty.set(0)
        self.l=[0]
        self.Total.set("")
        self.Sub_total.set("")
        self.Tax_input.set("")
        self.Combo_Category.current(0)
        self.ComboSubCategory.set("")
        self.welcome()



    















    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\tWELCOME TO  BVR  MALL")
        self.textarea.insert(END,f"\n BILL NUMBER : {self.Bill_no.get()}")
        self.textarea.insert(END,f"\n CUSTOMER NAME : {self.C_name.get()}")
        self.textarea.insert(END,f"\n PHONE NUMBER : {self.C_phone.get()}")
        self.textarea.insert(END,f"\n CUSTOMER EMAIL : {self.C_email.get()}")


        self.textarea.insert(END,"\n***************************************************")
        self.textarea.insert(END,f"\n PRODUCTS\t\tQTY\t\tPRICE")
        self.textarea.insert(END,"\n***************************************************")














        #Functions for Selecting Category and SubCatrgories

    def Categories(self,event=""):
        if self.Combo_Category.get() == "Clothing":
            self.ComboSubCategory.config(values=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get() == "LifeStyle":
            self.ComboSubCategory.config(values=self.SubCatLifSytle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get() == "Mobiles":
            self.ComboSubCategory.config(values=self.SubCatMobiles)
            self.ComboSubCategory.current(0)



    def Product_add(self,event=""):
        if self.ComboSubCategory.get() == "Pant":
            self.ComboProduct.config(values=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "T-Shirt":
            self.ComboProduct.config(values=self.T_Shirt)
            self.ComboProduct.current(0)


        if self.ComboSubCategory.get() == "Shirt":
            self.ComboProduct.config(values=self.Shirt)
            self.ComboProduct.current(0)

        #LifStyle
        if self.ComboSubCategory.get() == "Bath-Soap":
            self.ComboProduct.config(values=self.Bath_soap)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get() == "Face Cream":
            self.ComboProduct.config(values=self.Face_Cream)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Hair Oil":
            self.ComboProduct.config(values=self.Hair_oil)
            self.ComboProduct.current(0)

      #Mobiles
        if self.ComboSubCategory.get() == "Iphone":
            self.ComboProduct.config(values=self.Iphone)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get() == "Samsung":
            self.ComboProduct.config(values=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Vivo":
            self.ComboProduct.config(values=self.vivo)
            self.ComboProduct.current(0)




    def price(self,event=""):
        #Pant
        if self.ComboProduct.get() == "Levis":
            self.ComboPrice.config(values=self.price_Levis)
            self.ComboPrice.current(0)
            self.Qty.set(1) 


        if self.ComboProduct.get() == "Nike":
            self.ComboPrice.config(values=self.price_Nike)
            self.ComboPrice.current(0)
            self.Qty.set(1) 


        if self.ComboProduct.get() == "Adidas":
            self.ComboPrice.config(values=self.price_Adidas)
            self.ComboPrice.current(0)
            self.Qty.set(1) 



          

        if self.ComboProduct.get() == "Polo":
            self.ComboPrice.config(values=self.price_polo)
            self.ComboPrice.current(0)
            self.Qty.set(1) 

        if self.ComboProduct.get() == "Roadster":
            self.ComboPrice.config(values=self.price_Roadster)
            self.ComboPrice.current(0)
            self.Qty.set(1) 

        if self.ComboProduct.get() == "Jack&Jones":
            self.ComboPrice.config(values=self.price_JackJones)
            self.ComboPrice.current(0)
            self.Qty.set(1) 

       
        if self.ComboProduct.get() == "Peter England":
            self.ComboPrice.config(values=self.price_Peter)
            self.ComboPrice.current(0)
            self.Qty.set(1)

        if self.ComboProduct.get() == "Louis Phillipe":
            self.ComboPrice.config(values=self.price_Louis)
            self.ComboPrice.current(0)
            self.Qty.set(1) 

        if self.ComboProduct.get() == "Park Avenue":
            self.ComboPrice.config(values=self.price_Park)
            self.ComboPrice.current(0)
            self.Qty.set(1)  



            #"LifeBouy","Lux","Santoor","Pearl"
        
        if self.ComboProduct.get() == "LifeBouy":
            self.ComboPrice.config(values=self.price_life)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Lux":
            self.ComboPrice.config(values=self.price_lux)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Santoor":
            self.ComboPrice.config(values=self.price_santoor)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Pearl":
            self.ComboPrice.config(values=self.price_pearl)
            self.ComboPrice.current(0)
            self.Qty.set(1)  


        #"Fair&Lovely","Ponds","Olay","Ganier"
        if self.ComboProduct.get() == "Fair&Lovely":
            self.ComboPrice.config(values=self.price_fair)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Ponds":
            self.ComboPrice.config(values=self.price_ponds)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Olay":
            self.ComboPrice.config(values=self.price_olay)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Ganier":
            self.ComboPrice.config(values=self.price_garnier)
            self.ComboPrice.current(0)
            self.Qty.set(1)



        #"Parachute","Jashmin","Bajaj"

        if self.ComboProduct.get() == "Parachute":
            self.ComboPrice.config(values=self.price_para)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Jashmin":
            self.ComboPrice.config(values=self.price_jashmin)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Bajaj":
            self.ComboPrice.config(values=self.price_bajaj)
            self.ComboPrice.current(0)
            self.Qty.set(1)  


        #"Iphone-13ProMax","Iphone-14ProMax","Iphone-15ProMax"  

        if self.ComboProduct.get() == "Iphone-13ProMax":
            self.ComboPrice.config(values=self.price_13pm)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Iphone-14ProMax":
            self.ComboPrice.config(values=self.price_14pm)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Iphone-15ProMax":
            self.ComboPrice.config(values=self.price_15pm)
            self.ComboPrice.current(0)
            self.Qty.set(1) 

    #"Samsung-Flip4","Samsung-Flip5","Samsung-S24"

        if self.ComboProduct.get() == "Samsung-Flip4":
            self.ComboPrice.config(values=self.price_f4)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Samsung-Flip5":
            self.ComboPrice.config(values=self.price_f5)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Samsung-S24":
            self.ComboPrice.config(values=self.price_s24)
            self.ComboPrice.current(0)
            self.Qty.set(1) 

        #"Vivo-v26","Vivo-v28","Vivo-v30"

        if self.ComboProduct.get() == "Vivo-v26":
            self.ComboPrice.config(values=self.price_v26)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Vivo-v28":
            self.ComboPrice.config(values=self.price_v28)
            self.ComboPrice.current(0)
            self.Qty.set(1)  

        if self.ComboProduct.get() == "Vivo-v30":
            self.ComboPrice.config(values=self.price_v30)
            self.ComboPrice.current(0)
            self.Qty.set(1)  









if __name__ == '__main__':
    root=Tk()
    obj = Bill_App(root)
    root.mainloop()
