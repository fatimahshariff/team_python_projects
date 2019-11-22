from tkinter import *
root = Tk()
root.geometry('1080x720')
root.title('reg form')

title_label = Label(root, text="APM Portal",width=20,font=("bold", 30))
title_label.place(x=40,y=20)

title_label = Label(root, text="Part Details::::",width=20,font=("bold", 15))
title_label.place(x=40,y=80)

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
model_label = Label(root, text="Model",width=20,font=("bold", 10))
model_label.place(x=68,y=220)

model_entry = Entry(root)
model_entry.place(x=240,y=220)


'''
label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
'''

label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

entry_3 = Entry(root)
entry_3.place(x=240,y=280)

def insert():
	ent1 = entry_1.get()
	ent2 = entry_2.get()
	ent3 = entry_3.get()
	ent4 = var.get()
	if ent4 == 1:
		ent4 = 'male'
	else:
		ent4 = 'female'	

	print(ent4)		
		
	f = open('details.txt', 'a+')
	f.write('Name :  {} \n  email :  {} \n age :   {}  \n gender : {} \n\n'.format(ent1,ent2,ent3,ent4))
	print('done')
	

Button(root, text='Submit',width=20,bg='brown',fg='white', command=insert).place(x=180,y=380)

root.mainloop()
#create pull request
