from tkinter import *
from tkinter import filedialog

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

#Make
make_label = Label(root, text="Make",width=20,font=("bold", 10))
make_label.place(x=68,y=160)

make_entry = Entry(root)
make_entry.place(x=240,y=160)

#Model
model_label = Label(root, text="Model",width=20,font=("bold", 10))
model_label.place(x=68,y=190)

model_entry = Entry(root)
model_entry.place(x=240,y=190)

#Part
Part_label = Label(root, text="Part",width=20,font=("bold", 10))
Part_label.place(x=68,y=220)

Part_entry = Entry(root)
Part_entry.place(x=240,y=220)

#Partdesc
Partdesc_label = Label(root, text="Part Description",width=20,font=("bold", 10))
Partdesc_label.place(x=68,y=250)

Partdesc_entry = Entry(root)
Partdesc_entry.place(x=240,y=250)


#Part Notes
Part_notes_label = Label(root, text="Part Notes",width=20,font=("bold", 10))
Part_notes_label.place(x=68,y=280)

Part_Notes_entry = Entry(root)
Part_Notes_entry.place(x=240,y=280)

#Quoted Price
quoted_price_label = Label(root, text="Quoted Price in $",width=20,font=("bold", 10))
quoted_price_label.place(x=68,y=310)

quoted_price_entry = Entry(root)
quoted_price_entry.place(x=240,y=310)

#Purchase Price (Excluding Shipping) :
purchase_price_label = Label(root, text="Purchase Price",width=20,font=("bold", 10))
purchase_price_label.place(x=68,y=340)

purchase_price_entry = Entry(root)
purchase_price_entry.place(x=240,y=340)

#Salvage Yard 1,2,3:
sv1_label = Label(root, text="Yard 1",width=20,font=("bold", 10))
sv1_label.place(x=68,y=370)

sv1_entry = Entry(root)
sv1_entry.place(x=88,y=400)

sv2_label = Label(root, text="Yard 2",width=20,font=("bold", 10))
sv2_label.place(x=198,y=370)

sv2_entry = Entry(root)
sv2_entry.place(x=220,y=400)

sv3_label = Label(root, text="Yard 3",width=20,font=("bold", 10))
sv3_label.place(x=318,y=370)

sv3_entry = Entry(root)
sv3_entry.place(x=350,y=400)

#Image Upload Button

def upload_image1(event=None):
	image1 = filedialog.askopenfilename()
	print('selected:', image1)

def upload_image2(event=None):
	image1 = filedialog.askopenfilename()
	print('selected:', image1)

def upload_image3(event=None):
	image1 = filedialog.askopenfilename()
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

#Second Name
sname_label = Label(root, text="Second Name",width=20,font=("bold", 10))
sname_label.place(x=600,y=160)

sname_entry = Entry(root)
sname_entry.place(x=750,y=160)

#Email
uemail_label = Label(root, text="Users Email",width=20,font=("bold", 10))
uemail_label.place(x=600,y=190)

uemail_entry = Entry(root)
uemail_entry.place(x=750,y=190)


#Users Phone
uphone_label = Label(root, text="Users Phone",width=20,font=("bold", 10))
uphone_label.place(x=600,y=220)

uphone_entry = Entry(root)
uphone_entry.place(x=750,y=220)

###############################################################################
#Billing Address

title2_label = Label(root, text="Billing Address",width=20,font=("bold", 15))
title2_label.place(x=600,y=250)

#Address Line 1
badd_label = Label(root, text="Address Line 1",width=20,font=("bold", 10))
badd_label.place(x=600,y=280)

badd_line1_entry = Entry(root)
badd_line1_entry.place(x=750,y=280)


#Address Line 2
badd_label = Label(root, text="Address Line 2",width=20,font=("bold", 10))
badd_label.place(x=600,y=310)

badd_line2_entry = Entry(root)
badd_line2_entry.place(x=750,y=310)

#City
badd_city_label = Label(root, text="City",width=20,font=("bold", 10))
badd_city_label.place(x=600,y=340)

badd_city_entry = Entry(root)
badd_city_entry.place(x=750,y=340)

#State/province
badd_state_label = Label(root, text="Province",width=20,font=("bold", 10))
badd_state_label.place(x=600,y=370)

badd_state_entry = Entry(root)
badd_state_entry.place(x=750,y=370)

#Zip Code
badd_zcode_label = Label(root, text="Zip Code",width=20,font=("bold", 10))
badd_zcode_label.place(x=600,y=400)

badd_zcode_entry = Entry(root)
badd_zcode_entry.place(x=750,y=400)


###############################################################################
#Shipping Address

title3_label = Label(root, text="Shipping Address",width=20,font=("bold", 15))
title3_label.place(x=600,y=430)

#Address Line 1
sadd_label = Label(root, text="Address Line 1",width=20,font=("bold", 10))
sadd_label.place(x=600,y=460)

sadd_line1_entry = Entry(root)
sadd_line1_entry.place(x=750,y=460)


#Address Line 2
sadd_label = Label(root, text="Address Line 2",width=20,font=("bold", 10))
sadd_label.place(x=600,y=490)

sadd_line2_entry = Entry(root)
sadd_line2_entry.place(x=750,y=490)

#City
sadd_city_label = Label(root, text="City",width=20,font=("bold", 10))
sadd_city_label.place(x=600,y=520)

sadd_city_entry = Entry(root)
sadd_city_entry.place(x=750,y=520)

#State/province
sadd_state_label = Label(root, text="Province",width=20,font=("bold", 10))
sadd_state_label.place(x=600,y=550)

sadd_state_entry = Entry(root)
sadd_state_entry.place(x=750,y=550)

#Zip Code
sadd_zcode_label = Label(root, text="Zip Code",width=20,font=("bold", 10))
sadd_zcode_label.place(x=600,y=580)

sadd_zcode_entry = Entry(root)
sadd_zcode_entry.place(x=750,y=580)

####Delivery Instructions
delins_label = Label(root, text="Del Instructions(If Any)",width=20,font=("bold", 10))
delins_label.place(x=600,y=610)

delins_entry = Entry(root)
delins_entry.place(x=750,y=610)


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

#Card Number
card_num_label = Label(root, text="Card Number",width=20,font=("bold", 10))
card_num_label.place(x=600,y=720)

card_num_entry = Entry(root)
card_num_entry.place(x=750,y=720)

#Exp Month
card_type_label = Label(root, text="Exp. Month",width=20,font=("bold", 10))
card_type_label.place(x=600,y=755)

variable = StringVar(root)
variable.set("Select")
card_mon_dropdown = OptionMenu(root, variable, "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")
card_mon_dropdown.pack()
card_mon_dropdown.place(x=750,y=750)

#Exp Year
card_type_label = Label(root, text="Exp. Year",width=20,font=("bold", 10))
card_type_label.place(x=600,y=785)

variable = StringVar(root)
variable.set("Select")
card_yr_dropdown = OptionMenu(root, variable, "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034", "2035", "2036", "2037", "2038", "2039", "2040")
card_yr_dropdown.pack()
card_yr_dropdown.place(x=750,y=780)

#Card CVV
card_cvv_label = Label(root, text="CVV",width=20,font=("bold", 10))
card_cvv_label.place(x=600,y=820)

card_cvv_entry = Entry(root)
card_cvv_entry.place(x=750,y=820)

#Name On Card
card_name_label = Label(root, text="Name On Card",width=20,font=("bold", 10))
card_name_label.place(x=600,y=850)

card_name_entry = Entry(root)
card_name_entry.place(x=750,y=850)

#Submit Form Button
submit_button = Button(root,text='Close Sale',width=10,bg='red',fg='white', command='NONE').place(x=700,y=880)

#Send Confirmation To Customer
send_confirm_button = Button(root,text='Send Confirmation',width=20,bg='black',fg='white', command='NONE').place(x=800,y=880)


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
