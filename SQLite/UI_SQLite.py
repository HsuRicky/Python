import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import sqlite3

windows = tk.Tk()

def SQLite():
    conn = sqlite3.connect('db/0316.db')
    def SelectData():
        user_choice_id = txtID.get()
        user_choice_name = txtName.get()
        user_choice_phone = txtPhone.get()
        user_choice_addr = txtAddr.get()

        sql_select = 'select * from member'  # 查詢member中所有的資料
        rs = conn.execute(sql_select)
        for row in rs.fetchall():
            print(f"id:{row[0]}, name:{row[1]}  phone:{row[2]}  addr:{row[3]}  ")

    def InsertData():
        sql_select = 'select id from member'
        rs = conn.execute(sql_select)
        idList = []
        for row in rs.fetchall():
            idList.append(row[0])

        user_choice_id = txtID.get()
        user_choice_name = txtName.get()
        user_choice_phone = txtPhone.get()
        user_choice_addr = txtAddr.get()
        try:
            if user_choice_id  not in idList:
                sql = f"insert into member values('{user_choice_id}', '{user_choice_name}', '{user_choice_phone}', '{user_choice_addr}')"
                conn.execute(sql)
                labMsg['text'] = f"ID:{user_choice_id}已新增成功！"
            else:
                msg.showinfo(title="提示", message="ID已被使用，不可重複！")
                labMsg['text'] = ""
        except sqlite3.OperationalError:
            msg.showinfo(title="提示", message="ID欄位不得空白！")
            labMsg['text'] = ""

    def UpdataData():
        sql_select = 'select id from member'
        rs = conn.execute(sql_select)
        idList = []
        for row in rs.fetchall():
            idList.append(row[0])

        user_choice_id = txtID.get()
        user_choice_name = txtName.get()
        user_choice_phone = txtPhone.get()
        user_choice_addr = txtAddr.get()
        if user_choice_id in idList:
            sql = f"'update member set name = '{user_choice_name}' , phone = '{user_choice_phone}' , addr = '{user_choice_addr}' where id = '{user_choice_id}'"
            conn.execute(sql)
            labMsg['text'] = f"ID:{user_choice_id}已修改成功！"
        else:
            msg.showinfo(title="提示", message="查無此ID！")
            labMsg['text'] = ""

    def DeleteData():
        sql_select = 'select id from member'
        rs = conn.execute(sql_select)
        idList = []
        for row in rs.fetchall():
            idList.append(row[0])

        user_choice_id = txtID.get()
        if user_choice_id in idList:
            sql = f"delete from member where id = '{user_choice_id}'"
            conn.execute(sql)
            labMsg['text'] = f"ID:{user_choice_id}已刪除！"
        else:
            msg.showinfo(title="提示", message="查無此ID！")
            labMsg['text'] = ""

    if cmbChoice.get() == '新增':
        InsertData()
    elif cmbChoice.get() == '查詢':
        pass
    elif cmbChoice.get() == '刪除':
        DeleteData()
    elif cmbChoice.get() == '修改':
        UpdataData()
    else:
        msg.showinfo(title="提示", message="必須選擇要使用的功能！")

    conn.commit()
    conn.close()


windows.title('SQlite管理系統')
window_width = windows.winfo_screenwidth()    # 取得螢幕寬度
window_height = windows.winfo_screenheight()  # 取得螢幕高度

width = 250
height = 180
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
windows.geometry(f'{width}x{height}+{left}+{top}')
windows.resizable(False, False)  # 不可調整視窗大小
# windows.configure(background='#fff')   # 設定背景色黑色

labChoice = tk.Label(windows, text="功能選擇")
labChoice.grid(row=0, column=0)
cmbChoice = ttk.Combobox(windows, values=['查詢', '新增', '修改', '刪除'], state='readonly', width=4)
cmbChoice.grid(row=0, column=1)

labID = tk.Label(windows, text="ID")
labID.grid(row=1, column=0)
txtID = tk.Entry(windows)
txtID.grid(row=1, column=1)

labName = tk.Label(windows, text="Name")
labName.grid(row=2, column=0)
txtName = tk.Entry(windows)
txtName.grid(row=2, column=1)

labPhone = tk.Label(windows, text="Phone")
labPhone.grid(row=3, column=0)
txtPhone = tk.Entry(windows)
txtPhone.grid(row=3, column=1)

labAddr = tk.Label(windows, text="Address")
labAddr.grid(row=4, column=0)
txtAddr = tk.Entry(windows)
txtAddr.grid(row=4, column=1)



labMsg = tk.Label(windows, text="", width=25)
labMsg.grid(row=5, column=1)

btnScale = tk.Button(windows, text="  確定   ", command=SQLite)
btnScale.grid(row=6, column=1)



windows.mainloop()