from datetime import datetime
import pytz
from tkinter import *
import time

root = Tk()
root.title("World Clock")
root.configure(bg='#abdbe3') #background
root.geometry('1200x400')

#main window logo
logo = PhotoImage(file='logo.png')
image_label = Label(root, image=logo, bg='#abdbe3').place(x=5, y=0)

#main window icon
main_window_icon = PhotoImage(file='icon.png')
root.iconphoto(False, main_window_icon)

#timezones
def times():
    home = pytz.timezone('Europe/London')
    local_time = datetime.now(home)
    current_time = local_time.strftime('%a %H:%M:%S')
    clock.config(text=current_time)
    location.config(text='United Kingdom')
    clock.after(200, times)

    home1 = pytz.timezone('Africa/Lagos')
    local_time1 = datetime.now(home1)
    current_time1 = local_time1.strftime('%a %H:%M:%S')
    clock_ng.config(text=current_time1)
    location_1.config(text='Nigeria')
    clock_ng.after(200, times)

    home2 = pytz.timezone('Africa/Cape Town')
    local_time2 = datetime.now(home2)
    current_time3 = local_time2.strftime('%a %H:%M:%S')
    clock_za.config(text=current_time3)
    location_2.config(text='South Africa')
    clock_za.after(200, times)

    home_8 = pytz.timezone('America/Los Angeles')
    local_time_8 = datetime.now(home_8)
    current_time_8 = local_time_8.strftime('%a %H:%M:%S')
    clock_us.config(text=current_time_8)
    location_8.config(text='USA')
    clock_us.after(200, times)

    home3 = pytz.timezone('Africa/Kenya')
    local_time3 = datetime.now(home3)
    current_time3 = local_time3.strftime('%a %H:%M:%S')
    clock_kenya.config(text=current_time3)
    location_3.config(text='Kenya')
    clock_kenya.after(200, times)

    home6 = pytz.timezone('Asia/Shanghai')
    local_time6 = datetime.now(home6)
    current_time6 = local_time6.strftime('%a %H:%M:%S')
    clock_china.config(text=current_time6)
    location_6.config(text='China')
    clock_china.after(200, times)


#time zone gmt
gmt = Frame(root, bd=5, bg='#abdbe3')
gmt.place(x=10, y=118, width=220, height=150)

location = Label(gmt, font=('Raleway', 14, 'bold'), bg='#abdbe3')
location.place(x=5, y=70)

ukFlag = PhotoImage(file='uk.png')
flag_uk = Label(gmt, image=ukFlag, bg='#abdbe3')
flag_uk.place(x=10, y=10)

clock = Label(gmt, font=('Raleway', 14), bg='#abdbe3')
clock.place(x=5, y=95)

#time zone gmt+1
gmt_1 = Frame(root, bd=5, bg='#abdbe3')
gmt_1.place(x=230, y=118, width=220, height=150)

location_1 = Label(gmt_1, font=('Raleway', 18, 'bold'), bg='#abdbe3')
location_1.place(x=5, y=70)

naijaFlag = PhotoImage(file='naija.png')
flag_ng= Label(gmt_1, image=naijaFlag, bg='#abdbe3')
flag_ng.place(x=10, y=10)

clock_ng = Label(gmt_1, font=('Raleway', 20), bg='#abdbe3')
clock_ng.place(x=5, y=95)

#time zone gmt+2
gmt_2 = Frame(root, bd=5, bg='#abdbe3')
gmt_2.place(x=450, y=118, width=220, height=150)

location_2 = Label(gmt_2, font=('Raleway', 18, 'bold'), bg='#abdbe3')
location_2.place(x=5, y=70)

mzanziFlag = PhotoImage(file='sa.png')
flag_za= Label(gmt_2, image=mzanziFlag, bg='#abdbe3')
flag_za.place(x=10, y=10)

clock_za = Label(gmt_2, font=('Raleway', 20), bg='#abdbe3')
clock_za.place(x=5, y=95)

#time zone gmt-8
gmt_8 = Frame(root, bd=5, bg='#abdbe3')
gmt_8.place(x=670, y=118, width=220, height=150)

location_8 = Label(gmt_8, font=('Raleway', 18, 'bold'), bg='#abdbe3')
location_8.place(x=5, y=70)

usFlag = PhotoImage(file='usa.png')
flag_us= Label(gmt_8, image=usFlag, bg='#abdbe3')
flag_us.place(x=10, y=10)

clock_us = Label(gmt_8, font=('Raleway', 20), bg='#abdbe3')
clock_us.place(x=5, y=95)

#time zone gmt+3
gmt_3 = Frame(root, bd=5, bg='#abdbe3')
gmt_3.place(x=890, y=118, width=220, height=150)

location_3 = Label(gmt_3, font=('Raleway', 18, 'bold'), bg='#abdbe3')
location_3.place(x=5, y=70)

kenyaFlag = PhotoImage(file='kenya.png')
flag_kenya= Label(gmt_3, image=kenyaFlag, bg='#abdbe3')
flag_kenya.place(x=10, y=10)

clock_kenya = Label(gmt_3, font=('Raleway', 20), bg='#abdbe3')
clock_kenya.place(x=5, y=95)

#time zone gmt+6
gmt_6 = Frame(root, bd=5, bg='#abdbe3')
gmt_6.place(x=1210, y=118, width=220, height=150)

location_6 = Label(gmt_3, font=('Raleway', 18, 'bold'), bg='#abdbe3')
location_6.place(x=5, y=70)

chinaFlag = PhotoImage(file='china.png')
flag_china= Label(gmt_3, image=chinaFlag, bg='#abdbe3')
flag_china.place(x=10, y=10)

clock_china = Label(gmt_3, font=('Raleway', 20), bg='#abdbe3')
clock_china.place(x=5, y=95)

times()

root.mainloop()