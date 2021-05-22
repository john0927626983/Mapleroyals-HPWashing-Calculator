import tkinter as tk
from math import pi
from PIL import ImageTk, Image
import random
import webbrowser
import os
from tkinter import ttk


def calculate():

  try:
    lv = eval(lv_text.get())
    mp = eval(mp_text.get())

    #Warrior#####################
    if var01.get() == 'Warrior':
      if (201 > lv > 30) and mp > 0:
        mp_min = (lv * 4) + 156
        extra_mp = mp - mp_min

        if extra_mp >= 4:
          washtimes = int(extra_mp/4)
          apr_cost = washtimes*3100

          get_hp=0
          for i in range(1,washtimes+1):
            get_hp += random.randrange(50,54)


          if var02.get() == 0:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP minimum = {mp_min}\nwashtimes = {washtimes}  get {get_hp} hp\ncost {apr_cost}NX'


          if var02.get() == 1: 
            message_lable['text'] = f'Extra MP = {extra_mp}  MP底線為 = {mp_min}\n洗血次數={washtimes}  增加血量={get_hp}\n花費點數={apr_cost}NX'

        else:
            if var02.get() == 0:
              message_lable['text'] ='MP is not enough'
            if var02.get() == 1: 
              message_lable['text'] ='MP過低無法洗血'

    #Fighter#####################
    elif var01.get() == 'Fighter':
      if (201 > lv > 30) and mp > 0:
        mp_min = (lv * 4) + 56
        extra_mp = mp - mp_min

        if extra_mp >= 4:
          washtimes = int(extra_mp/4)
          apr_cost = washtimes*3100

          get_hp=0
          for i in range(1,washtimes+1):
            get_hp += random.randrange(50,54)

          if var02.get() == 0:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP minimum = {mp_min}\nwashtimes = {washtimes}  get {get_hp} hp\ncost {apr_cost}NX'
          
          if var02.get() == 1:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP底線為 = {mp_min}\n洗血次數={washtimes}  增加血量={get_hp}\n花費點數={apr_cost}NX'

        else:
          if var02.get() == 0:
            message_lable['text'] ='MP is not enough'
          if var02.get() == 1:
            message_lable['text'] ='MP過低無法洗血'

    #Archer#####################
    elif var01.get() == 'Archer':
      if (201 > lv > 30) and mp > 0:
        mp_min = (lv * 14) + 148
        extra_mp = mp - mp_min

        if extra_mp >= 12:
          washtimes = int(extra_mp/12)
          apr_cost = washtimes*3100

          get_hp=0
          for i in range(1,washtimes+1):
            get_hp += random.randrange(16,20)

          if var02.get() == 0:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP minimum = {mp_min}\nwashtimes = {washtimes}  get {get_hp} hp\ncost {apr_cost}NX'

          if var02.get() == 1:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP底線為 = {mp_min}\n洗血次數={washtimes}  增加血量={get_hp}\n花費點數={apr_cost}NX'

        else:
          if var02.get() == 0:
            message_lable['text'] ='MP is not enough'
          if var02.get() == 1:
            message_lable['text'] ='MP過低無法洗血'

    #Thief#####################
    elif var01.get() == 'Thief':
      if (201 > lv > 30) and mp > 0:
        mp_min = (lv * 14) + 148
        extra_mp = mp - mp_min

        if extra_mp >= 12:
          washtimes = int(extra_mp/12)
          apr_cost = washtimes*3100

          get_hp=0
          for i in range(1,washtimes+1):
            get_hp += random.randrange(20,24)

          if var02.get() == 0:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP minimum = {mp_min}\nwashtimes = {washtimes}  get {get_hp} hp\ncost {apr_cost}NX'
          
          if var02.get() == 1:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP底線為 = {mp_min}\n洗血次數={washtimes}  增加血量={get_hp}\n花費點數={apr_cost}NX'

        else:
          if var02.get() == 0:
            message_lable['text'] ='MP is not enough'
          if var02.get() == 1:
            message_lable['text'] ='MP過低無法洗血'

    #Brawler##################
    elif var01.get() == 'Brawler':
      if (201 > lv > 33) and mp > 0:
        mp_min = (lv * 18) + 111
        extra_mp = mp - mp_min

        if extra_mp >= 16:
          washtimes = int(extra_mp/16)
          apr_cost = washtimes*3100

          get_hp=0
          for i in range(1,washtimes+1):
            get_hp += random.randrange(36,40)

          if var02.get() == 0:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP minimum = {mp_min}\nwashtimes = {washtimes}  get {get_hp} hp\ncost {apr_cost}NX'

          if var02.get() == 1:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP底線為 = {mp_min}\n洗血次數={washtimes}  增加血量={get_hp}\n花費點數={apr_cost}NX'

        else:
          if var02.get() == 0:
            message_lable['text'] ='MP is not enough'
          if var02.get() == 1:
            message_lable['text'] ='MP過低無法洗血'

    #Gunslinger##################
    elif var01.get() == 'Gunslinger':
      if (201 > lv > 30) and mp > 0:
        mp_min = (lv * 18) + 111
        extra_mp = mp - mp_min

        if extra_mp >= 16:
          washtimes = int(extra_mp/16)
          apr_cost = washtimes*3100

          get_hp=0
          for i in range(1,washtimes+1):
            get_hp += random.randrange(16,20)

          if var02.get() == 0:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP minimum = {mp_min}\nwashtimes = {washtimes}  get {get_hp} hp\ncost {apr_cost}NX'

          if var02.get() == 1:
            message_lable['text'] = f'Extra MP = {extra_mp}  MP底線為 = {mp_min}\n洗血次數={washtimes}  增加血量={get_hp}\n花費點數={apr_cost}NX'

        else:
          if var02.get() == 0:
            message_lable['text'] ='MP is not enough'
          if var02.get() == 1:
            message_lable['text'] ='MP過低無法洗血'

    else:
      if var02.get() == 0:
        message_lable['text'] ='Plese enter again'
      if var02.get() == 1:
        message_lable['text'] ='請重新輸入'
###########################################


  except:
    if var02.get() == 0:
      message_lable['text'] ='Plese enter again'
    if var02.get() == 1:
      message_lable['text'] ='請重新輸入'



def callback_function(x):
  if var01.get() == 'Warrior':
    bg_layout['image'] = job_image1

  elif var01.get() == 'Fighter':
    bg_layout['image'] = job_image2

  elif var01.get() == 'Archer':
    bg_layout['image'] = job_image3

  elif var01.get() == 'Thief':
    bg_layout['image'] = job_image4

  elif var01.get() == 'Brawler':
    bg_layout['image'] = job_image5

  elif var01.get() == 'Gunslinger':
    bg_layout['image'] = job_image6

  else:
    pass

#滑鼠事件
def on_enter(e):
  calculate_button['image']=button_image2

def on_leave(e):
  calculate_button['image']=button_image1

#主視窗

root = tk.Tk()
root.title('Mapleroyals HP Washing')
root.config(bg = 'Black')
root.geometry('1053x798+0+0')
root.resizable(False, False)

# 建立此視窗內部的版面
bg_image = ImageTk.PhotoImage(file = 'images/wallpapers/0.png')
bg_layout = tk.Label(image = bg_image)
bg_layout.config(width = 1053, height = 798)
bg_layout.place(x = 0, y = 0)
#LV
lv_label = tk.Label()
lv_label.config(anchor = 'ne', text = ' L V ', width = 5, font = ('Courier New',15), fg = 'white', bg = 'chocolate')
lv_label.place(relx = 0.48, rely = 0.46)
#MP
mp_label = tk.Label()
mp_label.config(anchor = 'ne', text = ' M P ', width = 5, font = ('Courier New',15), fg = 'white', bg = 'chocolate')
mp_label.place(relx = 0.48, rely = 0.51)
#LV輸入格
lv_text = tk.Entry()
lv_text.config(width = 10, font = ('consolas',15), fg = 'white', bg = 'chocolate')
lv_text.focus_set()
lv_text.place(relx = 0.55, rely = 0.46)
#MP輸入格
mp_text = tk.Entry()
mp_text.config(width = 10, font = ('consolas',15), fg = 'white', bg = 'chocolate')
mp_text.focus_set()
mp_text.place(relx = 0.55, rely = 0.51)

#語言
language_label = tk.Label(anchor = 'ne', text = 'Language:', width = 9, font = ('Courier New',15,'bold'), fg = 'maroon', bg = 'chocolate')
language_label.place(relx = 0.53, rely = 0.41)

var02 = tk.IntVar()

rd01 = tk.Radiobutton(root, text = 'English', font = ('Courier New',12,'bold'), fg = 'maroon', bg = 'chocolate', variable = var02, value = 0)
rd01.place(relx = 0.63, rely = 0.41)

rd02 = tk.Radiobutton(root, text = '中文', font = ('Courier New',12,'bold'), fg = 'maroon', bg = 'chocolate', variable = var02, value = 1)
rd02.place(relx = 0.72, rely = 0.41)

rd01.invoke()

#職業圖片
job_image1 = ImageTk.PhotoImage(file = 'images/wallpapers/0.png')
job_image2 = ImageTk.PhotoImage(file = 'images/wallpapers/1.png')
job_image3 = ImageTk.PhotoImage(file = 'images/wallpapers/2.png')
job_image4 = ImageTk.PhotoImage(file = 'images/wallpapers/3.png')
job_image5 = ImageTk.PhotoImage(file = 'images/wallpapers/4.png')
job_image6 = ImageTk.PhotoImage(file = 'images/wallpapers/5.png')

#職業選擇
job_label = tk.Label(anchor = 'ne', text = 'Class:', width = 6, font = ('Courier New',15,'bold'), fg = 'maroon', bg = 'chocolate')
job_label.place(relx = 0.48, rely = 0.57)

option_list = ['Warrior', 'Fighter', 'Archer', 'Thief', 'Brawler', 'Gunslinger']

var01 = tk.StringVar(root)
var01.set(option_list[0])

combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                                settings={'TCombobox':
                                    {'configure':
                                        {
                                            'foreground': 'maroon',  # 前景色
                                            'selectbackground': 'chocolate',  # 选择后的背景颜色
                                            'fieldbackground': 'chocolate',  # 下拉框颜色
                                            'background': 'chocolate',  # 下拉按钮颜色
                                        }}}
                                )
combostyle.theme_use('combostyle')
bigfont = ('Courier New', '15', 'bold')
root.option_add("*TCombobox*Listbox*Font", bigfont)


drop_down_list = ttk.Combobox(root, textvariable=var01, state='readonly',font=bigfont)
drop_down_list['values'] =option_list
drop_down_list.current(0)

drop_down_list.bind('<<ComboboxSelected>>', callback_function)

drop_down_list.place(relx = 0.57, rely = 0.57)


#計算按鈕
button_image1 = ImageTk.PhotoImage(file = 'images/wallpapers/maple1.png')
button_image2 = ImageTk.PhotoImage(file = 'images/wallpapers/maple2.png')
calculate_button = tk.Button(root, image = button_image1, command=calculate, bg = 'chocolate')

calculate_button.bind('<Enter>', on_enter)
calculate_button.bind('<Leave>', on_leave)

calculate_button.place(relx = 0.73, rely = 0.45)
#計算結果
message_lable = tk.Label()
message_lable.config(anchor = 'ne', justify = 'left', font = ('微軟正黑體',18), bg = 'chocolate', fg = 'white')
message_lable.place(relx = 0.478, rely = 0.627)

root.iconbitmap('images/maple.ico')

root.mainloop()
