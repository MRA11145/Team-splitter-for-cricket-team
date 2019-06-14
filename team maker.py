import sqlite3
from tkinter import *
from tkinter import messagebox


class team:
 def __init__(self):
     self.MENU()
 def MENU(self):
  self.mwin = Tk()
  self.mwin.geometry('1000x600')
  menu = Menu(self.mwin)
  self.mwin.config(menu=menu)
  file = Menu(menu)
  file.add_command(label='Exit', command=self.mwin.destroy)
  menu.add_cascade(label='File', menu=file)
  help = Menu(menu)
  help.add_command(label='About', command=self.about)
  help.add_command(label='Support', command=self.support)
  menu.add_cascade(label='Help', menu=help)
  self.mid = Frame(self.mwin, bg='white', width=False, height=False)
  self.l = Label(self.mwin,text='TEAM MAKER', bg='black', fg='white',font=('algerian',80,'bold'),justify = CENTER).pack(fill=X); 
  self.Admin  = Button(self.mid, bg='gray80', text='ADMIN'     , fg='black', bd=7, height=2, width=20, cursor='hand1', activebackground='white',command=self.admin).pack(fill=X, padx=150, pady=25);
  self.Best   = Button(self.mid, bg='gray80', text='BEST TEAM ', fg='black', bd=7, height=2, width=20, cursor='hand1', activebackground='white',command=self.best).pack(fill=X, padx=150, pady=25);
  self.Team   = Button(self.mid, bg='gray80', text='TEAM MAKER', fg='black', bd=7, height=2, width=20, cursor='hand1', activebackground='white',command=self.team_maker).pack(fill=X, padx=150, pady=25);
  self.mid.pack(pady=80,ipady=100)
  self.mwin.configure(bg = "gray")
  self.mwin.title('TEAM MAKER')
  self.mwin.mainloop()
 def about(self):
  self.mwin.destroy()
  self.awin = Tk()
  self.awin.geometry('1000x600')
  self.mid = Frame(self.awin, width=False, height=False)
  self.l = Label(self.awin,text='ABOUT', bg='black', fg='white',font=('algerian',80,'bold'),justify = CENTER).pack(fill=X);
  self.Msg=' Team Maker\n Version 1805\n @ 2018 Microsoft Corporation. All Rights Are Reserved\n The Team Maker Application and its user interface is protected\n by trademark \n\n\n\n\n\n This product is licensed under MICROSOFT CORPORATION terms to\n Hp'
  self.msg = Label(self.mid, text= self.Msg, font=('times',14), justify=LEFT)
  self.msg.pack(pady=30)
  self.back   = Button(self.awin, bg='gray80', text='<- BACK',       fg='black', bd=6, cursor='hand1', activebackground='white',command= lambda: self.awin.destroy() or self.MENU()).place(x=10,y=133)
  self.mid.pack(pady=80,ipadx=100,ipady=100)
  self.awin.configure(bg = "gray")
  self.awin.title('ADMIN')
  self.awin.mainloop()
 def support(self):
  self.mwin.destroy()
  self.swin = Tk()
  self.swin.geometry('1000x600')
  self.mid = Frame(self.swin, width=False, height=False)
  self.l = Label(self.swin,text='CONTACT US', bg='black', fg='white',font=('algerian',80,'bold'),justify = CENTER).pack(fill=X);
  self.Msg='\n\n\n\n Customer Care : 1800-2222-2222\n\n\n Email : Team_Makersupport@gmail.com\n\n\n Address : opp to Amrishpuri, kanchenbagh, New Delhi, 500149. '
  self.MSG=' CONTACT US AT'
  self.mSG = Label(self.mid, text=self.MSG, font=('times',22,'bold'), justify=LEFT)
  self.mSG.pack(side='left')
  self.msg = Label(self.mid, text= self.Msg, font=('times',14), justify=LEFT)
  self.msg.pack()
  self.back   = Button(self.swin, bg='gray80', text='<- BACK',       fg='black', bd=6, cursor='hand1', activebackground='white',command= lambda: self.swin.destroy() or self.MENU()).place(x=10,y=133)
  self.mid.pack(pady=80,ipadx=100,ipady=100)
  self.swin.configure(bg = "gray")
  self.swin.title('ADMIN')
  self.swin.mainloop()
 def best(self):
    self.bat=[]
    self.ball=[]
    self.all=[]
    self.wic=[]
    self.conn = sqlite3.connect('player.db')
    self.c    = self.conn.cursor();
    
    for row in self.conn.execute('SELECT * FROM player'):
        if row[2]=='Batsman':
            self.bat.append(row[5])
        elif row[2]=='Bowler':
            self.ball.append(row[7])
        elif row[2]=='All Rounder':
            self.all.append(row[5])
        elif row[2]=='Wicket-Keeper':
            self.wic.append(row[5])
    self.bat.sort(reverse=True)
    self.ball.sort(reverse=True)
    self.all.sort(reverse=True)
    self.wic.sort(reverse=True)
    c=0
    c1=0
    c2=0
    c3=0
    for i in range(0,11):
        for row in self.conn.execute('SELECT * FROM player'):
            if row[2]=='Batsman':
                if c!=4:
                    if row[5]==self.bat[c]:
                        print(row[0],'(Batsman)')
                        c=c+1
    for i in range(0,11):
        for row in self.conn.execute('SELECT * FROM player'):
            if row[2]=='Wicket-Keeper':
                if c3!=1:
                    if row[5]==self.wic[c3]:
                        print(row[0],'(WC)')
                        c3=c3+1
    for i in range(0,11):
        for row in self.conn.execute('SELECT * FROM player'):
            if row[2]=='All Rounder':
                if c2!=2:
                    if row[5]==self.all[c2]:
                        print(row[0],'(All-Rounder)')
                        c2=c2+1
    for i in range(0,11):
        for row in self.conn.execute('SELECT * FROM player'):
            if row[2]=='Bowler':
                if c1!=4:
                    if row[7]==self.ball[c1]:
                        print(row[0],'(Bowler)')
                        c1=c1+1
    messagebox.showinfo('INFORMATION','RESULTS ARE DISPLAYED IN SHELL')
    self.conn.close();
 def team_maker(self):
    self.bat=[]
    self.ball=[]
    self.all=[]
    self.wic=[]
    self.teamA=[]
    self.teamB=[]
    self.conn = sqlite3.connect('player.db')
    self.c    = self.conn.cursor();
    for row in self.conn.execute('SELECT * FROM player'):
        if row[2]=='Batsman':
            self.bat.append(row[5])
        elif row[2]=='Bowler':
            self.ball.append(row[7])
        elif row[2]=='All Rounder':
            self.all.append(row[5])
        elif row[2]=='Wicket-Keeper':
            self.wic.append(row[5])
    self.bat.sort(reverse=True)
    self.ball.sort(reverse=True)
    self.all.sort(reverse=True)
    self.wic.sort(reverse=True)
    self.sumB=self.sumA=0
    self.teamA.append(self.bat[0])
    self.sumA=self.sumA+self.bat[0]
    c=0
    c1=1
    for i in range(1,9):
        if self.sumA>self.sumB:
            if c<4:
                self.teamB.append(self.bat[i])
                self.sumB=self.sumB+self.bat[i]
                c=c+1
        else:
            if c1<4:
                self.teamA.append(self.bat[i])
                self.sumA=self.sumA+self.bat[i]
                c1=c1+1
    
    c=0
    c1=0
    for i in range(0,2):
        if self.sumA>self.sumB:
            if c<1:
                self.teamB.append(self.wic[i])
                self.sumB=self.sumB+self.wic[i]
                c=c+1
        else:
            if c1<1:
                self.teamA.append(self.wic[i])
                self.sumA=self.sumA+self.wic[i]
                c1=c1+1

    c=0
    c1=0
    for i in range(0,4):
        if self.sumA>self.sumB:
            if c<2:
                self.teamB.append(self.all[i])
                self.sumB=self.sumB+self.all[i]
                c=c+1
        else:
            if c1<2:
                self.teamA.append(self.all[i])
                self.sumA=self.sumA+self.all[i]
                c1=c1+1 
        
    c=0
    c1=0
    for i in range(0,9):
        if self.sumA>self.sumB:
            if c<4:
                self.teamB.append(self.ball[i])
                self.sumB=self.sumB+self.ball[i]
                c=c+1
        else:
            if c1<4:
                self.teamA.append(self.ball[i])
                self.sumA=self.sumA+self.ball[i]
                c1=c1+1
    print('\t\t\t\tTEAM A\n\n')
    self.p=[]
    for i in range(0,11):
        c=0
        p1=0
        self.p.append('0')
        for row in self.conn.execute('SELECT * FROM player'):
            if i<4:
                if self.teamA[i]==row[5]:
                    p1=p1+1
                    if c==0:
                        c=1
                        print(row[0],'(Batsmen)')
                    if p1>1:
                     self.p[i]=self.teamA[i]
            elif i==4:
                if self.teamA[i]==row[5]:
                    p1=p1+1
                    if c==0:
                        c=1
                        print(row[0],'(WC)')
                    if p1>1:
                     self.p[i]=self.teamA[i]
            elif i>4 and i<7:
                if self.teamA[i]==row[5]:
                    p1=p1+1
                    if c==0:
                        c=1
                        print(row[0],'(All-Rounder)')
                    if p1>1:
                     self.p[i]=self.teamA[i]
            elif i>6:
                if self.teamA[i]==row[7]:
                    p1=p1+1
                    if c==0:
                        c=1
                        print(row[0],'(Bowler)')
                    if p1>1:
                     self.p[i]=self.teamA[i]
                     
    print('\n\n\t\t\t\tTEAM B\n\n')
    
    for i in range(0,11):
        c=0
        for row in self.conn.execute('SELECT * FROM player'):
            if i<4:
                if self.teamB[i]==row[5]:
                    if self.p[i]==self.teamB[i]:
                        if c==0:
                            c=c+1
                        else:
                            print(row[0],'(Batsmen)')
                    else:
                        print(row[0],'(Batsmen)')
            elif i==4:
                if self.teamB[i]==row[5]:
                    if self.p[i]==self.teamB[i]:
                        if c==0:
                            c=c+1
                        else:
                            print(row[0],'(WC)')
                    else:
                        print(row[0],'(WC)')
            elif i>4 and i<7:
                if self.teamB[i]==row[5]:
                    if self.p[i]==self.teamB[i]:
                        if c==0:
                            c=c+1
                        else:
                            print(row[0],'(All-Rounder)')
                    else:
                        print(row[0],'(All-Rounder)')
            elif i>6:
                if self.teamB[i]==row[7]:
                    if self.p[i]==self.teamB[i]:
                        if c==0:
                            c=c+1
                        else:
                            print(row[0],'(Bowler)')
                    else:
                        print(row[0],'(Bowler)')
                    
    messagebox.showinfo('INFORMATION','RESULTS ARE DISPLAYED IN SHELL')
    self.conn.close();
 def admin(self):
  self.mwin.destroy()
  self.win = Tk()
  self.win.geometry('1000x600')
  self.mid = Frame(self.win, bg='white', width=False, height=False)
  self.l = Label(self.win,text='ADMIN', bg='black', fg='white',font=('algerian',80,'bold'),justify = CENTER).pack(fill=X); 
  self.add    = Button(self.mid, bg='gray80', text='Add Member',    fg='black', bd=6, cursor='hand1', activebackground='white',command=self.add_member).pack(fill=X, padx=150, pady=20);
  self.view   = Button(self.mid, bg='gray80', text='View Member',   fg='black', bd=6, cursor='hand1', activebackground='white',command=self.view_member).pack(fill=X, padx=150, pady=20);
  self.search = Button(self.mid, bg='gray80', text='Search Member', fg='black', bd=6, cursor='hand1', activebackground='white',command=self.search_member).pack(fill=X, padx=150, pady=20);
  self.delete = Button(self.mid, bg='gray80', text='Delete Member', fg='black', bd=6, cursor='hand1', activebackground='white',command=self.delete_member).pack(fill=X, padx=150, pady=20);
  self.back   = Button(self.win, bg='gray80', text='<- BACK',       fg='black', bd=6, cursor='hand1', activebackground='white',command= lambda: self.win.destroy() or self.MENU()).place(x=10,y=133)
  self.mid.pack(pady=80)
  self.win.configure(bg = "gray")
  self.win.title('ADMIN')
  self.win.mainloop()

 def add_member(self):
    self.A = Tk()
    self.A.title('ADD MEMBERS')
    self.A.geometry('1000x600')
    self.A.configure(bg = "gray")
    self.mid = Frame(self.A, bg='white')
    self.l = Label(self.A,text='ADD MEMBER DETAILS', bg='black', fg='white',font=('algerian',60,'bold'),justify = CENTER).pack(fill=X);
    self.Name = Label(self.mid, text='Name', font=('times',18), bg='white')
    self.Name.grid(row=1, column=1, padx=50)
    self.Id   = Label(self.mid, text='Jersey Number', font=('times',18), bg='white')
    self.Id.grid(row=2, column=1, padx=50)
    self.Name = Entry(self.mid, bd=5, width=50)
    self.Name.grid(row=1, column=2, padx=50, pady=10)
    self.Id   = Entry(self.mid, bd=5, width=50)
    self.Id.grid(row=2, column=2, padx=50, pady=10)
    self.type = Label(self.mid, text='Type', font=('times',18), bg='white')
    self.type.grid(row=3,column=1)
    self.variable = StringVar(self.mid)
    self.variable.set("Batsman")
    self.type = OptionMenu(self.mid, self.variable, 'Batsman', 'Bowler', 'All Rounder', 'Wicket-Keeper')
    self.type.grid(row=3, column=2, ipadx=50)
    self.type.configure(bg='gray80', cursor='hand1', bd=5)
    self.ok = Button(self.mid, text='Press Ok', cursor='hand1',bg='gray80', command=self.Type).grid(row=3, column=3, padx=10)
    self.mid.pack(pady=50,ipady=10)
    self.A.mainloop()
 def Type(self):
     if self.variable.get() == 'Batsman' or self.variable.get() == 'Wicket-Keeper':
         self.Match = Label(self.mid, text='Total Matches', font=('times',18), bg='white')
         self.Match.grid(row=4, column=1, padx=50)
         self.Match = Entry(self.mid, bd=5, width=50)
         self.Match.grid(row=4, column=2, padx=50, pady=10)
         self.Run = Label(self.mid, text='Total Runs', font=('times',18), bg='white')
         self.Run.grid(row=5, column=1, padx=50)
         self.Run = Entry(self.mid, bd=5, width=50)
         self.Run.grid(row=5, column=2, padx=50, pady=10)
         self.Rate = Label(self.mid, text='Strike Rate', font=('times',18), bg='white')
         self.Rate.grid(row=6, column=1, padx=50)
         self.Rate = Entry(self.mid, bd=5, width=50)
         self.Rate.grid(row=6, column=2, padx=50, pady=10)
         self.submit = Button(self.mid, text='SUBMIT', bg='gray80', cursor='hand1', bd=6, command=self.create_database).grid(row=7, column=3, padx=50, pady=10)
     elif self.variable.get() == 'Bowler':
         self.Match = Label(self.mid, text='Total Matches', font=('times',18), bg='white')
         self.Match.grid(row=4, column=1, padx=50)
         self.Match = Entry(self.mid, bd=5, width=50)
         self.Match.grid(row=4, column=2, padx=50, pady=10)
         self.Wicket = Label(self.mid, text='Total Wickets', font=('times',18), bg='white')
         self.Wicket.grid(row=5, column=1, padx=50)
         self.Wicket = Entry(self.mid, bd=5, width=50)
         self.Wicket.grid(row=5, column=2, padx=50, pady=10)
         self.Eco = Label(self.mid, text='Economy', font=('times',18), bg='white')
         self.Eco.grid(row=6, column=1, padx=50)
         self.Eco = Entry(self.mid, bd=5, width=50)
         self.Eco.grid(row=6, column=2, padx=50, pady=10)
         self.submit = Button(self.mid, text='SUBMIT', bg='gray80', cursor='hand1', bd=6, command=self.create_database).grid(row=7, column=3, padx=50, pady=10)
     elif self.variable.get() == 'All Rounder':
         self.Match = Label(self.mid, text='Total Matches', font=('times',18), bg='white')
         self.Match.grid(row=4, column=1, padx=50)
         self.Match = Entry(self.mid, bd=5, width=50)
         self.Match.grid(row=4, column=2, padx=50, pady=10)
         self.Run = Label(self.mid, text='Total Runs', font=('times',18), bg='white')
         self.Run.grid(row=5, column=1, padx=50)
         self.Run = Entry(self.mid, bd=5, width=50)
         self.Run.grid(row=5, column=2, padx=50, pady=10)
         self.Rate = Label(self.mid, text='Strike Rate', font=('times',18), bg='white')
         self.Rate.grid(row=6, column=1, padx=50)
         self.Rate = Entry(self.mid, bd=5, width=50)
         self.Rate.grid(row=6, column=2, padx=50, pady=10)
         self.Wicket = Label(self.mid, text='Total Wickets', font=('times',18), bg='white')
         self.Wicket.grid(row=7, column=1, padx=50)
         self.Wicket = Entry(self.mid, bd=5, width=50)
         self.Wicket.grid(row=7, column=2, padx=50, pady=10)
         self.Eco = Label(self.mid, text='Economy', font=('times',18), bg='white')
         self.Eco.grid(row=8, column=1, padx=50)
         self.Eco = Entry(self.mid, bd=5, width=50)
         self.Eco.grid(row=8, column=2, padx=50, pady=10)
         self.submit = Button(self.mid, text='SUBMIT', bg='gray80', cursor='hand1', bd=6, command=self.create_database).grid(row=9, column=3, padx=50)
         
 def create_database(self):
    self.conn = sqlite3.connect('player.db')
    self.c    = self.conn.cursor();
    self.c.execute('''CREATE TABLE IF NOT EXISTS player(name CHAR(32) NOT NULL,id varchar(3) PRIMARY KEY NOT NULL,TYPE CHAR(12),TOTALMATCHES int,RUN int,STRIKERATE int,WICKET int,ECONOMY int);''')
    if self.variable.get() == 'Batsman' or self.variable.get() == 'Wicket-Keeper':
        self.c.execute("""INSERT INTO player (name,id,TYPE,TOTALMATCHES,RUN,STRIKERATE) VALUES(?,?,?,?,?,?)""",(self.Name.get(),self.Id.get(),self.variable.get(),self.Match.get(),self.Run.get(),self.Rate.get()))
    elif self.variable.get() == 'Bowler':
        self.c.execute("""INSERT INTO player (name,id,TYPE,TOTALMATCHES,WICKET,ECONOMY) VALUES(?,?,?,?,?,?)""",(self.Name.get(),self.Id.get(),self.variable.get(),self.Match.get(),self.Wicket.get(),self.Eco.get()))
    elif self.variable.get() == 'All Rounder':
        self.c.execute("""INSERT INTO player (name,id,TYPE,TOTALMATCHES,RUN,STRIKERATE,WICKET,ECONOMY) VALUES(?,?,?,?,?,?,?,?)""",(self.Name.get(),self.Id.get(),self.variable.get(),self.Match.get(),self.Run.get(),self.Rate.get(),self.Wicket.get(),self.Eco.get()))
    self.conn.commit();
    messagebox.showinfo('Comitted','SUCCESSFULLY ADDED')
    self.conn.close();
    self.A.destroy()

 def view_member(self):
    self.conn = sqlite3.connect('player.db')
    self.c    = self.conn.cursor();
    for row in self.conn.execute('SELECT * FROM player'):
        print(row);
    messagebox.showinfo('INFORMATION','RESULTS ARE DISPLAYED IN SHELL')
    self.conn.close();
 def search_member(self):
    self.B = Tk()
    self.B.title('SEARCH MEMBERS')
    self.B.geometry('1000x600')
    self.B.configure(bg = "gray")
    self.mid = Frame(self.B, bg='white')
    self.l = Label(self.B,text='SEARCH MEMBER DETAILS', bg='black', fg='white',font=('algerian',60,'bold'),justify = CENTER).pack(fill=X);
    self.Sid = Label(self.mid, text='Search Id', font=('times',18), bg='white')
    self.Sid.grid(row=1, column=1, padx=50, pady=50)
    self.Sid   = Entry(self.mid, bd=5, width=50)
    self.Sid.grid(row=1, column=2, padx=50, pady=50)
    self.Search = Button(self.mid, text='SEARCH', bg='gray80', cursor='hand1', bd=6, command=self.search_database).grid(row=7, column=3, padx=50, pady=10)
    self.mid.pack(pady=100)
    self.B.mainloop()
 def search_database(self):
    self.conn = sqlite3.connect('player.db')
    self.c    = self.conn.cursor();
    for row in self.c.execute("SELECT * FROM PLAYER"):
        if self.Sid.get()==row[1]:
            print(row)
    self.conn.close();
    messagebox.showinfo('INFORMATION','SEARCH RESULTS ARE DISPLAYED IN SHELL')
    self.B.destroy()
 def delete_member(self):
    self.D = Tk()
    self.D.title('DELETE MEMBERS')
    self.D.geometry('1000x600')
    self.D.configure(bg = "gray")
    self.mid = Frame(self.D, bg='white')
    self.l = Label(self.D,text='DELETE MEMBER DETAILS', bg='black', fg='white',font=('algerian',60,'bold'),justify = CENTER).pack(fill=X);
    self.Did = Label(self.mid, text='Delete Id', font=('times',18), bg='white')
    self.Did.grid(row=1, column=1, padx=50, pady=50)
    self.Did   = Entry(self.mid, bd=5, width=50)
    self.Did.grid(row=1, column=2, padx=50, pady=50)
    self.Delete = Button(self.mid, text='DELETE', bg='gray80', cursor='hand1', bd=6, command=self.delete_database).grid(row=7, column=3, padx=50, pady=10)
    self.mid.pack(pady=100)
    self.D.mainloop()
 def delete_database(self):
    self.conn = sqlite3.connect('player.db')
    self.c    = self.conn.cursor();
    for row in self.c.execute("SELECT * FROM PLAYER"):
        if self.Did.get()==row[1]:
            self.c.execute('''DELETE FROM player WHERE id='%s';'''% self.Did.get().strip())
    self.conn.commit();
    messagebox.showinfo('Comitted','SUCCESSFULLY DELETED')
    self.conn.close();
    self.D.destroy()
e = team()
