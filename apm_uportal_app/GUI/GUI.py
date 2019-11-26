from tkinter import *
from tkinter import filedialog
import smtplib
from email.message import EmailMessage


root = Tk()
root.geometry('1080x1000')
root.title('APM Sale Form')

title_label = Label(root, text="APM Portal",width=20,font=("bold", 30))
title_label.place(x=40,y=20)


######################################################################
######################################################################
#Vehicle Details

title_label = Label(root, text="::::::::: Part Details ::::::::",width=20,font=("bold", 15))
title_label.place(x=170,y=80)

#Year
year_label = Label(root, text="Year",width=20,font=("bold", 10))
year_label.place(x=68,y=130)

year_entry = Entry(root)
year_entry.place(x=240,y=130)
year = year_entry.get()
""""
#READ THIS
def get_year():
	year1 = year_entry.get()
	Label(root, text=year1 ,width=20,font=("bold", 10)).place(x=400,y=600)

Button(root,text='Get Entry',width=10,bg='red',fg='white', command=get_year).place(x=300,y=880)
"""

#Make
make_label = Label(root, text="Make",width=20,font=("bold", 10))
make_label.place(x=68,y=160)

make_entry = Entry(root)
make_entry.place(x=240,y=160)
make = make_entry.get()

#Model
model_label = Label(root, text="Model",width=20,font=("bold", 10))
model_label.place(x=68,y=190)

model_entry = Entry(root)
model_entry.place(x=240,y=190)
model = model_entry.get()

#Part
Part_label = Label(root, text="Part",width=20,font=("bold", 10))
Part_label.place(x=68,y=220)

Part_entry = Entry(root)
Part_entry.place(x=240,y=220)
part = Part_entry.get()

#Partdesc
Partdesc_label = Label(root, text="Part Description",width=20,font=("bold", 10))
Partdesc_label.place(x=68,y=250)

Partdesc_entry = Entry(root)
Partdesc_entry.place(x=240,y=250)
part_desc = Partdesc_entry.get()


#Part Notes
Part_notes_label = Label(root, text="Part Notes",width=20,font=("bold", 10))
Part_notes_label.place(x=68,y=280)

Part_Notes_entry = Entry(root)
Part_Notes_entry.place(x=240,y=280)
part_notes = Part_Notes_entry.get()

#Quoted Price
quoted_price_label = Label(root, text="Quoted Price in $",width=20,font=("bold", 10))
quoted_price_label.place(x=68,y=310)

quoted_price_entry = Entry(root)
quoted_price_entry.place(x=240,y=310)
quoted_price = quoted_price_entry.get()

#Purchase Price (Excluding Shipping) :
purchase_price_label = Label(root, text="Purchase Price",width=20,font=("bold", 10))
purchase_price_label.place(x=68,y=340)

purchase_price_entry = Entry(root)
purchase_price_entry.place(x=240,y=340)
purchase_price = purchase_price_entry.get()

#Salvage Yard 1,2,3:
sv1_label = Label(root, text="Yard 1",width=20,font=("bold", 10))
sv1_label.place(x=68,y=370)

sv1_entry = Entry(root)
sv1_entry.place(x=88,y=400)
sv1 = sv1_entry.get()

sv2_label = Label(root, text="Yard 2",width=20,font=("bold", 10))
sv2_label.place(x=198,y=370)

sv2_entry = Entry(root)
sv2_entry.place(x=220,y=400)
sv2 = sv2_entry.get()

sv3_label = Label(root, text="Yard 3",width=20,font=("bold", 10))
sv3_label.place(x=318,y=370)

sv3_entry = Entry(root)
sv3_entry.place(x=350,y=400)
sv3 = sv3_entry.get()

#Image Upload Button

def upload_image1(event=None):
	image1 = filedialog.askopenfilename()
	print('selected:', image1)

def upload_image2(event=None):
	image2 = filedialog.askopenfilename()
	print('selected:', image1)

def upload_image3(event=None):
	image2 = filedialog.askopenfilename()
	print('selected:', image1)	

image_button1 = Button(root,text='attach img 1',width=10,bg='red',fg='white', command=upload_image1).place(x=68,y=450)
image_button2 = Button(root,text='attach img 2',width=10,bg='red',fg='white', command=upload_image2).place(x=150,y=450)
image_button3 = Button(root,text='attach img 3',width=10,bg='red',fg='white', command=upload_image3).place(x=235,y=450)

##########################################################################################
##########################################################################################
#User Details

title2_label = Label(root, text=":::: User Details ::::",width=20,font=("bold", 15))
title2_label.place(x=650,y=80)

#First Name
fname_label = Label(root, text="First Name",width=20,font=("bold", 10))
fname_label.place(x=600,y=130)

fname_entry = Entry(root)
fname_entry.place(x=750,y=130)
fname = fname_entry.get()

#Second Name
sname_label = Label(root, text="Second Name",width=20,font=("bold", 10))
sname_label.place(x=600,y=160)

sname_entry = Entry(root)
sname_entry.place(x=750,y=160)
sname = sname_entry.get()

#Email
uemail_label = Label(root, text="Users Email",width=20,font=("bold", 10))
uemail_label.place(x=600,y=190)

uemail_entry = Entry(root)
uemail_entry.place(x=750,y=190)
uemail = uemail_entry.get()


#Users Phone
uphone_label = Label(root, text="Users Phone",width=20,font=("bold", 10))
uphone_label.place(x=600,y=220)

uphone_entry = Entry(root)
uphone_entry.place(x=750,y=220)
uphone = uphone_entry.get()
###############################################################################
#Billing Address

title2_label = Label(root, text="Billing Address",width=20,font=("bold", 15))
title2_label.place(x=600,y=250)

#Address Line 1
badd_label = Label(root, text="Address Line 1",width=20,font=("bold", 10))
badd_label.place(x=600,y=280)

badd_line1_entry = Entry(root)
badd_line1_entry.place(x=750,y=280)
badd_line1 = badd_line1_entry.get()


#Address Line 2
badd_label = Label(root, text="Address Line 2",width=20,font=("bold", 10))
badd_label.place(x=600,y=310)

badd_line2_entry = Entry(root)
badd_line2_entry.place(x=750,y=310)
badd_line2 = badd_line2_entry.get()

#City
badd_city_label = Label(root, text="City",width=20,font=("bold", 10))
badd_city_label.place(x=600,y=340)

badd_city_entry = Entry(root)
badd_city_entry.place(x=750,y=340)
badd_city = badd_city_entry.get()

#State/province
badd_state_label = Label(root, text="Province",width=20,font=("bold", 10))
badd_state_label.place(x=600,y=370)

badd_state_entry = Entry(root)
badd_state_entry.place(x=750,y=370)
badd_state = badd_state_entry.get()

#Zip Code
badd_zcode_label = Label(root, text="Zip Code",width=20,font=("bold", 10))
badd_zcode_label.place(x=600,y=400)

badd_zcode_entry = Entry(root)
badd_zcode_entry.place(x=750,y=400)
badd_zcode = badd_zcode_entry.get()

###############################################################################
#Shipping Address

title3_label = Label(root, text="Shipping Address",width=20,font=("bold", 15))
title3_label.place(x=600,y=430)

#Address Line 1
sadd_label = Label(root, text="Address Line 1",width=20,font=("bold", 10))
sadd_label.place(x=600,y=460)

sadd_line1_entry = Entry(root)
sadd_line1_entry.place(x=750,y=460)
sadd_line1 = sadd_line1_entry.get()


#Address Line 2
sadd_label = Label(root, text="Address Line 2",width=20,font=("bold", 10))
sadd_label.place(x=600,y=490)

sadd_line2_entry = Entry(root)
sadd_line2_entry.place(x=750,y=490)
sadd_line2 = sadd_line2_entry.get()


#City
sadd_city_label = Label(root, text="City",width=20,font=("bold", 10))
sadd_city_label.place(x=600,y=520)

sadd_city_entry = Entry(root)
sadd_city_entry.place(x=750,y=520)
sadd_city = sadd_city_entry.get()


#State/province
sadd_state_label = Label(root, text="Province",width=20,font=("bold", 10))
sadd_state_label.place(x=600,y=550)

sadd_state_entry = Entry(root)
sadd_state_entry.place(x=750,y=550)
sadd_state = sadd_state_entry.get()


#Zip Code
sadd_zcode_label = Label(root, text="Zip Code",width=20,font=("bold", 10))
sadd_zcode_label.place(x=600,y=580)

sadd_zcode_entry = Entry(root)
sadd_zcode_entry.place(x=750,y=580)
sadd_zcode = sadd_zcode_entry.get()

####Delivery Instructions
delins_label = Label(root, text="Del Instructions(If Any)",width=20,font=("bold", 10))
delins_label.place(x=600,y=610)

delins_entry = Entry(root)
delins_entry.place(x=750,y=610)
delins = delins_entry.get()



###############################################################################
#Payment Info
title4_label = Label(root, text="Payment Information",width=20,font=("bold", 15))
title4_label.place(x=600,y=650)

#Type Of Card
card_type_label = Label(root, text="Card Type",width=20,font=("bold", 10))
card_type_label.place(x=600,y=685)

variable = StringVar(root)
variable.set("Select")
card_type_dropdown = OptionMenu(root, variable, "VISA", "MASTER CARD", "AMEX", "DISCOVER", "PayPal")
card_type_dropdown.pack()
card_type_dropdown .place(x=750,y=680)
#card_type = card_type_dropdown.get()

#Card Number
card_num_label = Label(root, text="Card Number",width=20,font=("bold", 10))
card_num_label.place(x=600,y=720)

card_num_entry = Entry(root)
card_num_entry.place(x=750,y=720)
card_num = card_num_entry.get()


#Exp Month
card_type_label = Label(root, text="Exp. Month",width=20,font=("bold", 10))
card_type_label.place(x=600,y=755)

variable = StringVar(root)
variable.set("Select")
card_mon_dropdown = OptionMenu(root, variable, "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")
card_mon_dropdown.pack()
card_mon_dropdown.place(x=750,y=750)
#card_mon = card_mon_dropdown.get()


#Exp Year
card_type_label = Label(root, text="Exp. Year",width=20,font=("bold", 10))
card_type_label.place(x=600,y=785)

variable = StringVar(root)
variable.set("Select")
card_yr_dropdown = OptionMenu(root, variable, "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040")
card_yr_dropdown.pack()
card_yr_dropdown.place(x=750,y=780)
#card_yr = card_yr_dropdown.get()

#Card CVV
card_cvv_label = Label(root, text="CVV",width=20,font=("bold", 10))
card_cvv_label.place(x=600,y=820)

card_cvv_entry = Entry(root)
card_cvv_entry.place(x=750,y=820)
card_cvv = card_cvv_entry.get()

#Name On Card
card_name_label = Label(root, text="Name On Card",width=20,font=("bold", 10))
card_name_label.place(x=600,y=850)

card_name_entry = Entry(root)
card_name_entry.place(x=750,y=850)
card_name = card_name_entry.get()

#Submit Form Button


#Display the Send Confirmation button and send mail to customer with confirmation

close_sale = Button(root,text='Close Sale',width=10,bg='red',fg='white', command='NONE').place(x=700,y=880)
send_confirmation = Button(root,text='Send Confirmation',width=20,bg='black',fg='white', command='NONE').place(x=800,y=880)

#Send Confirmation To Customer
#send_confirm_button = Button(root,text='Send Confirmation',width=20,bg='black',fg='white', command='NONE').place(x=800,y=880)


###########################################################################################
###########################################################################################
###########################################################################################

#create a submit to manager function


#def send_to_manager(email, path):


###########################################################################################
###########################################################################################
###########################################################################################

#create a send confirmation to customer function (Only diplay while last clicked)


#run program
root.mainloop()
