import tkinter as tk
from tkinter import ttk
from PIL import Image ,ImageTk
import datetime
import re

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        ttkstyle = ttk.Style()
        ttkstyle.theme_use('default')
        #ttkstyle.configure('white.TFrame',background='white')
        #ttkstyle.configure('green.TFrame',background='green')
        #ttkstyle.configure('blue.TFrame',background='blue')
        ttkstyle.configure('gridlabel.TLabel',font=('Helvetica', 16),foreground = '#666666')
        ttkstyle.configure('gridentry.TEntry',font=('Helvetica', 16))

        mainframe = ttk.Frame(self)
        mainframe.pack(expand=True,fill=tk.BOTH,padx=30,pady=30)

        topframe = ttk.Frame(mainframe,height=100)
        topframe.pack(fill=tk.X)
        ttk.Label(topframe,text='BMI試算',font=('Helvetica','20')).pack(pady=(180,20))

        bottomframe = ttk.Frame(mainframe)
        bottomframe.pack(expand=True,fill=tk.BOTH)
        bottomframe.columnconfigure(0,weight=3,pad=20) 
        bottomframe.columnconfigure(1,weight=5,pad=20)
        bottomframe.rowconfigure(0,weight=1,pad=20)
        bottomframe.rowconfigure(3,weight=1,pad=20)
        bottomframe.rowconfigure(4,weight=1,pad=20)
        bottomframe.rowconfigure(5,weight=1,pad=20)
        bottomframe.rowconfigure(6,weight=1,pad=20)

        self.namestingvar = tk.StringVar()
        self.birthstingvar = tk.StringVar()
        self.heightintvar = tk.IntVar()
        self.weightintvar = tk.IntVar()


        ttk.Label(bottomframe,text='姓名:',style='gridlabel.TLabel').grid(column=0,row=0,sticky=tk.E)
        namentry = ttk.Entry(bottomframe,style='gridentry.TEntry',textvariable=self.namestingvar)
        namentry.grid(column=1,row=0,sticky=tk.W,padx=10)

        ttk.Label(bottomframe,text='出生年月日:',style='gridlabel.TLabel').grid(column=0,row=1,sticky=tk.E)        
        ttk.Label(bottomframe,text='(2000-03-01)',style='gridlabel.TLabel').grid(column=0,row=2,sticky=tk.E)
        birthentry = ttk.Entry(bottomframe,style='gridentry.TEntry',textvariable=self.birthstingvar)
        birthentry.grid(column=1,row=1,sticky=tk.W,rowspan=2,padx=10)

        ttk.Label(bottomframe,text='身高(CM):',style='gridlabel.TLabel').grid(column=0,row=3,sticky=tk.E)
        heightentry = ttk.Entry(bottomframe,style='gridentry.TEntry',textvariable=self.heightintvar)
        heightentry.grid(column=1,row=3,sticky=tk.W,padx=10)

        ttk.Label(bottomframe,text='體重(KG):',style='gridlabel.TLabel').grid(column=0,row=4,sticky=tk.E)
        weightentry = ttk.Entry(bottomframe,style='gridentry.TEntry',textvariable=self.weightintvar)
        weightentry.grid(column=1,row=4,sticky=tk.W,padx=10)

        self.messagetext = tk.Text(bottomframe,height=5,width=35,state=tk.DISABLED,takefocus=0,bd=0)
        self.messagetext.grid(column=0,row=5,sticky=tk.N+tk.S,columnspan=2)

        commitframe = ttk.Frame(bottomframe)
        commitframe.grid(column=0,row=6,columnspan=2)
        commitframe.columnconfigure(0,pad=10)

        commitbut = tk.Button(commitframe,text='計算',command=self.presscommit)
        commitbut.grid(column=0,row=0,sticky=tk.W)

        clearbut = tk.Button(commitframe,text='清除',command=self.pressclear)
        clearbut.grid(column=1,row=0,sticky=tk.E)

        logoimage = Image.open('cat.png')
        resizeimage = logoimage.resize((250,150),Image.LANCZOS)
        self.logotkimage = ImageTk.PhotoImage(resizeimage)
        logolabel = ttk.Label(self,image=self.logotkimage,width=250)
        logolabel.place(x=70,y=40)
    
    def pressclear(self,*args):
        self.namestingvar.set('')
        self.birthstingvar.set('')
        self.heightintvar.set(0)
        self.weightintvar.set(0)
        self.messagetext.configure(state=tk.NORMAL)
        self.messagetext.delete('1.0',tk.END)
        self.messagetext.configure(state=tk.DISABLED)
        print("清除")
    
    def presscommit(self):
        self.checkdata()

    def checkdata(self):
        
        namevalue = self.namestingvar.get()
        birthvalue = self.birthstingvar.get()

        #dateregex = re.compile(r"^\d\d\d\d/\d\d/\d\d$")
        #birthmatch = re.match(dateregex,birthvalue)
        #if birthmatch is None:
            #birthvalue = ''

        birthday = datetime.datetime.strptime(birthvalue, '%Y-%m-%d')
        age = datetime.datetime.now().year - birthday.year

        if birthday.year > datetime.datetime.now().year:
            self.messagetext.configure(state=tk.NORMAL)
            self.messagetext.delete('1.0',tk.END)
            self.messagetext.insert(tk.END,'輸入的年份超過2023')
            self.messagetext.configure(state=tk.DISABLED)
        else:
            month, day = birthday.month, birthday.day
        
        if month == 12 and day >= 22 or month == 1 and day <= 19:
            zodiac_sign = "摩羯座(Capricorn)"
        elif month == 1 and day >= 20 or month == 2 and day <= 18:
            zodiac_sign = "水瓶座(Aquarius)"
        elif month == 2 and day >= 19 or month == 3 and day <= 20:
            zodiac_sign = "雙鱼座(Pisces)"
        elif month == 3 and day >= 21 or month == 4 and day <= 19:
            zodiac_sign = "牡羊座(Aries)"
        elif month == 4 and day >= 20 or month == 5 and day <= 20:
            zodiac_sign = "金牛座(Taurus)"
        elif month == 5 and day >= 21 or month == 6 and day <= 21:
            zodiac_sign = "雙子座(Gemini)"
        elif month == 6 and day >= 22 or month == 7 and day <= 22:
            zodiac_sign = "巨蟹座(Cancer)"
        elif month == 7 and day >= 23 or month == 8 and day <= 22:
            zodiac_sign = "獅子座(Leo)"
        elif month == 8 and day >= 23 or month == 9 and day <= 22:
            zodiac_sign = "處女座(Virgo)"
        elif month == 9 and day >= 23 or month == 10 and day <= 22:
            zodiac_sign = "天秤座(Libra)"
        elif month == 10 and day >= 23 or month == 11 and day <= 21:
            zodiac_sign = "天蠍座(Scorpio)"
        elif month == 11 and day >= 22 or month == 12 and day <= 21:
            zodiac_sign = "射手座(Sagittarius)"
        
        try:
            heightvalue = self.heightintvar.get()
        except:
            heightvalue = 0

        try:
            weightvalue = self.weightintvar.get()
        except:
            weightvalue = 0

        if namevalue == '':
            self.messagetext.configure(state=tk.NORMAL)
            self.messagetext.delete('1.0',tk.END)
            self.messagetext.insert(tk.END,'名字格式錯誤')
            self.messagetext.configure(state=tk.DISABLED)
        elif birthvalue == '':
            self.messagetext.configure(state=tk.NORMAL)
            self.messagetext.delete('1.0',tk.END)
            self.messagetext.insert(tk.END,'生日格式錯誤')
            self.messagetext.configure(state=tk.DISABLED)
        elif heightvalue == 0:
            self.messagetext.configure(state=tk.NORMAL)
            self.messagetext.delete('1.0',tk.END)
            self.messagetext.insert(tk.END,'身高格式錯誤')
            self.messagetext.configure(state=tk.DISABLED)
        elif weightvalue == 0:
            self.messagetext.configure(state=tk.NORMAL)
            self.messagetext.delete('1.0',tk.END)
            self.messagetext.insert(tk.END,'體重格式錯誤')
            self.messagetext.configure(state=tk.DISABLED)
        else:
            BMI = weightvalue / (heightvalue / 100) ** 2
            if BMI > 18.5:
                BODY = "體重健康!!繼續保持"
            elif BMI > 24:
                BODY = "體重過重!!力行健康體重管理"
            elif BMI > 27:
                BODY = "體重肥胖!!立刻力行健康體重管理"
            else:
                BODY = "體重過輕!!"

            message = f"{namevalue}您好:\n"
            message += f"出生年月日:{birthvalue}\n"
            message += f"BMI值是:{BMI:.2f}\n"
            message += f"BMI的狀態是:{BODY}\n"
            message += f"您的年齡是{age}歲\n"
            message += f"您的星座是:{zodiac_sign}"

            self.messagetext.configure(state=tk.NORMAL)
            self.messagetext.delete('1.0',tk.END)
            self.messagetext.insert(tk.END,message)
            self.messagetext.configure(state=tk.DISABLED)

def closewindow(w):
    w.destroy()

def main():    
    window = Window()
    window.title('BMI計算')
    window.resizable(width=False,height=False)
    window.protocol('WM_DELETE_WONDOW',lambda:closewindow(window))
    window.mainloop()

if __name__=='__main__':
    main()