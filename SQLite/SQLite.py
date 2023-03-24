import sqlite3

conn = sqlite3.connect('db/0316.db')

#rs = conn.cursor()

# 新增至member
def InsertData():
    user_choice_id = input('enter your id:')
    user_choice_name = input('enter your name:')
    user_choice_phone = input('enter your phone:')
    user_choice_addr = input('enter your addr:')
    try:
        sql = f"insert into member values('{user_choice_id}', '{user_choice_name}', '{user_choice_phone}', '{user_choice_addr}')"
        rs = conn.execute(sql)

    except sqlite3.IntegrityError:
        print("id不可重複哦!")


# 刪除memeber中的data
def DeleteData():
    user_choice_id = input('enter delete id:')
    sql = f"delete from member where id = '{user_choice_id}'"
    rs = conn.execute(sql)


# 修改memeber中的某個id的phone
def UpdataData():
    user_choice_id = input('enter update id:')
    user_choice_phone = input('enter update your choice\'s phone:')
    sql = f"update member set phone = '{user_choice_phone}' where id = '{user_choice_id}'"
    rs = conn.execute(sql)


# 查詢
def SelectData():
    #sql_select = 'select * from member'  # 查詢member中所有的資料
    sql_select = 'select id from member'  # 查詢member中的所有id
    rs = conn.execute(sql_select)
    for row in rs.fetchall():
        #print(f"id:{row[0]}, name:{row[1]}  phone:{row[2]}  addr:{row[3]}  ")
        print(row)


# 查詢各個table的對應關係
def InquiryData():
    print("Meber的id對應到orders的id")
    sql = "select * from member, orders where member.id == orders.member_id and member.id='A000000001'"
    rs = conn.execute(sql)
    for row in rs.fetchall():
        print(row)

    print("\nOrders的order_id對應到orders_detail的order_id")
    rs1 = conn.execute("select * from orders, orders_detail where orders.order_id == orders_detail.order_id")
    for row in rs1.fetchall():
        print(row)

    print("\nOrders_detail的product_id對應到product的product_id")
    rs2 = conn.execute("select * from orders_detail, product where orders_detail.product_id == product.product_id")
    for row in rs2.fetchall():
        print(row)




# SelectData()
# InsertData()
# UpdataData()
# DeleteData()
# InquiryData()



conn.commit()
conn.close()