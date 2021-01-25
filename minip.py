from tkinter import *
scr=Tk()
l=Label(scr,text='Username',font=('times',15,'bold'))
l.grid(row=0,column=0)
l1=Label(scr,text='Password',font=('times',15,'bold'))
l1.grid(row=1,column=0)
u=Entry(scr,font=('times',15,'bold'))
u.grid(row=0,column=1)
p=Entry(scr,font=('times',15,'bold'),show='*')
p.grid(row=1,column=1)
q=Label(scr,font=('times',15,'bold'))
q.grid(row=2,column=0)
def fun():
    if re.search(r'^\S+$',u.get()) and re.search(r'^\S+$',p.get()):
        dt=open('user.txt').readlines()
        for i in dt:
            if u.get()==i.split()[0] and p.get()==i.split()[1]:
                q.config(text="logged in")
                break
        else:
            q.config(text="invalid password or user")
                
    else:
        q.config(text="space not allowed")
b=Button(scr,text='submit',font=('times',15,'bold'),command=fun)
b.grid(row=2,column=1)
