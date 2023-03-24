import tkinter as tk

root = tk.Tk()
root.title('基本版計算機')
root.resizable(False, False)

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
width = 238
height = 295
left = int((window_width - width)/2)
top = int((window_height - height)/2)
root.geometry(f'{width}x{height}+{left}+{top}')

a = 0
num = tk.StringVar()
num.set('')
label = tk.Label(root, textvariable=num,
                borderwidth=1, relief='solid',
                background='#fff', width=14,
                font=('Arial',20), justify='left',
                anchor='e')
label.place(x=5, y=10)

# 計算函式
def test(e):
    global a
    # 如果按下等於
    if e == 'equal':
        a = eval(a)   # 使用 eval() 計算
        num.set(a)    # 設定顯示的文字變數
        a = 0         # 歸零
    # 如果按下AC
    elif e == 'empty':
        a = 0         # 歸零
        num.set(a)
    else:
        # 如果目前的數字不是 0
        if a != 0:
            a = f'{a}{e}'   # 字串相加
        else:
            a = f'{e}'      # 顯示輸入的字串
        num.set(a)




btn_7 = tk.Button(root, text='7', font=('Arial',20), width=2, command=lambda: test(7))
btn_7.place(x=8, y=50)
btn_8 = tk.Button(root, text='8', font=('Arial',20), width=2, command=lambda: test(8))
btn_8.place(x=68, y=50)
btn_9 = tk.Button(root, text='9', font=('Arial',20), width=2, command=lambda: test(9))
btn_9.place(x=128, y=50)
btn_a = tk.Button(root, text='+', font=('Arial',20), width=2, command=lambda: test('+'))
btn_a.place(x=188, y=50)

btn_4 = tk.Button(root, text='4', font=('Arial',20), width=2, command=lambda: test(4))
btn_4.place(x=8, y=110)
btn_5 = tk.Button(root, text='5', font=('Arial',20), width=2, command=lambda: test(5))
btn_5.place(x=68, y=110)
btn_6 = tk.Button(root, text='6', font=('Arial',20), width=2, command=lambda: test(6))
btn_6.place(x=128, y=110)
btn_b = tk.Button(root, text='-', font=('Arial',20), width=2, command=lambda: test('-'))
btn_b.place(x=188, y=110)

btn_3 = tk.Button(root, text='3', font=('Arial',20), width=2, command=lambda: test(3))
btn_3.place(x=8, y=170)
btn_2 = tk.Button(root, text='2', font=('Arial',20), width=2, command=lambda: test(2))
btn_2.place(x=68, y=170)
btn_1 = tk.Button(root, text='1', font=('Arial',20), width=2, command=lambda: test(1))
btn_1.place(x=128, y=170)
btn_c = tk.Button(root, text='x', font=('Arial',20), width=2, command=lambda: test('*'))
btn_c.place(x=188, y=170)

btn_ac = tk.Button(root, text='AC', font=('Arial',20), width=2, command=lambda: test('empty'))
btn_ac.place(x=8, y=230)
btn_0 = tk.Button(root, text='0', font=('Arial',20), width=2, command=lambda: test(0))
btn_0.place(x=68, y=230)
btn_e = tk.Button(root, text='=', font=('Arial',20), width=2, command=lambda: test('equal'))
btn_e.place(x=128, y=230)
btn_d = tk.Button(root, text='/', font=('Arial',20), width=2, command=lambda: test('/'))
btn_d.place(x=188, y=230)

root.mainloop()