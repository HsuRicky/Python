import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import Healthy as hy

win = tk.Tk()
myHy = hy.Healthy()
def BMI():
    high = txtHigh.get()
    weight = txtWeight.get()
    try:
        if high == '' or weight == '':
            msg.showinfo(title='提示', message='身高或體重不可為空白喔！')
        else:
            bmi = myHy.BMI(float(high), float(weight))
            labMsg['text'] = f'你的BMI => {bmi}'
    except:
        msg.showerror(title='警告', message='身高或體重格式錯誤喔！')

def BMR():
    sex = cmbSex.get()
    high = txtHigh.get()
    weight = txtWeight.get()
    age = txtAge.get()
    try:
        if sex == '' or high == '' or weight == '' or age == '':
            msg.showinfo(title='提示', message='性別或年齡或身高或體重不可為空白喔！')
        else:
            bmr = myHy.BMR(sex, float(high), float(weight), float(age))
            labMsg['text'] = f'你的BMR => {bmr}'
    except:
        msg.showerror(title='警告', message='年齡或身高或體重格式錯誤喔！')

def TDEE():
    sex = cmbSex.get()
    high = txtHigh.get()
    weight = txtWeight.get()
    age = txtAge.get()
    sport = cmbSport.get()
    try:
        if sex == '' or high == '' or weight == '' or age == '' or sport == '':
            msg.showinfo(title='提示', message='表單內容不可為空白喔！')
        else:
            tdee = myHy.TDEE(sex, float(high), float(weight), float(age), sport)
            labMsg['text'] = f'你的TDEE => {tdee}'
    except:
        msg.showerror(title='警告', message='年齡或身高或體重格式錯誤喔！')

win.title('健康管理系統')
window_width = win.winfo_screenwidth()    # 取得螢幕寬度
window_height = win.winfo_screenheight()  # 取得螢幕高度

width = 330
height = 200
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
win.geometry(f'{width}x{height}+{left}+{top}')
# win.configure(background='#fff')   # 設定背景色黑色


labSex = tk.Label(win, text="性            別")
labSex.grid(row=0, column=0)
cmbSex = ttk.Combobox(win, values=['男', '女'], width=15)
cmbSex.grid(row=0, column=1)

labAge = tk.Label(win, text="年            齡")
labAge.grid(row=1, column=0)
txtAge = tk.Entry(win)
txtAge.grid(row=1, column=1)

labHigh = tk.Label(win, text="身            高")
labHigh.grid(row=2, column=0)
txtHigh = tk.Entry(win)
txtHigh.grid(row=2, column=1)

labWeight = tk.Label(win, text="體            重")
labWeight.grid(row=3, column=0)
txtWeight = tk.Entry(win)
txtWeight.grid(row=3, column=1)


labSport = tk.Label(win, text="日常活動量")
labSport.grid(row=4, column=0)
cmbSport = ttk.Combobox(win, values=['久坐(辦公室工作、沒有運動習慣)',
                                     '輕度(運動1-2天/週)',
                                     '中度(運動3-5天/週)',
                                     '高度(運動6-7天/週)',
                                     '極高度(運動員等級，每天運動2次)'], width=25)
cmbSport.grid(row=4, column=1)

labMsg = tk.Label(win, text="", width=20)
labMsg.grid(row=5, column=1)

btnScale = tk.Button(win, text="BMI", command=BMI)
btnScale.grid(row=6, column=0)

btnScale = tk.Button(win, text="BMR", command=BMR)
btnScale.grid(row=6, column=1)

btnScale = tk.Button(win, text="TDEE", command=TDEE)
btnScale.grid(row=6, column=2)

win.mainloop()