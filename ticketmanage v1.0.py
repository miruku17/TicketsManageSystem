#!/usr/bin/env python
# coding: utf-8

# In[97]:


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from random import randint
from sqlalchemy import ForeignKey,select
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import sessionmaker
import numpy as np





HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "ticketsystem"
USERNAME = "root"
PASSWORD = "110303"
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".     format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)
conn = engine.connect()
result = conn.execute("select 1")
print(result.fetchone())


# In[98]:


import tkinter as tk  
import tkinter.messagebox
import pickle

n=np.random.randint(0,1000)
window = tk.Tk()


window.title("欢迎使用铁路客票系统！")

window.geometry('500x600') 
canvas = tk.Canvas(window, width=400, height=135, bg='pink')
canvas.pack(side='top')
tk.Label(window, text='铁路客票服务系统欢迎您',font=('Arial', 16)).pack()

 

tk.Label(window, text='用户名:', font=('Arial', 14)).place(x=10, y=170)

tk.Label(window, text='密码:', font=('Arial', 14)).place(x=10, y=210)

#用户名
var_usr_name = tk.StringVar()
var_usr_name.set('在此键入您的用户名')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120,y=175)

# 用户密码
var_usr_pwd = tk.IntVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120,y=215)




purchased_ticket_id=0

usr_name="test"

lookup_ticket_id=0


# 定义用户登录功能

def usr_login():

    # 获取用户输入的usr_name和usr_pwd

    global usr_name
    
    usr_name = var_usr_name.get()

    usr_pwd = var_usr_pwd.get()
    
    Base=declarative_base()

    md = MetaData(bind=engine) #引用MetaData

    class user_info(Base):
        __table__ = Table("user_info", md, autoload=True)
    
    Session=sessionmaker(bind=engine)
    session=Session()

    record = session.query(user_info).filter(user_info.usr_name == usr_name).first()


    if (record.usr_pwd == usr_pwd):
        print("匹配成功")
        tkinter.messagebox.showinfo(title='Welcome', message='欢迎使用铁路客票服务系统！ ' + usr_name)
        Buy_Ticket()

    else:
        tk.messagebox.showerror(message='密码输入错误，请重试')

 
def usr_sign_up():

    def sign_to_system():

        # 以下三行就是获取我们注册时所输入的信息

        np = new_pwd.get()

        npf = new_pwd_confirm.get()

        nn = new_name.get()
        
        nphone = new_phone.get()

 

        

        md = MetaData(bind=engine)
        user_info = Table('user_info', md, autoload=True)

        # 判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!

        if np != npf:

            tkinter.messagebox.showerror('错误', '两次密码输入请保持一致！')

        ins_usr=  user_info.insert()
        ins_usr.execute(
          usr_id=n,
          usr_name=nn,
          usr_pwd=np, 
          usr_phone=nphone
                       )
        tkinter.messagebox.showinfo('Welcome', '恭喜！您已成功注册！')

        window_sign_up.destroy()
    


    window_sign_up = tk.Toplevel(window)

    window_sign_up.geometry('300x200')

    window_sign_up.title('Sign up window')

 

    new_name = tk.StringVar()  # 将输入的注册名赋值给变量

    #new_name.set('example@tlxxxt.com')  

    tk.Label(window_sign_up, text='请输入用户名: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。

    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`

    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

 

    new_pwd = tk.StringVar()

    tk.Label(window_sign_up, text='密码 ').place(x=10, y=50)

    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')

    entry_usr_pwd.place(x=130, y=50)

 

    new_pwd_confirm = tk.StringVar()

    tk.Label(window_sign_up, text='请再次输入密码 ').place(x=10, y=90)

    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')

    entry_usr_pwd_confirm.place(x=130, y=90)
    
    new_phone = tk.StringVar()
    tk.Label(window_sign_up,text='请输入电话号码').place(x=10,y=130)
    entry_usr_phone = tk.Entry(window_sign_up, textvariable=new_phone)
    entry_usr_phone.place(x=130, y=130)
    

 

    

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_to_system)

    btn_comfirm_sign_up.place(x=180, y=170)
    
btn_login = tk.Button(window, text='登陆', command=usr_login)
btn_login.place(x=120, y=240)
btn_sign_up = tk.Button(window, text='新用户？请注册新账户', command=usr_sign_up)
btn_sign_up.place(x=200, y=240)


var_admin_name = tk.StringVar() 
var_admin_pwd = tk.StringVar()
    

def admin_login():
    def verify_admin():
        admin_name= var_admin_name.get()
        admin_pwd = var_admin_pwd.get()
        print(admin_name)
        print(admin_pwd)
        Base=declarative_base()
        md = MetaData(bind=engine) #引用MetaData
        
        class admin_info(Base):
            __table__ = Table("admin_info", md, autoload=True)
        Session=sessionmaker(bind=engine)
        session=Session()
        record = session.query(admin_info).filter(admin_info.admin_name==admin_name).first()
        print("成功打开数据库")
        print(record.admin_pwd)
        if(record.admin_pwd == admin_pwd):
            print("匹配成功")
            tkinter.messagebox.showinfo(title='Welcome', message='欢迎使用系统管理功能!    ' + admin_name)
            admin_manage()
            window_admin_login.destroy()
        else:
            print("匹配失败")
            tkinter.messagebox.showerror(message='密码输入错误，请重试')
    
   
    
    
   
    
    window_admin_login = tk.Toplevel(window)
    window_admin_login.geometry('300x200')
    window_admin_login.title('管理员登陆')
    
    #获得用户输入的值
    
    #管理员名
    
    tk.Label(window_admin_login, text='管理员账户名 ').place(x=50, y=10)  # 放置管理员登陆
    entry_admin_name = tk.Entry(window_admin_login, textvariable=var_admin_name) #创建entry
    entry_admin_name.place(x=130, y=10)  

    #管理员密码
   
    tk.Label(window_admin_login, text='管理员账户密码').place(x=40, y=50) #放置管理员登陆密码
    entry_admin_pwd = tk.Entry(window_admin_login, textvariable=var_admin_pwd, show='*') #创建entry
    entry_admin_pwd.place(x=130, y=50)
                             
    btn_sign_up=tk.Button(window_admin_login,text='登陆',command=verify_admin)
    btn_sign_up.place(x=150,y=100)

btn_admin_login = tk.Button(window, text='管理员登陆', command=admin_login)
btn_admin_login.place(x=400, y=240)

var_line_id = tk.StringVar() 
var_line_station_1 = tk.StringVar()
var_line_station_2 = tk.StringVar() 
var_line_station_3 = tk.StringVar()
var_line_station_4 = tk.StringVar()
var_line_station_5 = tk.StringVar()
int_line_distance = tk.IntVar()

int_station_id = tk.IntVar()
var_station_name = tk.StringVar()
var_station_open = tk.StringVar()
var_station_close = tk.StringVar()
var_station_location = tk.StringVar()

int_ticket_id = tk.IntVar()
var_start_station = tk.StringVar()
var_terminal_station = tk.StringVar()
var_stopping_station = tk.StringVar()
int_ticket_price = tk.IntVar()
int_available_seats = tk.IntVar()
var_go_time = tk.StringVar()
var_arr_time = tk.StringVar()
var_line_id = tk.StringVar()
var_train_id = tk.StringVar()



def admin_manage():
    window_admin_manage=tk.Toplevel(window)
    window_admin_manage.geometry('500x500')
    window_admin_manage.title('信息管理系统')
    Base=declarative_base()
    md = MetaData(bind=engine) #引用MetaData
    class user_info(Base):
        __table__ = Table("user_info", md, autoload=True)
    class tickets_info(Base):
        __table__ = Table("tickets_info", md, autoload=True) 
    class line_info(Base):
        __table__ = Table("line_info", md, autoload=True)
    class station_info(Base):
        __table__ = Table("station_info", md, autoload=True)
    Session=sessionmaker(bind=engine)
    session=Session()
    record=session.query(user_info.usr_id,user_info.usr_name,user_info.ticket_id,user_info.usr_phone).all()#显示用户的信息。
    lb = tk.Listbox(window_admin_manage,width=50) 
    tk.Label(window_admin_manage,text='当前注册用户的信息如下：').pack()
    tk.Label(window_admin_manage,text='用户id 用户名 用户已购票ID 用户电话号码').pack()
    for item in record:
        lb.insert('end', item)  # 从最后一个位置开始加入值
    lb.pack()
    
    def CallOn():
        lookup_ticket=lb.get(lb.curselection())
        global lookup_ticket_id
        lookup_ticket_id=lookup_ticket[2] 
        print(lookup_ticket_id)
        root1=tk.Toplevel(window)    
        tk.Label(root1,text="当前选中用户的客票信息如下").pack()
        result=session.query(tickets_info.start_station,tickets_info.terminal_station,tickets_info.stopping_station,tickets_info.ticket_price,tickets_info.available_seats,tickets_info.go_time,tickets_info.arr_time).filter(tickets_info.ticket_id==lookup_ticket_id).first()
        lb2 = tk.Listbox(root1,width=50) 
        lb2.insert('end',result)
        lb2.pack()
        
        def Admin_Return():
            result1 = session.query(tickets_info).filter(tickets_info.ticket_id==lookup_ticket_id).first()
            result1.available_seats=result1.available_seats+1     #恢复原来的信息,座位加一
            session.commit()
            
            result2 = session.query(user_info).filter(user_info.ticket_id==lookup_ticket_id).first()
            result2.ticket_id=0                                    #恢复原来的信息
            session.commit()
            
            tkinter.messagebox.showinfo('success', '成功为该用户办理退票手续！')
        
       
            
        tk.Button(root1,text='为其办理退票手续',command=Admin_Return).pack()
        tk.Button(root1,text='取消',command=root1.destroy).pack()
    def Station():
        window_station=tk.Toplevel(window)
        window_station.geometry('500x500')
        window_station.title("查看/修改站点信息")
        station_record=session.query(station_info.station_id,
                                  station_info.station_name,
                                  station_info.station_open,
                                  station_info.station_close,
                                  station_info.station_location).all()
        
        lb4 = tk.Listbox(window_station,width=50) 
        tk.Label(window_station,text='当前站点信息如下：').pack()
        for item in station_record:
            lb4.insert('end', item)  # 从最后一个位置开始加入值
        lb4.pack()#显示线路信息
        def AddStation():
            def new_station():
                stationid=int_station_id.get()
                st_name=var_station_name.get()
                st_open=var_station_open.get()
                st_close=var_station_close.get()
                st_location=var_station_location.get()
                
                md = MetaData(bind=engine)
                station_info = Table('station_info', md, autoload=True)
                
                ins_station=  station_info.insert()
                
                ins_station.execute(
                    station_id=stationid,
                    station_name=st_name,
                    station_open=st_open,
                    station_close=st_close,
                    station_location=st_location
                                  )
                tkinter.messagebox.showinfo('success', '成功添加新站点信息')
            
            window_add_station=tk.Toplevel(window)
            window_add_station.geometry('300x300')
            window_add_station.title("新增站点信息")
            
            tk.Label(window_add_station, text='站点ID').place(x=50, y=10)  # 放置站点编号输入框
            entry_station_id = tk.Entry(window_add_station, textvariable=int_station_id) #创建entry
            entry_station_id.place(x=130, y=10) 
            
            tk.Label(window_add_station, text='站点名称').place(x=50, y=40)  # 放置站点名称输入框
            entry_station_name = tk.Entry(window_add_station, textvariable=var_station_name) #创建entry
            entry_station_name.place(x=130, y=40)
            
            tk.Label(window_add_station, text='站点开放时刻').place(x=50, y=70)  # 放置站点开放时间输入框
            entry_station_open = tk.Entry(window_add_station, textvariable=var_station_open) #创建entry
            entry_station_open.place(x=130, y=70)
            
            tk.Label(window_add_station, text='站点关闭时刻').place(x=50, y=110)  # 放置站点关闭时间输入框
            entry_station_close = tk.Entry(window_add_station, textvariable=var_station_close) #创建entry
            entry_station_close.place(x=130, y=110)
            
            tk.Label(window_add_station, text='站点所在地').place(x=50, y=140)  # 放置站点所在地输入框
            entry_station_location = tk.Entry(window_add_station, textvariable=var_station_location) #创建entry
            entry_station_location.place(x=130, y=140) 
            
            add_station=tk.Button(window_add_station,text='增加此站点信息',command=new_station)
            add_station.place(x=95,y=200)  
            
        add_station=tk.Button(window_station,text='增加站点信息',command=AddStation)
        add_station.place(x=180,y=330)
        
        def DelStation():
            def confirm_del_station():
                dele_station=session.query(station_info).filter(station_info.station_id==lookup_station_id).first()
                session.delete(dele_station)
                session.commit()
                tkinter.messagebox.showinfo('success', '成功删除此站点信息')
                
            root6=tk.Toplevel(window)    
            tk.Label(root6,text='将删除'+str(lb4.get(lb4.curselection()))+'站点').pack()
            lookup_station=lb4.get(lb4.curselection())
            lookup_station_id=lookup_station[0] 
            print(lookup_station_id)
            tk.Button(root6,text='确定',command=confirm_del_station).pack()
            tk.Button(root6,text='取消',command=root6.destroy).pack()
        
        del_station=tk.Button(window_station,text='删除当前选中站点信息',command=DelStation)
        del_station.place(x=180,y=360)
    
    def Ticket():
        window_ticket=tk.Toplevel(window)
        window_ticket.geometry('500x500')
        window_ticket.title("客票信息管理")
        ticket_record=session.query(tickets_info.ticket_id,tickets_info.start_station,
                                    tickets_info.terminal_station,tickets_info.stopping_station,
                                    tickets_info.ticket_price,tickets_info.available_seats,
                                    tickets_info.go_time,tickets_info.arr_time,
                                    tickets_info.line_id).all() #查询客票信息
        
        lb7 = tk.Listbox(window_ticket,width=50) 
        tk.Label(window_ticket,text='当前现有客票信息如下：').pack()
        for item in ticket_record:
            lb7.insert('end', item)  # 从最后一个位置开始加入值
        lb7.pack()#显示线路信息
        
        def AddTicket():
            def new_ticket():
                ticketid = int_ticket_id.get()
                start = var_start_station.get()
                terminal = var_terminal_station.get() 
                stopping = var_stopping_station.get()
                price = int_ticket_price.get()
                seats = int_available_seats.get()
                go = var_go_time.get()
                arr = var_arr_time.get()
                lineid = var_line_id.get()
                trainid = var_train_id.get()
                
                md = MetaData(bind=engine)
                tickets_info = Table('tickets_info', md, autoload=True)
                
                ins_ticket=  tickets_info.insert()
                
                ins_ticket.execute(
                    ticket_id=ticketid,
                    start_station=start,
                    terminal_station=terminal,
                    stopping_station=stopping,
                    ticket_price=price,
                    available_seats=seats,
                    go_time=go,
                    arr_time=arr,
                    line_id=lineid,
                    train_id=trainid
                                  )
                tkinter.messagebox.showinfo('success', '成功添加可购买客票')
            
            window_add_ticket=tk.Toplevel(window)
            window_add_ticket.geometry('300x500')
            window_add_ticket.title("新增可购买购票") #设置新增客票窗口
            
            
            tk.Label(window_add_ticket, text='客票ID').place(x=50, y=10)  # 放置站点编号输入框
            entry_ticket_id = tk.Entry(window_add_ticket, textvariable=int_ticket_id) #创建entry
            entry_ticket_id.place(x=130, y=10)
            
            tk.Label(window_add_ticket, text='始发站').place(x=50, y=40)  # 放置始发站输入框
            entry_start_station = tk.Entry(window_add_ticket, textvariable=var_start_station) #创建entry
            entry_start_station.place(x=130, y=40)
            
            tk.Label(window_add_ticket, text='终点站').place(x=50, y=70)  # 放置站点编号输入框
            entry_terminal_station = tk.Entry(window_add_ticket, textvariable=var_terminal_station) #创建entry
            entry_terminal_station.place(x=130, y=70)
            
            tk.Label(window_add_ticket, text='经停站').place(x=50, y=100)  # 放置站点编号输入框
            entry_stopping_station = tk.Entry(window_add_ticket, textvariable=var_stopping_station) #创建entry
            entry_stopping_station.place(x=130, y=100)
            
            tk.Label(window_add_ticket, text='票价').place(x=50, y=130)  # 放置站点编号输入框
            entry_ticket_price = tk.Entry(window_add_ticket, textvariable=int_ticket_price) #创建entry
            entry_ticket_price.place(x=130, y=130)
            
            tk.Label(window_add_ticket, text='可用座位').place(x=50, y=160)  # 放置站点编号输入框
            entry_available_seats = tk.Entry(window_add_ticket, textvariable=int_available_seats) #创建entry
            entry_available_seats.place(x=130, y=160)
            
            tk.Label(window_add_ticket, text='出发时间').place(x=50, y=190)  # 放置站点编号输入框
            entry_go_time = tk.Entry(window_add_ticket, textvariable=var_go_time) #创建entry
            entry_go_time.place(x=130, y=190)
            
            tk.Label(window_add_ticket, text='到达时间').place(x=50, y=230)  # 放置站点编号输入框
            entry_arr_time = tk.Entry(window_add_ticket, textvariable=var_arr_time) #创建entry
            entry_arr_time.place(x=130, y=230)
            
            tk.Label(window_add_ticket, text='线路ID').place(x=50, y=260)  # 放置站点编号输入框
            entry_line_id = tk.Entry(window_add_ticket, textvariable=var_line_id) #创建entry
            entry_line_id.place(x=130, y=260)
            
            tk.Label(window_add_ticket, text='列车ID').place(x=50, y=290)  # 放置站点编号输入框
            entry_train_id = tk.Entry(window_add_ticket, textvariable=var_train_id) #创建entry
            entry_train_id.place(x=130, y=290)
            
            confirm_add_ticket=tk.Button(window_add_ticket,text='增加此客票到系统中',command=new_ticket)
            confirm_add_ticket.place(x=95,y=350)
        
        add_ticket=tk.Button(window_ticket,text='新增可购买客票',command=AddTicket)
        add_ticket.place(x=180,y=360)
        
        def DelTicket():
            def confirm_del_ticket():
                dele_ticket=session.query(tickets_info).filter(tickets_info.ticket_id==lookup_del_ticket_id).first()
                session.delete(dele_ticket)
                session.commit()
                tkinter.messagebox.showinfo('success', '成功删除此客票信息')
                
            root9=tk.Toplevel(window)    
            tk.Label(root9,text='将删除'+str(lb7.get(lb7.curselection()))+'客票').pack()
            lookup_del_ticket=lb7.get(lb7.curselection())
            lookup_del_ticket_id=lookup_del_ticket[0] 
            print(lookup_del_ticket_id)
            tk.Button(root9,text='确定',command=confirm_del_ticket).pack()
            tk.Button(root9,text='取消',command=root9.destroy).pack()
        
        dele_ticket=tk.Button(window_ticket,text='从系统中删除当前选中客票',command=DelTicket)
        dele_ticket.place(x=180,y=400)
        
    
            
        
            
            
            
                
                
    
    lookup_ticket=tk.Button(window_admin_manage,text='管理客票信息',command=Ticket)
    lookup_ticket.place(x=180,y=360)
    
        
        
        
        
    
    def Line():
        window_line=tk.Toplevel(window)
        window_line.geometry('500x500')
        window_line.title("查看/修改线路信息")
        line_record=session.query(line_info.line_id,line_info.line_station_1,
                                  line_info.line_station_2,line_info.line_station_3,
                                  line_info.line_station_4,line_info.line_station_5,line_info.line_distance).all()
        #查询线路信息
        
        lb3 = tk.Listbox(window_line,width=50) 
        tk.Label(window_line,text='当前线路信息如下：').pack()
        for item in line_record:
            lb3.insert('end', item)  # 从最后一个位置开始加入值
        lb3.pack()#显示线路信息
        
        def AddLine():#增加线路信息
            def new_line():
                lineid=var_line_id.get()
                station1=var_line_station_1.get()
                station2=var_line_station_2.get()
                station3=var_line_station_3.get()
                station4=var_line_station_4.get()
                station5=var_line_station_5.get()
                distance=int_line_distance.get()
                
                md = MetaData(bind=engine)
                line_info = Table('line_info', md, autoload=True)
                
                ins_line=  line_info.insert()
                
                ins_line.execute(
                    line_id=lineid,
                    line_station_1=station1,
                    line_station_2=station2,
                    line_station_3=station3,
                    line_station_4=station4,
                    line_station_5=station5,
                    line_distance=distance
                                )
                tkinter.messagebox.showinfo('success', '成功添加新线路信息')
            
                
            window_add_line=tk.Toplevel(window)
            window_add_line.geometry('300x300')
            window_add_line.title("新增线路信息")
            
            tk.Label(window_add_line, text='线路ID').place(x=50, y=10)  # 放置线路编号输入框
            entry_line_id = tk.Entry(window_add_line, textvariable=var_line_id) #创建entry
            entry_line_id.place(x=130, y=10) 
            
            tk.Label(window_add_line, text='出发站').place(x=50, y=40)  
            entry_line_id = tk.Entry(window_add_line, textvariable=var_line_station_1)
            entry_line_id.place(x=130, y=40) 
            
            tk.Label(window_add_line, text='经停站1').place(x=50, y=70)  # 放置管理员登陆
            entry_line_id = tk.Entry(window_add_line, textvariable=var_line_station_2) #创建entry
            entry_line_id.place(x=130, y=70)  
            
            tk.Label(window_add_line, text='经停站2').place(x=50, y=100)  # 放置管理员登陆
            entry_line_id = tk.Entry(window_add_line, textvariable=var_line_station_3) #创建entry
            entry_line_id.place(x=130, y=100)  
            
            tk.Label(window_add_line, text='经停站3').place(x=50, y=130)  # 放置管理员登陆
            entry_line_id = tk.Entry(window_add_line, textvariable=var_line_station_4) #创建entry
            entry_line_id.place(x=130, y=130)  
            
            tk.Label(window_add_line, text='终点站').place(x=50, y=160)  # 放置管理员登陆
            entry_line_id = tk.Entry(window_add_line, textvariable=var_line_station_5) #创建entry
            entry_line_id.place(x=130, y=160) 
            
            tk.Label(window_add_line, text='线路长度').place(x=50, y=190)  # 放置管理员登陆
            entry_line_id = tk.Entry(window_add_line, textvariable=int_line_distance) #创建entry
            entry_line_id.place(x=130, y=190)  
            
            confirm_add_line=tk.Button(window_add_line,text='增加此线路信息',command=new_line)
            confirm_add_line.place(x=90,y=230)
        
        def DelLine():
            def confirm_del():
                dele_line=session.query(line_info).filter(line_info.line_id==lookup_line_id).first()
                session.delete(dele_line)
                session.commit()
                tkinter.messagebox.showinfo('success', '成功删除此线路信息')
                
            root5=tk.Toplevel(window)    
            tk.Label(root5,text='将删除'+str(lb3.get(lb3.curselection()))+'线路').pack()
            lookup_line=lb3.get(lb3.curselection())
            lookup_line_id=lookup_line[0] 
            print(lookup_line_id)
            tk.Button(root5,text='确定',command=confirm_del).pack()
            tk.Button(root5,text='取消',command=root5.destroy).pack()
            
            
            
            
    
            
            
        #增加线路信息按钮   
        add_line=tk.Button(window_line,text='增加线路信息',command=AddLine)
        add_line.place(x=180,y=330)
        #删除线路信息按钮
        del_line=tk.Button(window_line,text='删除当前选中信息',command=DelLine)
        del_line.place(x=180,y=400)
        
    lookup_usr_ticket=tk.Button(window_admin_manage,text='查询当前选中用户的客票信息',command=CallOn)
    lookup_usr_ticket.place(x=180,y=250)
    
    lookup_station=tk.Button(window_admin_manage,text='查看/修改站点信息',command=Station)
    lookup_station.place(x=180,y=290)
    
    lookup_line=tk.Button(window_admin_manage,text='查看/修改线路信息',command=Line)
    lookup_line.place(x=180,y=330)



def Buy_Ticket():
    window_ticket_buy = tk.Toplevel(window)
    window_ticket_buy.geometry('500x500')
    window_ticket_buy.title('购票')
    
    Base=declarative_base()
    md = MetaData(bind=engine) #引用MetaData
    class tickets_info(Base):
        __table__ = Table("tickets_info", md, autoload=True)
    Session=sessionmaker(bind=engine)
    session=Session()
    record=session.query(tickets_info.ticket_id,tickets_info.start_station,tickets_info.terminal_station,tickets_info.stopping_station,tickets_info.ticket_price,tickets_info.available_seats,tickets_info.go_time,tickets_info.arr_time).all()#显示客票信息。
    lb = tk.Listbox(window_ticket_buy,width=50) 
    tk.Label(window_ticket_buy,text='选择你的行程').pack()
    tk.Label(window_ticket_buy,justify="left",text='始发站 终点站 经停 票价 剩余座位 出发时间 到达时间').pack()
    for item in record:
        lb.insert('end', item)  # 从最后一个位置开始加入值
    def CallOn():    
        root1=tk.Toplevel(window)    
        tk.Label(root1,text='你的选择是'+str(lb.get(lb.curselection()))+'行程').pack()
        purchased_ticket=lb.get(lb.curselection())
        global purchased_ticket_id
        purchased_ticket_id=purchased_ticket[0] 
        print(purchased_ticket_id)
        tk.Button(root1,text='确定',command=Purchased).pack()
        tk.Button(root1,text='取消',command=root1.destroy).pack()
        
    
    #lb.bind('<Double-Button-1>',CallOn)   #绑定事件。


    lb.pack()
    
    confirm_buy=tk.Button(window_ticket_buy,text='购买当前选中客票',command=CallOn)
    confirm_buy.place(x=180,y=250)
    
    look_profile=tk.Button(window_ticket_buy,text='查看个人信息',command=Profile)
    look_profile.place(x=180,y=300)
    
    

    def Purchased():
        window_ticket_purchased=tk.Toplevel(window)
        window_ticket_purchased.title("成功")
        tk.Label(window_ticket_purchased, text="购票成功！",font=('Arial', 16)).pack()
        tk.Button(window_ticket_purchased,text='关闭',command=window_ticket_purchased.destroy).pack()
        
        Base=declarative_base()
        md = MetaData(bind=engine) #引用MetaData
        class tickets_info(Base):
            __table__ = Table("tickets_info", md, autoload=True)
        class user_info(Base):
            __table__ = Table("user_info", md, autoload=True)
        Session=sessionmaker(bind=engine)
        session=Session() 
        
        global purchased_ticket_id
        global usr_name
        
        result1 = session.query(tickets_info).filter(tickets_info.ticket_id==purchased_ticket_id).first()
        result1.available_seats=result1.available_seats-1
        
        session.commit()
        
        print(result1)

        result2 = session.query(user_info).filter(user_info.usr_name==usr_name).first()
        result2.ticket_id=purchased_ticket_id         #修改用户信息

        session.commit()
        
        print(usr_name)     
        
        print(result2)

def Profile():
    window_profile=tk.Toplevel(window)
    window_profile.geometry('500x500')
    window_profile.title('个人购票信息')
    Base=declarative_base()
    md = MetaData(bind=engine) #引用MetaData
    class tickets_info(Base):
        __table__ = Table("tickets_info", md, autoload=True)
    class user_info(Base):
        __table__ = Table("user_info", md, autoload=True)
    class line_info(Base):
        __table__ = Table("line_info", md, autoload=True)
        
    Session=sessionmaker(bind=engine)
    session=Session()
    
    global usr_name
    
    usr_ticket_id=session.query(user_info.ticket_id).filter(user_info.usr_name==usr_name)
    
    record=session.query(tickets_info.start_station,tickets_info.terminal_station,
                         tickets_info.stopping_station,tickets_info.go_time,tickets_info.arr_time,
                         tickets_info.line_id).filter(tickets_info.ticket_id==usr_ticket_id).first()
    
    lb = tk.Listbox(window_profile,width=50) 
    
    tk.Label(window_profile,text='当前最新行程如下').pack()
    # for item in record:
    lb.insert('end', record)  # 从最后一个位置开始加入值
    
    lb.pack()
    
    def LookupAllStoppingStations():     
        root11=tk.Toplevel(window)
        tk.Label(root11,text='您当前选中行程的所有经停站如下：').pack()
        usr_lookup_line=lb.get(lb.curselection())
        usr_lookup_line_id=usr_lookup_line[5]
        print(usr_lookup_line_id)
        
        record_of_line = session.query(line_info.line_station_1,line_info.line_station_2,
                                       line_info.line_station_3,line_info.line_station_4,
                                       line_info.line_station_5,line_info.line_distance).filter(line_info.line_id==usr_lookup_line_id).first()
        lb_stopping_stations = tk.Listbox(root11,width=50)
        
        lb_stopping_stations.insert('end',record_of_line)
        
        lb_stopping_stations.pack()
    
    lookup_line=tk.Button(window_profile,text='查询当前选中客票的所有经停站（线路信息）',command=LookupAllStoppingStations)
    lookup_line.place(x=180,y=300)
    
    
        
        
        
    
    def ReturnTicket(): 
        def confirm_return_ticket():
            window_ticket_returned=tk.Toplevel(window)
            window_ticket_returned.title("成功")
            tk.Label(window_ticket_returned, text="退票成功！",font=('Arial', 16)).pack()
            tk.Button(window_ticket_returned,text='关闭',command=window_ticket_returned.destroy).pack()
            
            Base=declarative_base()
            md = MetaData(bind=engine) #引用MetaData
            class tickets_info(Base):
                __table__ = Table("tickets_info", md, autoload=True)
            class user_info(Base):
                __table__ = Table("user_info", md, autoload=True)
            Session=sessionmaker(bind=engine)
            session=Session() 
            #global purchased_ticket_id
            global usr_name
            
            print(usr_name)
            
            usr_ticket = session.query(user_info).filter(user_info.usr_name==usr_name).first()
            usr_ticket_id = usr_ticket.ticket_id
            
            print(usr_ticket_id)
            
            print(type(usr_ticket_id))    
            
            seat = session.query(tickets_info).filter(tickets_info.ticket_id==usr_ticket_id).first()
            seat.available_seats=seat.available_seats+1     #恢复原来的信息,座位加一
            session.commit()
            
            ticketid = session.query(user_info).filter(user_info.ticket_id==usr_ticket_id).first()
            ticketid.ticket_id=0                                    #恢复原来的信息
            session.commit()
            
            #恢复原来的信息
            

        root1=tk.Toplevel(window)    
        tk.Label(root1,text='您将退票'+str(lb.get(lb.curselection()))+'行程').pack()
        purchased_ticket=lb.get(lb.curselection())
        
        tk.Button(root1,text='确定',command=confirm_return_ticket).pack()
        tk.Button(root1,text='取消',command=root1.destroy).pack()
    
    confirm_buy=tk.Button(window_profile,text='退选当前选中客票',command=ReturnTicket)
    confirm_buy.place(x=180,y=250)
    
    

window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




